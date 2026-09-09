"""Manim: packet switching, watched. A message is cut into six numbered packets; each router forwards each packet
along whichever link is free right now, so they take different routes, arrive out of order, one is lost and re-sent,
and the receiver reassembles them by number.
Render: manim -qk networks-packet-switching.py PacketSwitching ; copy MP4 to networks-packet-switching.mp4 ; rm -rf media __pycache__"""
from manim import *
GREY="#888888"; BLUE_K="#2563eb"; GREEN_K="#059669"; RED_K="#dc2626"; AMBER="#f59e0b"; PURPLE_K="#7c3aed"
COLS=[BLUE_K,GREEN_K,PURPLE_K,AMBER,"#0891b2","#db2777"]

class PacketSwitching(Scene):
    def construct(self):
        self.camera.background_color="#1e1e1e"
        title=Text("Packet switching: numbered pieces, independent routes, reassembled at the end",font_size=28,color=GREY).to_edge(UP); self.add(title)
        # routers
        P={"S":np.array([-5.5,0,0]),"A":np.array([-2.5,1.6,0]),"B":np.array([-2.5,-1.6,0]),"C":np.array([0,0,0]),"D":np.array([2.5,1.6,0]),"E":np.array([2.5,-1.6,0]),"R":np.array([5.5,0,0])}
        links=[("S","A"),("S","B"),("A","C"),("B","C"),("A","D"),("B","E"),("C","D"),("C","E"),("D","R"),("E","R"),("A","B"),("D","E")]
        for a,b in links: self.add(Line(P[a],P[b],color=GREY,stroke_width=2,stroke_opacity=0.5))
        for k,v in P.items():
            self.add(Circle(radius=0.32,color=GREY,fill_color="#1e1e1e",fill_opacity=1,stroke_width=2).move_to(v), Text({"S":"sender","R":"receiver"}.get(k,"router"),font_size=16,color=GREY).move_to(v+DOWN*0.55))
        # message and packets
        msg=Text("HELLO, WORLD!",font_size=30,color=GREY).move_to(P["S"]+UP*2.4+RIGHT*0.7)
        self.play(FadeIn(msg)); self.wait(0.5)
        parts=["HE","LL","O,"," W","OR","LD"]
        pk=VGroup(*[VGroup(RoundedRectangle(width=0.62,height=0.42,corner_radius=0.06,color=COLS[i],fill_color=COLS[i],fill_opacity=0.25,stroke_width=2),Text(f"{i+1}",font_size=16,color=COLS[i]).shift(UP*0.08),Text(parts[i],font_size=12,color=GREY).shift(DOWN*0.1)) for i in range(6)]).arrange(RIGHT,buff=0.08).move_to(P["S"]+UP*2.4+RIGHT*0.7)
        self.play(Transform(msg,pk)); self.wait(0.4)
        note=Text("each packet carries: destination, sender, its number, a slice of data, a check",font_size=20,color=GREY).to_edge(DOWN,buff=0.35); self.play(FadeIn(note)); self.wait(1.2); self.play(FadeOut(note))
        routes={0:["S","A","D","R"],1:["S","B","E","R"],2:["S","A","C","E","R"],3:["S","B","C","D","R"],4:["S","A","B","E","R"],5:["S","B","C","D","R"]}
        delays={0:0.0,1:0.2,2:0.4,3:0.6,4:0.8,5:1.0}
        speed={0:0.55,1:0.5,2:0.7,3:0.9,4:0.75,5:0.6}
        note2=Text("a router looks only at the destination address and forwards to the best free link, right now",font_size=20,color=GREY).to_edge(DOWN,buff=0.35); self.play(FadeIn(note2))
        anims=[]; arrival=[]
        for i in range(6):
            p=msg[i] if False else pk[i]
            path=VMobject().set_points_as_corners([P[r] for r in routes[i]])
            arrival.append(delays[i]+speed[i]*(len(routes[i])-1))
            anims.append(Succession(Wait(delays[i]),MoveAlongPath(p,path,rate_func=linear,run_time=speed[i]*(len(routes[i])-1))))
        self.play(*anims); self.play(FadeOut(note2))
        # arrival order
        order=sorted(range(6),key=lambda i: arrival[i])
        slots=VGroup(*[Square(side_length=0.5,color=GREY,stroke_width=1.5) for _ in range(6)]).arrange(RIGHT,buff=0.06).move_to(P["R"]+UP*2.4+LEFT*0.6)
        self.play(FadeIn(slots)); self.play(*[pk[i].animate.scale(0.75).move_to(slots[k]) for k,i in enumerate(order)],run_time=1)
        o=Text("arrived in order " + ", ".join(str(i+1) for i in order),font_size=20,color=GREY).to_edge(DOWN,buff=0.35); self.play(FadeIn(o)); self.wait(1.2)
        # packet 4 got lost: simulate by marking it red and re-requesting
        lost=pk[3]; self.play(lost.animate.set_opacity(0.15)); l=Text("packet 4 damaged in transit: the trailer's check fails — the receiver asks for it again",font_size=20,color=GREY).to_edge(DOWN,buff=0.35); self.play(Transform(o,l))
        req=Dot(color=RED_K).move_to(P["R"]); self.play(MoveAlongPath(req,VMobject().set_points_as_corners([P["R"],P["D"],P["A"],P["S"]]),run_time=1.2,rate_func=linear)); self.remove(req)
        again=VGroup(RoundedRectangle(width=0.62,height=0.42,corner_radius=0.06,color=COLS[3],fill_color=COLS[3],fill_opacity=0.25,stroke_width=2),Text("4",font_size=16,color=COLS[3]).shift(UP*0.08),Text(" W",font_size=12,color=GREY).shift(DOWN*0.1)).move_to(P["S"])
        self.play(FadeIn(again)); self.play(MoveAlongPath(again,VMobject().set_points_as_corners([P["S"],P["A"],P["C"],P["D"],P["R"]]),run_time=1.6,rate_func=linear)); self.play(FadeOut(lost),again.animate.scale(0.75).move_to(slots[order.index(3)]))
        # reorder
        r2=Text("reassemble by packet number",font_size=20,color=GREY).to_edge(DOWN,buff=0.35); self.play(Transform(o,r2))
        allp=[pk[i] if i!=3 else again for i in range(6)]
        self.play(*[allp[i].animate.move_to(slots[i]) for i in range(6)],run_time=1.2)
        final=Text("HELLO, WORLD!",font_size=26,color=GREEN_K).move_to(P["R"]+UP*1.65+LEFT*0.6); self.play(FadeIn(final)); self.wait(2.5)
