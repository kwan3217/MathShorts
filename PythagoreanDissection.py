"""
YouTube Shorts version of Dissection Proof
"""

from manim import *
config.background_color='#e0e0ff'
config.pixel_width=1080
config.pixel_height=1920
gold='#ffc000'
blue='#6060ff'


class RightTriangle(Polygon):
    """
    Make a right triangle with the right angle at the origin.
    Triangle will be in quadrant I (upper right) with vertical
    leg a and horizontal leg b
    """
    def __init__(self,a:float=3.0,b:float=4.0,*args,**kwargs):
        super().__init__([0,0,0],[b,0,0],[0,a,0],*args,**kwargs)
        self.a=a
        self.b=b


class BSquare(Polygon):
    def __init__(self,a:float=3.0,b:float=4.0,*args,**kwargs):
        r=(a+b)/2
        super().__init__([r-b,-r, 0], [r,-r, 0], [r, -r+b, 0],[r-b,-r+b,0], *args, **kwargs)
        self.a=a
        self.b=b


class ASquare(Polygon):
    def __init__(self,a:float=3.0,b:float=4.0,*args,**kwargs):
        r=(a+b)/2
        super().__init__([-r,r-a, 0], [-r+a,r-a, 0], [-r+a, r, 0],[-r,r,0], *args, **kwargs)
        self.a=a
        self.b=b


class DiagSquare(Polygon):
    """
    Make a polygon that fills in the square between the four rotated triangles.
    The triangles have vertical leg a and horizontal leg b
    """
    def __init__(self,a:float=3.0,b:float=4.0,*args,**kwargs):
        super().__init__([-(a+b)/2,-(b-a)/2,0],[(b-a)/2,-(b+a)/2,0],[(b+a)/2,(b-a)/2,0],[-(b-a)/2,(b+a)/2,0],*args,**kwargs)
        self.a=a
        self.b=b


class CreateCircle(Scene):
    def construct(self):
        Title=Text("Pythagorean Theorem",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,12,0])
        self.play(FadeIn(Title))
        RT1a=RightTriangle(a=3, b=4, color=BLACK).shift([-2,-1.5,0]).set_fill(gold, 1.0)
        Text1=Text("Consider a right triangle",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,-5,0])
        self.play(FadeIn(Text1),
                  Create(RT1a))
        self.pause()
        self.play(FadeOut(Text1))
        Text2=Text(r"""The sides around the right
angle have length a and b""",font_size=72,font='TeX Gyre Adventor',t2s={' a ':ITALIC,' b':ITALIC},color=BLACK).move_to([0,-5,0])
        self.play(FadeIn(Text2))
        a=MathTex("a",color=BLACK).scale(2).next_to(RT1a,LEFT)
        b=MathTex("b",color=BLACK).scale(2).next_to(RT1a,DOWN)
        self.play(FadeIn(a),FadeIn(b))
        self.pause()
        self.play(FadeOut(Text2))
        Text3=Text(r"""What is the length of
the third side c?""",font_size=72,font='TeX Gyre Adventor',t2s={' c':ITALIC},color=BLACK).move_to([0,-5,0])
        self.play(FadeIn(Text3))
        c=MathTex("c",color=BLACK).scale(2).move_to((RIGHT+UP)*0.4)
        self.play(FadeIn(c))
        self.pause()
        self.play(FadeOut(a),FadeOut(b),FadeOut(c),FadeOut(Text3))
        Text4=Text(r"""Make three copies of the
triangle, and arrange the
four triangles around
a square""",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,-5,0])
        self.play(RT1a.animate.move_to([-1.5,-2,0]),FadeIn(Text4))
        RT2a=RT1a.copy()
        self.play(Rotate(RT2a,PI/2,about_point=ORIGIN))
        RT3a=RT2a.copy()
        self.play(Rotate(RT3a,PI/2,about_point=ORIGIN))
        RT4a=RT3a.copy()
        self.play(Rotate(RT4a,PI/2,about_point=ORIGIN))
        c2a=DiagSquare(a=3,b=4,color=BLACK).set_fill(blue,1.0)
        self.play(FadeIn(c2a))
        self.play(FadeOut(Text4))
        Text5=Text(r"""Pause and ponder:
All four sides of the
square have length c.
Are all 4 angles 90°?
Can you prove it?""",font_size=72,font='TeX Gyre Adventor',t2s={' c':ITALIC},color=BLACK).move_to([0,-5,0])
        self.play(FadeIn(Text5))
        self.pause(2)
        self.play(FadeOut(Text5))
        Text6=Text(r"""The area of the blue
square is c².""",font_size=72,font='TeX Gyre Adventor',t2s={' c':ITALIC},color=BLACK).move_to([0,-5,0])
        c2label=MathTex("c^2").scale(2).set_z_index(10)
        self.play(FadeIn(Text6))
        self.play(FadeIn(c2label))
        self.pause(2)
        self.play(FadeOut(Text6))
        RT1b=RT1a.copy()
        RT2b=RT2a.copy()
        RT3b=RT3a.copy()
        RT4b=RT4a.copy()
        c2b=c2a.copy()
        Text7=Text(r"""Make a copy of the whole
figure, and set it aside.""",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,-9,0])
        self.play(RT1a.animate.shift(UP*4.5),RT2a.animate.shift(UP*4.5),RT3a.animate.shift(UP*4.5),RT4a.animate.shift(UP*4.5),
                  c2a.animate.shift(UP*4.5),c2label.animate.shift(UP*4.5),
                  RT1b.animate.shift(DOWN*4.5),RT2b.animate.shift(DOWN*4.5),RT3b.animate.shift(DOWN*4.5),RT4b.animate.shift(DOWN*4.5),
                  c2b.animate.shift(DOWN*4.5),FadeIn(Text7))
        RT1ah=RightTriangle(a=1,b=6,color=BLACK).set_fill(gold,1.0).shift([-3.5,-3.5,0]).shift(UP*4.5)
        RT2ah=RT1ah.copy().rotate(PI/2,about_point=UP*4.5)
        RT3ah=RT2ah.copy().rotate(PI/2,about_point=UP*4.5)
        RT4ah=RT3ah.copy().rotate(PI/2,about_point=UP*4.5)
        c2ah=DiagSquare(a=1,b=6,color=BLACK).set_fill(blue,1.0).shift(UP*4.5)
        RT1av=RightTriangle(a=6,b=1,color=BLACK).set_fill(gold,1.0).shift([-3.5,-3.5,0]).shift(UP*4.5)
        RT2av=RT1av.copy().rotate(PI/2,about_point=UP*4.5)
        RT3av=RT2av.copy().rotate(PI/2,about_point=UP*4.5)
        RT4av=RT3av.copy().rotate(PI/2,about_point=UP*4.5)
        c2av=DiagSquare(a=6,b=1,color=BLACK).set_fill(blue,1.0).shift(UP*4.5)
        self.pause()
        self.play(FadeOut(Text7))
        Text8=Text(r"""Slide the triangles to
form squares with sides
a and b""",font_size=72,t2s={'a ':ITALIC,' b':ITALIC},font='TeX Gyre Adventor',color=BLACK).move_to([0,-9,0])
        self.play(FadeIn(Text8))
        self.remove(c2b)
        background=Polygon([-3.5,-3.5,0],[3.5,-3.5,0],[ 3.5, 3.5,0],[-3.5, 3.5,0],color=BLACK).set_fill(blue,1.0).shift(DOWN*4.5)
        self.add(background)
        self.bring_to_back(background)
        self.play(RT1b.animate.shift([3,4,0]))
        self.play(RT2b.animate.shift([-4,0,0]),
                  RT4b.animate.shift([0,-3,0]))
        b2=BSquare(a=3,b=4,color=BLACK).set_fill(GREEN,1.0).shift(DOWN*4.5)
        a2=ASquare(a=3,b=4,color=BLACK).set_fill(RED,1.0).shift(DOWN*4.5)
        a=1
        b=6
        RT1bh=RightTriangle(a=a,b=b,color=BLACK).set_fill(gold,1.0).shift([-3.5,-3.5,0]).shift(DOWN*4.5).shift([a,b,0])
        RT2bh=RT1bh.copy().shift([-a,-b,0]).rotate(  PI/2,about_point=DOWN*4.5).shift([-b,0,0])
        RT3bh=RT1bh.copy().shift([-a,-b,0]).rotate(2*PI/2,about_point=DOWN*4.5)
        RT4bh=RT1bh.copy().shift([-a,-b,0]).rotate(3*PI/2,about_point=DOWN*4.5).shift([0,-a,0])
        b2h=BSquare(a=a,b=b,color=BLACK).set_fill(GREEN,1.0).shift(DOWN*4.5)
        a2h=ASquare(a=a,b=b,color=BLACK).set_fill(RED,1.0).shift(DOWN*4.5)
        a=6
        b=1
        RT1bv=RightTriangle(a=a,b=b,color=BLACK).set_fill(gold,1.0).shift([-3.5,-3.5,0]).shift(DOWN*4.5).shift([a,b,0])
        RT2bv=RT1bv.copy().shift([-a,-b,0]).rotate(  PI/2,about_point=DOWN*4.5).shift([-b,0,0])
        RT3bv=RT1bv.copy().shift([-a,-b,0]).rotate(2*PI/2,about_point=DOWN*4.5)
        RT4bv=RT1bv.copy().shift([-a,-b,0]).rotate(3*PI/2,about_point=DOWN*4.5).shift([0,-a,0])
        b2v=BSquare(a=a,b=b,color=BLACK).set_fill(GREEN,1.0).shift(DOWN*4.5)
        a2v=ASquare(a=a,b=b,color=BLACK).set_fill(RED,1.0).shift(DOWN*4.5)
        a2label=MathTex("a^2").scale(2).move_to([-2,2,0]).shift(DOWN*4.5).set_z_index(11)
        b2label=MathTex("b^2").scale(2).move_to([1.5,-1.5,0]).shift(DOWN*4.5).set_z_index(12)
        self.play(FadeIn(b2),FadeIn(a2),FadeIn(a2label),FadeIn(b2label))
        self.remove(background)
        self.play(FadeOut(Text8))
        Text9=Text(r"""If we get rid of the
triangles, the area left
in both figures is the same""",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,-9,0])
        self.play(FadeOut(RT1a),FadeOut(RT2a),FadeOut(RT3a),FadeOut(RT4a),
                  FadeOut(RT1b),FadeOut(RT2b),FadeOut(RT3b),FadeOut(RT4b),
                  FadeIn(Text9))
        self.pause(2)
        Text10=Text("Therefore,",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([0,-9,0])
        Math10=MathTex("{{a^2}}+{{b^2}}={{c^2}}",color=BLACK).scale(2).next_to(Text10,DOWN).set_color_by_tex("a^2",RED).set_color_by_tex("b^2",GREEN).set_color_by_tex("c^2",blue)
        self.play(FadeOut(Text9))
        self.play(FadeIn(Text10),FadeIn(Math10))
        self.pause(3)
        self.play(FadeOut(Text10),FadeOut(Math10))
        Text11 = Text(r"""Note that it doesn't
matter what shape or size
the right triangles are.
The squares in the figures
are still equal.""", font_size=72, font='TeX Gyre Adventor', color=BLACK).move_to([0, -9, 0])
        self.play(FadeIn(RT1a),FadeIn(RT2a),FadeIn(RT3a),FadeIn(RT4a),
                  FadeIn(RT1b),FadeIn(RT2b),FadeIn(RT3b),FadeIn(RT4b),
                  FadeIn(Text11))
        self.remove(RT1a,RT2a,RT3a,RT4a,RT1b,RT2b,RT3b,RT4b,c2a,a2,b2)
        self.play(ReplacementTransform(RT1a.copy(),RT1ah),
                  ReplacementTransform(RT2a.copy(),RT2ah),
                  ReplacementTransform(RT3a.copy(),RT3ah),
                  ReplacementTransform(RT4a.copy(),RT4ah),
                  ReplacementTransform(RT1b.copy(), RT1bh),
                  ReplacementTransform(RT2b.copy(), RT2bh),
                  ReplacementTransform(RT3b.copy(), RT3bh),
                  ReplacementTransform(RT4b.copy(), RT4bh),
                  a2label.animate.shift([-1, 1,0]),
                  b2label.animate.shift([-1, 1,0]),
                  ReplacementTransform(c2a.copy(),c2ah),
                  ReplacementTransform(a2.copy(),a2h),
                  ReplacementTransform(b2.copy(),b2h)
                  )
        self.play(ReplacementTransform(RT1ah,RT1av),
                  ReplacementTransform(RT2ah,RT2av),
                  ReplacementTransform(RT3ah,RT3av),
                  ReplacementTransform(RT4ah,RT4av),
                  ReplacementTransform(RT1bh,RT1bv),
                  ReplacementTransform(RT2bh,RT2bv),
                  ReplacementTransform(RT3bh,RT3bv),
                  ReplacementTransform(RT4bh,RT4bv),
                  a2label.animate.shift([2.5,-2.5,0]),
                  b2label.animate.shift([2.5,-2.5,0]),
                  ReplacementTransform(c2ah,c2av),
                  ReplacementTransform(a2h,a2v),
                  ReplacementTransform(b2h,b2v)
                  )
        self.play(ReplacementTransform(RT1av,RT1a),
                  ReplacementTransform(RT2av,RT2a),
                  ReplacementTransform(RT3av,RT3a),
                  ReplacementTransform(RT4av,RT4a),
                  ReplacementTransform(RT1bv,RT1b),
                  ReplacementTransform(RT2bv,RT2b),
                  ReplacementTransform(RT3bv,RT3b),
                  ReplacementTransform(RT4bv,RT4b),
                  a2label.animate.shift([-1.5,1.5,0]),
                  b2label.animate.shift([-1.5,1.5,0]),
                  ReplacementTransform(c2av,c2a),
                  ReplacementTransform(a2v,a2),
                  ReplacementTransform(b2v,b2)
                  )



def main():
    import manimpango
    manimpango.list_fonts()

if __name__=="__main__":
    main()