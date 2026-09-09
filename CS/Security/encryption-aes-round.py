"""Manim: one round of AES on real bytes, then the avalanche.
Uses encryption-aes.py (same folder) so every hex value shown is the true intermediate state, and
the final ciphertext matches the cryptography library.
Render: manim -qk encryption-aes-round.py AESRound ; copy the MP4 to encryption-aes-round.mp4 ; rm -rf media __pycache__"""
import importlib.util, os
spec = importlib.util.spec_from_file_location("aes", os.path.join(os.path.dirname(os.path.abspath(__file__)), "encryption-aes.py"))
aes = importlib.util.module_from_spec(spec); spec.loader.exec_module(aes)
from manim import *
GREY="#888888"; BLUE_K="#2563eb"; GREEN_K="#059669"; RED_K="#dc2626"; AMBER="#f59e0b"; PURPLE_K="#7c3aed"

KEY = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c"); PT = b"Attack at dawn!!"
TR = []; CT = aes.encrypt_block(PT, KEY, TR)
PT2 = bytes([PT[0] ^ 1]) + PT[1:]; CT2 = aes.encrypt_block(PT2, KEY)

def grid(state, color=GREY, cell=0.62):
    """4x4 grid, column-major like the AES state: cell (row r, col c) holds state[4c + r]."""
    g = VGroup()
    for c in range(4):
        for r in range(4):
            sq = Square(side_length=cell, stroke_color=GREY, stroke_width=1.2).move_to([c*cell, -r*cell, 0])
            t = Text(f"{state[4*c+r]:02x}", font_size=24, color=color).move_to(sq)
            g.add(VGroup(sq, t))
    return g.move_to(ORIGIN)

class AESRound(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("AES-128: one round on a 16-byte block, with the real numbers", font_size=30, color=GREY).to_edge(UP)
        self.add(title)
        cap = Text("plaintext  'Attack at dawn!!'  laid out as a 4×4 grid of bytes (down the columns)", font_size=22, color=GREY).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(cap))
        g = grid(list(PT), GREEN_K).shift(DOWN*0.4); self.play(FadeIn(g)); self.wait(1)
        def step(name, state, color, note):
            nonlocal g
            ng = grid(state, color).move_to(g)
            lab = Text(name, font_size=30, color=color).next_to(ng, LEFT, buff=0.9)
            nt = Text(note, font_size=20, color=GREY).to_edge(DOWN, buff=0.6)
            self.play(FadeIn(lab)); self.play(Transform(g, ng), FadeIn(nt), run_time=1.2); self.wait(1.4); self.play(FadeOut(lab), FadeOut(nt))
        step("AddRoundKey", TR[0][1], AMBER, "XOR every byte with the round key — the only step where the secret enters")
        step("SubBytes", TR[1][1], PURPLE_K, "replace every byte by its entry in a fixed 256-entry table (the S-box): confusion — a non-linear scramble")
        # shift rows: animate the rotation
        sr = grid(TR[2][1], BLUE_K).move_to(g); lab = Text("ShiftRows", font_size=30, color=BLUE_K).next_to(sr, LEFT, buff=0.9)
        nt = Text("row r rotates left by r places: bytes leave their column — the start of diffusion", font_size=20, color=GREY).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(lab), FadeIn(nt))
        for r in range(1, 4):
            cells = [g[4*c + r] for c in range(4)]; self.play(*[cells[c].animate.move_to(sr[4*((c - r) % 4) + r]) for c in range(4)], run_time=0.9)
        self.play(Transform(g, sr), run_time=0.3); self.wait(1.2); self.play(FadeOut(lab), FadeOut(nt))
        step("MixColumns", TR[3][1], RED_K, "each column becomes a mix of all four of its bytes (GF(2⁸) arithmetic): every output byte depends on four inputs")
        step("AddRoundKey", TR[4][1], AMBER, "round key 1 (derived from the secret key) — one round done; after two more, every bit depends on every bit")
        dots = Text("… rounds 2 to 10 …", font_size=26, color=GREY).next_to(g, DOWN, buff=0.5); self.play(FadeIn(dots)); self.wait(0.8)
        fin = grid(list(CT), RED_K).move_to(g); lab = Text("ciphertext", font_size=30, color=RED_K).next_to(fin, LEFT, buff=0.9)
        self.play(Transform(g, fin), FadeIn(lab), FadeOut(dots)); nt = Text("01a5003c…e88df3 — byte for byte what the cryptography library returns", font_size=20, color=GREY).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(nt)); self.wait(2); self.play(FadeOut(nt), FadeOut(lab), FadeOut(cap))
        # avalanche
        self.play(g.animate.shift(LEFT*3.2))
        cap2 = Text("the avalanche: flip ONE bit of the plaintext ('A' → '@') and encrypt again", font_size=22, color=GREY).next_to(title, DOWN, buff=0.3); self.play(FadeIn(cap2))
        g2 = grid(list(CT2), RED_K).move_to(g).shift(RIGHT*6.4)
        # colour cells that changed
        for i in range(16):
            if CT[i] != CT2[i]: g2[i][1].set_color(AMBER)
        self.play(FadeIn(g2)); diff = sum(bin(a ^ b).count("1") for a, b in zip(CT, CT2))
        nt2 = Text(f"{diff} of 128 ciphertext bits changed — about half, as a good cipher must; nothing in the output says the inputs were close", font_size=20, color=GREY).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(nt2)); self.wait(3)
