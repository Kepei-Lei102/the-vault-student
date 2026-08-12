"""
Manim — "keeping every execution unit fed" for
CS/Hardware Systems/Pipelining and Simultaneous Multithreading.md

A simplified, procedural animation of a RISC core's out-of-order engine. The
front-end (L1-I -> fetch -> decode) streams ops into the op queue / reorder
buffer; an out-of-order SCHEDULER fires every *ready* op into any free
execution unit each cycle. You watch:
  - the units fill up (superscalar: several dispatched per cycle),
  - a not-yet-ready op wait in the queue while younger ops pass it (OOO),
  - a cache-missed load tie up Load/Store while the ALUs keep cycling,
  - the branch predictor keep the front-end fed (speculation),
  - a HUD counting 'units busy this cycle'.

Two configs share this script:
  SimplifiedCore  — clean teaching core (4-wide, 3 ALU + 2 SIMD + 1 Ld/St)
  FirestormCore   — Apple-Firestorm-style (8-wide, 6 ALU + 4 SIMD + 2 Ld/St)

Render (still layout check):  PIPE_STILL=1 manim -s -ql core-pipeline-fill.py SimplifiedCore
Render (video):               manim -qh core-pipeline-fill.py SimplifiedCore
                              manim -qh core-pipeline-fill.py FirestormCore
  then copy media/videos/.../<Scene>.mp4 beside the card and rm -rf media.
"""
import os
from manim import *

BG="#1e1e1e"; TXT="#cccccc"; DIM="#888888"
GREEN="#059669"; AMBER="#f59e0b"; TEAL="#0891b2"; BLUE="#2563eb"; PURPLE="#7c3aed"; RED="#dc2626"
config.background_color = BG

TYPE_COL = {'int':GREEN, 'fp':AMBER, 'mem':TEAL}
TYPE_UNIT = {'int':'ALU', 'fp':'SIMD', 'mem':'LD'}
STILL = os.environ.get("PIPE_STILL")

# deterministic op stream (int-heavy, some fp, some mem)
PATTERN = (['int','int','fp','int','mem','int','fp','int','int','mem','fp','int']*6)


class CoreFillBase(Scene):
    # ---- per-core config (overridden) ----
    TITLE = "A RISC core"
    L1 = "L1-I"
    FETCHW = 4
    DECODE = "decode (4-wide)"
    ROB = "reorder buffer"
    UNIT_SPEC = [('int',3),('fp',2),('mem',1)]   # (type, count)
    NSLOT = 14
    NCYC = 9
    UBOXW = 1.15

    def construct(self):
        cfg_units = []
        for t,n in self.UNIT_SPEC:
            cfg_units += [t]*n
        NU = len(cfg_units)

        # ---------- static layout ----------
        title = Text(self.TITLE, color=TXT, weight=BOLD, font_size=28).to_edge(UP, buff=0.12)
        sub = Text("the out-of-order engine keeps every execution unit fed", color=DIM, font_size=17)
        sub.next_to(title, DOWN, buff=0.16)

        def lbox(txt, col, w, h, fs=18):
            r = RoundedRectangle(width=w, height=h, corner_radius=0.08, stroke_color=col,
                                 stroke_width=2, fill_color=col, fill_opacity=0.10)
            t = Text(txt, color=col, font_size=fs)
            if t.width > w-0.16: t.scale((w-0.16)/t.width)
            return VGroup(r, t)

        # front-end row
        l1 = lbox(self.L1, BLUE, 1.5, 0.62).move_to([-5.9, 2.05, 0])
        fetch = lbox(f"fetch x{self.FETCHW}", BLUE, 1.5, 0.62).move_to([-4.05, 2.05, 0])
        dec = lbox(self.DECODE, PURPLE, 1.9, 0.62).move_to([-1.85, 2.05, 0])
        pred = lbox("branch predictor", BLUE, 2.0, 0.5, 15).move_to([-4.05, 3.05, 0])
        fe_arrows = VGroup(
            Arrow(l1.get_right(), fetch.get_left(), buff=0.05, color=DIM, stroke_width=2, max_tip_length_to_length_ratio=0.18),
            Arrow(fetch.get_right(), dec.get_left(), buff=0.05, color=DIM, stroke_width=2, max_tip_length_to_length_ratio=0.18),
            Arrow(pred.get_bottom(), fetch.get_top(), buff=0.05, color=BLUE, stroke_width=2, max_tip_length_to_length_ratio=0.2),
        )

        # op queue slots
        qy = 1.15
        xs = [-5.7 + i*(11.4/(self.NSLOT-1)) for i in range(self.NSLOT)]
        slot_w = min(0.62, (11.4/(self.NSLOT-1))-0.06)
        slots = VGroup(*[RoundedRectangle(width=slot_w, height=0.46, corner_radius=0.05,
                          stroke_color=DIM, stroke_width=1, fill_opacity=0).set_opacity(0.5).move_to([x, qy, 0]) for x in xs])
        qlabel = Text("op queue / reorder buffer  (program order ->)", color=DIM, font_size=15)
        qlabel.next_to(slots, UP, buff=0.16)

        # scheduler bar
        sched = RoundedRectangle(width=11.6, height=0.5, corner_radius=0.1, stroke_color=AMBER,
                                 stroke_width=2, fill_color=AMBER, fill_opacity=0.08).move_to([0, 0.15, 0])
        sched_t = Text("out-of-order scheduler  —  fire every READY op into any free unit",
                       color=AMBER, font_size=17).move_to(sched.get_center())

        # execution units row
        uy = -1.95
        uxs = [-6.5 + i*(13.0/(NU-1)) for i in range(NU)] if NU>1 else [0]
        units=[]
        ugroup=VGroup()
        for i,t in enumerate(cfg_units):
            col = TYPE_COL[t]
            b = RoundedRectangle(width=self.UBOXW, height=0.86, corner_radius=0.07, stroke_color=col,
                                 stroke_width=2, fill_color=col, fill_opacity=0.10).move_to([uxs[i], uy, 0])
            lab = Text(TYPE_UNIT[t], color=col, font_size=15).move_to([uxs[i], uy-0.27, 0])
            ugroup.add(b, lab)
            units.append({'type':t,'center':[uxs[i],uy+0.11,0],'box':b,'busy_until':-1,'token':None,'stall':False})
        # faint dispatch guide lines (scheduler -> each unit)
        guides = VGroup(*[Line([uxs[i], -0.12, 0], [uxs[i], uy+0.48, 0], stroke_color=DIM, stroke_width=1).set_opacity(0.16) for i in range(NU)])
        # group brackets
        grp_labels=VGroup()
        seen={}
        for i,t in enumerate(cfg_units):
            seen.setdefault(t,[]).append(uxs[i])
        names={'int':'integer  (ALU)','fp':'FP / SIMD','mem':'load / store'}
        for t,xsg in seen.items():
            gl = Text(names[t], color=TYPE_COL[t], font_size=15)
            gl.move_to([sum(xsg)/len(xsg), uy+0.62, 0])
            grp_labels.add(gl)

        # HUD
        hud_cyc = Text("cycle 0", color=TXT, font_size=20).move_to([-5.4, -3.35, 0])
        self.busy_txt = Text("units busy this cycle: 0 / %d" % NU, color=TXT, font_size=20).move_to([0.2, -3.35, 0])
        barx0 = 3.7; barw=2.6
        bar_bg = RoundedRectangle(width=barw, height=0.26, corner_radius=0.06, stroke_color=DIM, stroke_width=1, fill_opacity=0).move_to([barx0+barw/2, -3.35, 0])
        self.bar_bg = bar_bg
        self.bar_fill = Rectangle(width=0.001, height=0.26, stroke_width=0, fill_color=GREEN, fill_opacity=0.55)
        self.bar_fill.move_to([barx0, -3.35, 0])
        self.barx0=barx0; self.barw=barw; self.NU=NU

        layout = VGroup(l1,fetch,dec,pred,fe_arrows,slots,qlabel,guides,sched,sched_t,ugroup,grp_labels,
                        hud_cyc,self.busy_txt,bar_bg,self.bar_fill)
        self.l1_c = l1.get_center()
        self.qslots = [[x,qy,0] for x in xs]
        self.units = units
        self.hud_cyc = hud_cyc

        # ---------- STILL: representative mid-state ----------
        if STILL:
            self.add(title, sub, layout)
            for i in range(min(8,self.NSLOT)):
                tok = self.token(i+1, PATTERN[i])
                tok.move_to(self.qslots[i]); self.add(tok)
            for j,u in enumerate(units[:max(1,NU-1)]):
                tok = self.token(20+j, u['type']); tok.move_to(u['center']); self.add(tok)
            self.wait(0.2); return

        # ---------- intro ----------
        self.play(FadeIn(title), FadeIn(sub))
        self.play(FadeIn(layout), run_time=1.0)
        self.wait(0.3)

        # ---------- procedural cycles ----------
        queue=[]          # {mob,type,ready_at}
        stream=list(PATTERN)
        nid=1
        did_stall=False; did_pred=False
        pred_flag=None

        for cyc in range(self.NCYC):
            self.play(self.hud_cyc.animate.become(Text(f"cycle {cyc+1}", color=TXT, font_size=20).move_to(self.hud_cyc.get_center())), run_time=0.2)

            # FRONT-END: fetch new ops into queue
            ins=[]
            for _ in range(self.FETCHW):
                if len(queue) >= self.NSLOT or not stream: break
                t=stream.pop(0)
                tok=self.token(nid,t)
                # make op #5 a not-ready (dependency) op for the OOO demo
                ready_at = cyc
                if nid==5: ready_at = cyc+3
                tok.move_to(self.l1_c)
                self.add(tok)
                slot=len(queue)
                queue.append({'mob':tok,'type':t,'ready_at':ready_at})
                if ready_at>cyc: tok.set_opacity(0.35)
                ins.append(tok.animate.move_to(self.qslots[slot]))
                nid+=1
            if ins: self.play(LaggedStart(*ins, lag_ratio=0.12), run_time=0.7)

            # speculation beat (once): predictor keeps the front-end fed
            if not did_pred and cyc==2:
                did_pred=True
                pred_flag=Text("predict: taken  v", color=BLUE, font_size=15).move_to([-4.05, 3.55, 0])
                self.play(Flash(pred, color=BLUE, line_length=0.15, num_lines=10, flash_radius=0.7), FadeIn(pred_flag), run_time=0.5)

            # wake not-ready ops whose time has come
            wake=[]
            for op in queue:
                if op['ready_at']==cyc+1 or (op['ready_at']<=cyc and op['mob'].get_fill_opacity()<0.9):
                    if op['ready_at']<=cyc+1:
                        wake.append(op['mob'].animate.set_opacity(1.0))
            # (handled below at dispatch readiness)

            # DISPATCH: each free unit grabs the oldest READY matching op
            disp=[]; fired_units=[]
            for u in self.units:
                if u['busy_until']>cyc: continue
                # free the unit if its op just finished
                if u['token'] is not None and u['busy_until']<=cyc:
                    pass
                idx=None
                for k,op in enumerate(queue):
                    if op['type']==u['type'] and op['ready_at']<=cyc:
                        idx=k; break
                if idx is None: continue
                op=queue.pop(idx)
                stall = (u['type']=='mem' and not did_stall and cyc>=2)
                if stall: did_stall=True
                u['busy_until']= cyc + (4 if stall else 1)
                u['stall']=stall
                # retire previous token in this unit if any
                if u['token'] is not None:
                    self.remove(u['token'])
                u['token']=op['mob']
                disp.append(op['mob'].animate.move_to(u['center']).set_opacity(1.0))
                fired_units.append((u,stall))
            if disp: self.play(*disp, run_time=0.55)

            # reflow queue slots — AUTHORITATIVE: move every op to its index slot,
            # combining position + (optional) brighten into ONE animation per token.
            # (Two separate .animate calls on the same mob in one play() drop one of
            # them -> the move was lost and tokens stacked. One chained animation
            # fixes both the overlap and the leftover gaps.)
            reflow=[]
            for i,op in enumerate(queue):
                a=op['mob'].animate.move_to(self.qslots[i])
                if op['ready_at']<=cyc and op['mob'].get_fill_opacity()<0.9:
                    a=a.set_opacity(1.0)
                reflow.append(a)
            if reflow: self.play(*reflow, run_time=0.35)

            # EXECUTE flashes + stall marker
            flashes=[]; marks=[]
            for u,stall in fired_units:
                flashes.append(Flash(u['token'], color=TYPE_COL[u['type']], line_length=0.12, num_lines=8, flash_radius=0.45))
                if stall:
                    m=Text("miss ~200cy", color=RED, font_size=13).next_to(u['box'], DOWN, buff=0.06)
                    u['miss_mark']=m; marks.append(FadeIn(m))
            if flashes: self.play(*flashes, *marks, run_time=0.45)

            # RETIRE 1-cycle ops (free the unit, fade token up) — next cycle they're free
            ret=[]
            for u in self.units:
                if u['token'] is not None and u['busy_until']<=cyc+1:
                    ret.append(FadeOut(u['token'], shift=UP*0.35))
                    u['token']=None
                    if u.get('miss_mark') is not None:
                        ret.append(FadeOut(u['miss_mark'])); u['miss_mark']=None
            if ret: self.play(*ret, run_time=0.35)

            # HUD busy + bar
            busy=sum(1 for u in self.units if u['token'] is not None or u['busy_until']>cyc)
            self.update_hud(busy)

        # ---------- payoff ----------
        punch = Text("almost every unit busy, almost every cycle —", color=TXT, font_size=22)
        punch2 = Text("the whole art of the modern core", color=GREEN, font_size=22, weight=BOLD)
        pg=VGroup(punch,punch2).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.45)
        self.play(FadeOut(self.hud_cyc), FadeOut(self.busy_txt), FadeOut(self.bar_fill), FadeOut(self.bar_bg))
        self.play(FadeIn(pg, shift=UP*0.2)); self.wait(2.0)

    # ---- helpers ----
    def token(self, idn, ttype):
        col=TYPE_COL[ttype]
        sq=RoundedRectangle(width=0.4, height=0.4, corner_radius=0.06, stroke_color=col,
                            stroke_width=2, fill_color=col, fill_opacity=0.30)
        t=Text(str(idn), color=TXT, font_size=15).move_to(sq.get_center())
        return VGroup(sq,t)

    def update_hud(self, busy):
        busy=min(busy, self.NU)
        self.play(
            self.busy_txt.animate.become(Text(f"units busy this cycle: {busy} / {self.NU}", color=TXT, font_size=20).move_to(self.busy_txt.get_center())),
            self.bar_fill.animate.become(Rectangle(width=max(0.001,self.barw*busy/self.NU), height=0.26, stroke_width=0,
                fill_color=(GREEN if busy>=self.NU*0.7 else AMBER), fill_opacity=0.55).move_to([self.barx0+self.barw*busy/self.NU/2, -3.35, 0])),
            run_time=0.3)


class SimplifiedCore(CoreFillBase):
    TITLE="A RISC core — keeping the units fed"
    L1="L1-I"; FETCHW=4; DECODE="decode x4"; UBOXW=1.15
    UNIT_SPEC=[('int',3),('fp',2),('mem',1)]
    NSLOT=12; NCYC=9


class FirestormCore(CoreFillBase):
    TITLE="Apple Firestorm-style core (8-wide, 630 ROB)"
    L1="192KB L1-I"; FETCHW=8; DECODE="decode x8"; ROB="630 ROB"; UBOXW=0.92
    UNIT_SPEC=[('int',6),('fp',4),('mem',2)]
    NSLOT=16; NCYC=9
