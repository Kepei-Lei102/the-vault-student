"""
Manim — the fetch-decode-execute cycle, register by register, for
CS/Hardware Systems/CPU Architecture and the Fetch-Execute Cycle.md

Traces the card's worked example C = A + B (LOAD 50; ADD 51; STORE 52) through
the von Neumann datapath: a phase banner (FETCH / DECODE / EXECUTE), values
moving along the address/data/control buses, and the registers (PC, MAR, MDR,
CIR, ACC) updating live. Instruction 1 is shown in full micro-step detail; the
other two complete the loop so the ACC builds 5 -> 8 -> stored.

Render (still):  PIPE_STILL=1 manim -s -ql fde-cycle.py FetchExecuteCycle
Render (4K):     manim -qk fde-cycle.py FetchExecuteCycle
  then copy media/videos/fde-cycle/2160p60/FetchExecuteCycle.mp4 -> ./fde-cycle.mp4 ; rm -rf media
"""
import os
from manim import *

BG="#1e1e1e"; TXT="#cccccc"; DIM="#888888"
BLUE="#2563eb"; PURPLE="#7c3aed"; GREEN="#059669"; AMBER="#f59e0b"; TEAL="#0891b2"; RED="#dc2626"
config.background_color = BG
STILL=os.environ.get("PIPE_STILL")

class FetchExecuteCycle(Scene):
    def construct(self):
        title=Text("The fetch-decode-execute cycle", color=TXT, weight=BOLD, font_size=30).to_edge(UP, buff=0.18)
        self.phase_mob=Text("", font_size=26, weight=BOLD).move_to([0,3.0,0])
        self.cap_mob=Text("one loop, repeated billions of times a second", color=DIM, font_size=20).to_edge(DOWN, buff=0.35)
        self.add(title)

        # ---------- CPU ----------
        cpu=RoundedRectangle(width=5.6, height=5.6, corner_radius=0.12, stroke_color=PURPLE, stroke_width=2,
                             fill_color=PURPLE, fill_opacity=0.04).move_to([-3.9,-0.25,0])
        cpu_lab=Text("CPU", color=PURPLE, font_size=20, weight=BOLD).move_to([-6.2,2.15,0])
        cu=self.unit("Control Unit", PURPLE, [-5.5,1.5,0], 2.0,0.62)
        alu=self.unit("ALU", GREEN, [-5.5,-1.9,0], 2.0,0.7)
        self.add(cpu,cpu_lab,cu,alu)

        # registers (name + live value)
        self.regval={}; self.regcell={}; self.regcenter={}
        regs=[("PC",BLUE,1.85),("MAR",BLUE,1.15),("MDR",TEAL,0.45),("CIR",PURPLE,-0.25),("ACC",GREEN,-1.15)]
        for name,col,y in regs:
            cell=RoundedRectangle(width=2.5,height=0.56,corner_radius=0.06,stroke_color=col,stroke_width=1.6,
                                  fill_color=col,fill_opacity=0.10).move_to([-3.0,y,0])
            nm=Text(name,color=col,font_size=16,weight=BOLD).move_to([-3.75,y,0])
            vb=RoundedRectangle(width=1.5,height=0.4,corner_radius=0.04,stroke_color=DIM,stroke_width=1,
                                fill_opacity=0).move_to([-2.55,y,0])
            val=Text("",color=TXT,font_size=15).move_to([-2.55,y,0])
            self.add(cell,nm,vb,val); self.regcell[name]=cell; self.regval[name]=val; self.regcenter[name]=[-2.55,y,0]

        # ---------- Memory ----------
        mem=RoundedRectangle(width=3.7,height=5.2,corner_radius=0.12,stroke_color=TEAL,stroke_width=2,
                             fill_color=TEAL,fill_opacity=0.05).move_to([4.9,-0.05,0])
        mem_lab=Text("Main Memory (RAM)",color=TEAL,font_size=18,weight=BOLD).move_to([4.9,2.2,0])
        self.add(mem,mem_lab)
        self.memval={}; self.memcell={}; self.memcenter={}
        rows=[("0","LOAD 50",1.6,PURPLE),("1","ADD 51",1.05,PURPLE),("2","STORE 52",0.5,PURPLE),
              ("50","5",-0.45,GREEN),("51","3",-1.0,GREEN),("52","",-1.55,GREEN)]
        for addr,v,y,col in rows:
            nm=Text(addr,color=DIM,font_size=14).move_to([3.65,y,0])
            cell=RoundedRectangle(width=2.2,height=0.44,corner_radius=0.05,stroke_color=col,stroke_width=1.3,
                                  fill_color=col,fill_opacity=0.10).move_to([5.25,y,0])
            val=Text(v,color=TXT,font_size=14).move_to([5.25,y,0])
            self.add(nm,cell,val); self.memcell[addr]=cell; self.memval[addr]=val; self.memcenter[addr]=[5.25,y,0]
        self.add(Text("instructions",color=PURPLE,font_size=12).move_to([5.25,1.92,0]))
        self.add(Text("data",color=GREEN,font_size=12).move_to([5.25,-0.13,0]))

        # ---------- buses ----------
        self.bus={}
        for y,name,col in [(1.25,"address bus",BLUE),(0.15,"data bus",TEAL),(-0.95,"control bus",AMBER)]:
            ln=Line([-1.55,y,0],[3.0,y,0],color=col,stroke_width=3).set_opacity(0.5)
            self.bus[name]=ln
            self.add(ln, Text(name,color=col,font_size=13).move_to([0.7,y+0.22,0]))

        self.add(self.phase_mob,self.cap_mob)

        if STILL:
            self.regval["PC"].become(Text("1",color=TXT,font_size=15).move_to(self.regcenter["PC"]))
            self.regval["CIR"].become(Text("LOAD 50",color=TXT,font_size=14).move_to(self.regcenter["CIR"]))
            self.regval["ACC"].become(Text("5",color=TXT,font_size=15).move_to(self.regcenter["ACC"]))
            self.set_phase_static("EXECUTE",GREEN)
            self.wait(0.2); return

        # =========================================================== TRACE
        # ---- Instruction 1: LOAD 50  (full detail) ----
        self.phase("FETCH",BLUE)
        self.reg_set("PC","0",rt=0.4)
        self.cap("PC holds the address of the next instruction: 0")
        self.transfer("0",BLUE,"PC","MAR","address bus",to_reg=True)
        self.reg_set("MAR","0")
        self.cap("PC -> MAR: copy that address into the MAR")
        self.flash_bus("control bus","read")
        self.transfer("LOAD 50",PURPLE,None,"MDR","data bus",src_mem="0")
        self.reg_set("MDR","LOAD 50",col=PURPLE)
        self.cap("read memory[0] over the data bus -> MDR")
        self.transfer("LOAD 50",PURPLE,"MDR","CIR",None,to_reg=True)
        self.reg_set("CIR","LOAD 50",col=PURPLE)
        self.cap("MDR -> CIR: the instruction is now ready to decode")
        self.reg_set("PC","1")
        self.cap("PC + 1: point at the next instruction (now 1)")

        self.phase("DECODE",PURPLE)
        self.play(Indicate(self.regcell["CIR"],color=PURPLE), Indicate(self.regval["CIR"],color=PURPLE), run_time=0.6)
        self.cap("CU splits CIR into opcode LOAD and operand 50")

        self.phase("EXECUTE",GREEN)
        self.transfer("50",BLUE,"CIR","MAR","address bus",to_reg=True,val_override="50")
        self.reg_set("MAR","50")
        self.cap("operand 50 -> MAR")
        self.flash_bus("control bus","read")
        self.transfer("5",GREEN,None,"MDR","data bus",src_mem="50")
        self.reg_set("MDR","5",col=GREEN)
        self.cap("read memory[50] = 5 over the data bus -> MDR")
        self.transfer("5",GREEN,"MDR","ACC",None,to_reg=True)
        self.reg_set("ACC","5",col=GREEN)
        self.cap("LOAD done: ACC = 5")
        self.wait(0.4)

        # ---- Instruction 2: ADD 51 ----
        self.phase("FETCH",BLUE)
        self.transfer("1",BLUE,"PC","MAR","address bus",to_reg=True)
        self.reg_set("MAR","1")
        self.flash_bus("control bus","read")
        self.transfer("ADD 51",PURPLE,None,"MDR","data bus",src_mem="1")
        self.reg_set("MDR","ADD 51",col=PURPLE); self.reg_set("CIR","ADD 51",col=PURPLE,rt=0.4)
        self.reg_set("PC","2",rt=0.4)
        self.cap("fetch ADD 51, PC -> 2")
        self.phase("EXECUTE",GREEN)
        self.transfer("51",BLUE,"CIR","MAR","address bus",to_reg=True)
        self.reg_set("MAR","51")
        self.flash_bus("control bus","read")
        self.transfer("3",GREEN,None,"MDR","data bus",src_mem="51")
        self.reg_set("MDR","3",col=GREEN)
        self.cap("read memory[51] = 3 -> MDR; now the ALU adds")
        # ALU: MDR + ACC -> ACC
        self.alu_add()
        self.reg_set("ACC","8",col=GREEN)
        self.cap("ALU: ACC (5) + MDR (3) = 8 -> ACC")
        self.wait(0.4)

        # ---- Instruction 3: STORE 52 ----
        self.phase("FETCH",BLUE)
        self.transfer("2",BLUE,"PC","MAR","address bus",to_reg=True)
        self.reg_set("MAR","2")
        self.flash_bus("control bus","read")
        self.transfer("STORE 52",PURPLE,None,"MDR","data bus",src_mem="2")
        self.reg_set("MDR","STORE 52",col=PURPLE); self.reg_set("CIR","STORE 52",col=PURPLE,rt=0.4)
        self.reg_set("PC","3",rt=0.4)
        self.cap("fetch STORE 52, PC -> 3")
        self.phase("EXECUTE",GREEN)
        self.reg_set("MDR","8",col=GREEN)
        self.transfer("52",BLUE,"CIR","MAR","address bus",to_reg=True)
        self.reg_set("MAR","52")
        self.flash_bus("control bus","write")
        self.transfer("8",GREEN,"MDR",None,"data bus",dst_mem="52")
        new52=Text("8",color=TXT,font_size=14).move_to(self.memcenter["52"])
        self.play(FadeTransform(self.memval["52"],new52),run_time=0.5); self.memval["52"]=new52
        self.cap("STORE: ACC -> memory[52]. C = 8.")
        self.wait(0.4)

        # ---- finale ----
        self.play(self.phase_mob.animate.become(Text("",font_size=26).move_to(self.phase_mob.get_center())))
        pg=VGroup(Text("C = A + B = 8", color=GREEN, font_size=30, weight=BOLD),
                  Text("every program is this loop, scaled up", color=TXT, font_size=20)).arrange(DOWN,buff=0.12).move_to([0,3.0,0])
        self.play(FadeIn(pg,shift=DOWN*0.2)); self.wait(2.2)

    # ---------- helpers ----------
    def unit(self,label,col,center,w,h):
        b=RoundedRectangle(width=w,height=h,corner_radius=0.07,stroke_color=col,stroke_width=2,fill_color=col,fill_opacity=0.12).move_to(center)
        t=Text(label,color=col,font_size=15).move_to(center)
        return VGroup(b,t)

    def token(self,value,col):
        c=RoundedRectangle(width=max(0.5,0.22*len(str(value))+0.3),height=0.42,corner_radius=0.06,
                           stroke_color=col,stroke_width=2,fill_color=col,fill_opacity=0.30)
        t=Text(str(value),color=TXT,font_size=15,weight=BOLD).move_to(c.get_center())
        return VGroup(c,t)

    def set_phase_static(self,name,col):
        self.phase_mob.become(Text(name,color=col,font_size=26,weight=BOLD).move_to([0,3.0,0]))
    def phase(self,name,col):
        self.play(self.phase_mob.animate.become(Text(name,color=col,font_size=26,weight=BOLD).move_to([0,3.0,0])),run_time=0.4)
    def cap(self,s):
        self.play(self.cap_mob.animate.become(Text(s,color=DIM,font_size=20).to_edge(DOWN,buff=0.35)),run_time=0.3)

    def reg_set(self,name,val,col=None,rt=0.5):
        new=Text(str(val),color=col or TXT,font_size=(15 if len(str(val))<=2 else 14)).move_to(self.regcenter[name])
        self.play(FadeTransform(self.regval[name],new),run_time=rt); self.regval[name]=new

    def flash_bus(self,bus,word):
        ln=self.bus[bus]
        lab=Text(word,color=AMBER,font_size=14,weight=BOLD).move_to([0.7,-0.95-0.0,0])
        self.play(ln.animate.set_opacity(1.0).set_stroke(width=5),FadeIn(lab),run_time=0.35)
        self.play(ln.animate.set_opacity(0.5).set_stroke(width=3),FadeOut(lab),run_time=0.35)

    def transfer(self,value,col,src,dst,bus,to_reg=False,src_mem=None,dst_mem=None,val_override=None):
        # determine source point
        if src_mem is not None: sp=self.memcenter[src_mem]
        elif src is not None: sp=self.regcenter[src]
        else: sp=[-2.55,0.45,0]
        if dst_mem is not None: dp=self.memcenter[dst_mem]
        elif dst is not None: dp=self.regcenter[dst]
        else: dp=[5.25,0.0,0]
        tok=self.token(value if val_override is None else val_override,col); tok.move_to(sp); self.add(tok)
        if bus is not None:
            by=self.bus[bus].get_center()[1]
            self.play(tok.animate.move_to([sp[0],by,0]),run_time=0.3)
            self.play(tok.animate.move_to([dp[0],by,0]),self.bus[bus].animate.set_opacity(0.95),run_time=0.6)
            self.bus[bus].set_opacity(0.5)
            self.play(tok.animate.move_to(dp),run_time=0.3)
        else:
            self.play(tok.animate.move_to(dp),run_time=0.7)
        self.play(FadeOut(tok),run_time=0.2)

    def alu_add(self):
        # MDR and ACC values flow into the ALU, result flows back to ACC
        a=self.token("3",GREEN); a.move_to(self.regcenter["MDR"])
        b=self.token("5",GREEN); b.move_to(self.regcenter["ACC"])
        self.add(a,b)
        alu_c=[-5.5,-1.9,0]
        self.play(a.animate.move_to(alu_c),b.animate.move_to(alu_c),run_time=0.7)
        plus=Text("+",color=GREEN,font_size=28,weight=BOLD).move_to([-5.5,-1.9,0])
        self.play(FadeOut(a),FadeOut(b),FadeIn(plus),run_time=0.3)
        res=self.token("8",GREEN); res.move_to(alu_c)
        self.play(FadeOut(plus),FadeIn(res),run_time=0.2)
        self.play(res.animate.move_to(self.regcenter["ACC"]),run_time=0.6)
        self.play(FadeOut(res),run_time=0.2)
