"""Pre-rendered student companion. Stack: Manim, chosen by Kepei 2026-09-16.
Regenerate: manim -qk --media_dir /tmp/vault-manim <this-file.py> Companion
Copy the final MP4 beside this source using the matching kebab-case filename.
No external data or temporary-path dependencies; deterministic where stochastic.
"""
from manim import *
import numpy as np
import math

config.background_color = "#1e1e1e"
TXT="#cccccc"; DIM="#888888"; B="#60a5fa"; G="#34d399"
R="#dc2626"; A="#f59e0b"; P="#a78bfa"
def label(s, size=28, color=TXT, width=12.5):
    m=Text(s, font="DejaVu Sans", font_size=size, color=color)
    if m.width>width: m.scale_to_fit_width(width)
    return m
class Companion(Scene):
    def heading(self,s):
        self.add(label(s,38).move_to([0,3.35,0]))
    def caption(self,s):
        if hasattr(self,"cap"): self.remove(self.cap)
        self.cap=label(s,25,width=12.7).move_to([0,-3.30,0])
        self.add(self.cap)
    def clear_scene(self):
        self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=.6)
    def construct(self):
        import hashlib
        def digest(previous,payload):return hashlib.sha256((previous+"|"+payload).encode()).hexdigest()
        genesis="0"*64
        payloads=["Alice pays Bob 5","Bob pays Chen 2","Chen pays Dana 1"]
        hashes=[];prev=genesis
        for text in payloads:hashes.append(digest(prev,text));prev=hashes[-1]
        self.heading("A HASH CHAIN: changing the past leaves evidence")
        self.caption("Teaching model: SHA-256 links three records. This is not Bitcoin's full block format.")
        boxes=[];texts=[];links=[]
        for i,x in enumerate([-4.5,0,4.5]):
            box=RoundedRectangle(width=3.8,height=3.5,corner_radius=.15,color=B).move_to([x,.3,0]);boxes.append(box)
            previous=genesis if i==0 else hashes[i-1]
            text=VGroup(label(f"Block {i+1}",28),label(payloads[i],22,width=3.4),label("prev: "+previous[:10],19,width=3.4),label("hash: "+hashes[i][:10],19,width=3.4)).arrange(DOWN,buff=.32).move_to(box)
            texts.append(text);self.play(FadeIn(box),FadeIn(text),run_time=.7)
            if i>0:
                link=Arrow(boxes[i-1].get_right(),box.get_left(),color=G,buff=.1);links.append(link)
                self.play(GrowArrow(link),run_time=.8)
            self.wait(2)
        self.add(label("Hash prefixes shown",19).move_to([0,-2.2,0]))
        self.wait(3)
        altered="Alice pays Bob 50";changed=digest(genesis,altered)
        t=texts[0];new_payload=label(altered,22,width=3.4).move_to(t[1]);new_hash=label("hash: "+changed[:10],19,color=R,width=3.4).move_to(t[3])
        self.caption("Alter one payment. Recomputing block 1 produces a different hash.")
        self.play(ReplacementTransform(t[1],new_payload),ReplacementTransform(t[3],new_hash),boxes[0].animate.set_color(R),run_time=1.5);self.wait(5)
        self.play(Indicate(texts[1][2],color=R),run_time=1.5)
        links[0].set_color(R);texts[1][2].set_color(R)
        self.add(label("Mismatch",23,color=R).move_to([-2.25,-1.85,0]))
        self.caption("Block 2 still points to the OLD hash. The link no longer matches.")
        self.wait(6)
        self.clear_scene();self.heading("DETECTION IS NOT CONSENSUS")
        phrases=["An attacker can recompute this toy chain.","Hashes expose changes; they do not make rewriting impossible.","Signatures check spending authority.","Consensus rules decide which valid history nodes accept."]
        for i,s in enumerate(phrases):
            self.play(FadeIn(label(s,28,color=A if i<2 else TXT).move_to([0,1.8-i*.95,0])),run_time=.7);self.wait(3)
        self.caption("In Bitcoin, proof of work makes a competing history costly; nodes still reject invalid spends.")
        self.wait(6)
