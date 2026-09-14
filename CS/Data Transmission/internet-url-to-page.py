"""From URL to page, animated: the DNS lookup, the connection, the request, the cookie.

The browser has a name and needs a number. It asks its resolver; the resolver, if it
does not remember, asks the root, then the .com servers, then the site's own name
server; the answer comes back and is cached. Then TCP, then HTTPS, then GET /, then
HTML plus a Set-Cookie header — and on the next visit the cookie goes back with the request.

Render:  manim -qk internet-url-to-page.py UrlToPage
"""
from manim import *
import numpy as np
GREY_K="#888888"; BLUE_K="#2563eb"; PURPLE_K="#7c3aed"; GREEN_K="#059669"; RED_K="#dc2626"; AMBER_K="#f59e0b"; TEAL_K="#0891b2"

def box(label, sub, pos, color, w=2.2, h=0.9):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color, stroke_width=2, fill_color=color, fill_opacity=0.12).move_to(pos)
    t = Text(label, font_size=22, color=color).move_to(pos + UP*0.18)
    s = Text(sub, font_size=15, color=GREY_K).move_to(pos + DOWN*0.22)
    return VGroup(r, t, s)

class UrlToPage(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("From URL to page: the browser has a name and needs a number", font_size=28, color=GREY_K).to_edge(UP)
        self.add(title)
        browser = box("browser", "your laptop", LEFT*4.7 + DOWN*0.4, BLUE_K)
        resolver = box("DNS resolver", "your ISP, or 223.5.5.5", LEFT*1.6 + DOWN*0.4, TEAL_K, w=2.6)
        root = box("root server", "'.'  -> ask .com", RIGHT*2.6 + UP*1.6, PURPLE_K)
        tld = box(".com server", "-> ask bilibili's", RIGHT*2.6 + DOWN*0.4, PURPLE_K)
        auth = box("authoritative", "bilibili.com's own", RIGHT*2.6 + DOWN*2.4, PURPLE_K)
        web = box("web server", "119.84.174.66", RIGHT*5.2 + DOWN*0.4, GREEN_K)
        url = Text("https://www.bilibili.com/", font_size=20, color=BLUE_K).next_to(browser, UP, buff=0.35).shift(RIGHT*0.7)
        self.play(FadeIn(browser), FadeIn(url), FadeIn(resolver), FadeIn(root), FadeIn(tld), FadeIn(auth))
        cap = Text("1. DNS: 'what is the IP address of www.bilibili.com?'", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap))
        def packet(txt, color, a, b, rt=1.8, hold=0.5):
            p = VGroup(RoundedRectangle(width=2.1, height=0.46, corner_radius=0.08, color=color, fill_color=color, fill_opacity=0.25, stroke_width=1.5), Text(txt, font_size=15, color=color)).move_to(a)
            self.play(FadeIn(p, run_time=0.25)); self.play(p.animate.move_to(b), run_time=rt, rate_func=smooth); self.wait(hold); self.play(FadeOut(p, run_time=0.25))
        packet("www.bilibili.com?", BLUE_K, browser.get_right(), resolver.get_left())
        climb = Text("the resolver does not know: it climbs the hierarchy", font_size=17, color=GREY_K).next_to(resolver, DOWN, buff=0.15); self.play(FadeIn(climb)); self.wait(0.6)
        packet("bilibili.com?", TEAL_K, resolver.get_right(), root.get_left())
        packet(".com is at ...", PURPLE_K, root.get_left(), resolver.get_right())
        packet("bilibili.com?", TEAL_K, resolver.get_right(), tld.get_left())
        packet("its name server is ...", PURPLE_K, tld.get_left(), resolver.get_right())
        packet("www.bilibili.com?", TEAL_K, resolver.get_right(), auth.get_left())
        packet("119.84.174.66", GREEN_K, auth.get_left(), resolver.get_right())
        cache = Text("cached for 41 s", font_size=15, color=AMBER_K).next_to(resolver, DOWN, buff=0.12); self.play(FadeOut(climb)); self.play(FadeIn(cache)); self.wait(0.6)
        packet("119.84.174.66", GREEN_K, resolver.get_left(), browser.get_right())
        ip = Text("119.84.174.66", font_size=20, color=GREEN_K).next_to(url, DOWN, buff=0.1); self.play(FadeIn(ip)); self.wait(0.5)
        cap2 = Text("2. TCP connects, TLS proves the server's name — the padlock — then HTTP asks for the page", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap2), FadeOut(root), FadeOut(tld), FadeOut(auth), FadeOut(resolver), FadeOut(cache))
        self.play(FadeIn(web))
        line = Line(browser.get_right(), web.get_left(), color=GREY_K, stroke_width=1.5); self.play(Create(line))
        packet("SYN / SYN-ACK / ACK", GREY_K, browser.get_right(), web.get_left())
        packet("TLS: certificate", GREEN_K, web.get_left(), browser.get_right())
        lock = Text("padlock", font_size=15, color=GREEN_K).next_to(browser, DOWN, buff=0.12); self.play(FadeIn(lock))
        packet("GET / HTTP/1.1", BLUE_K, browser.get_right(), web.get_left())
        packet("200 OK + HTML", GREEN_K, web.get_left(), browser.get_right())
        packet("Set-Cookie: session=...", AMBER_K, web.get_left(), browser.get_right())
        cookie = Text("cookie stored", font_size=15, color=AMBER_K).next_to(lock, DOWN, buff=0.08); self.play(FadeIn(cookie))
        page = Text("HTML rendered: the page appears", font_size=18, color=BLUE_K).next_to(browser, UP, buff=0.35).shift(RIGHT*0.9)
        self.play(FadeOut(url), FadeOut(ip), FadeIn(page)); self.wait(0.6)
        cap3 = Text("3. next visit: the browser sends the cookie back, and the site remembers you", font_size=22, color=GREY_K).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap3))
        packet("GET /  Cookie: session=...", AMBER_K, browser.get_right(), web.get_left())
        packet("200 OK: 'welcome back'", GREEN_K, web.get_left(), browser.get_right())
        self.wait(2.0)
