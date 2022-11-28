"""
YouTube Shorts version of Dissection Proof
"""
from kwanmath.interp import linterp
from manim import *
config.background_color='#e0e0ff'
config.pixel_width=1080
config.pixel_height=1920
actual_frame_height=config.frame_width*config.pixel_height/config.pixel_width
gold='#ffc000'
blue='#6060ff'
pixel_safe_x0=20
pixel_safe_y0=232
pixel_safe_w=892
pixel_safe_h=1585
pixel_safe_x1=pixel_safe_x0+pixel_safe_w
pixel_safe_y1=pixel_safe_y0+pixel_safe_h
frame_safe_x0=linterp(0,-config.frame_width/2,config.pixel_width,config.frame_width/2,pixel_safe_x0)
frame_safe_x1=linterp(0,-config.frame_width/2,config.pixel_width,config.frame_width/2,pixel_safe_x1)
frame_safe_y0=linterp(0,-actual_frame_height/2,config.pixel_height,actual_frame_height/2,pixel_safe_y0)
frame_safe_y1=linterp(0,-actual_frame_height/2,config.pixel_height,actual_frame_height/2,pixel_safe_y1)
frame_safe_xc=(frame_safe_x0+frame_safe_x1)/2
frame_safe_yc=(frame_safe_y0+frame_safe_y1)/2


class Quadratic1(Scene):
    def construct(self):
        GraphPoint=Point([frame_safe_x0,6,0])
        TextPoint=Point([frame_safe_x0,frame_safe_y0,0])
        MathPoint=Point([frame_safe_x0+1,7,0])
        #self.add(Polygon([frame_safe_x0,frame_safe_y0,0],
        #                 [frame_safe_x1, frame_safe_y0, 0],
        #                 [frame_safe_x1, frame_safe_y1, 0],
        #                 [frame_safe_x0, frame_safe_y1, 0],color='#ff00ff'
        #                 ))
        Title=Text("Quadratic Equation",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([frame_safe_xc,frame_safe_y1-0.5,0])
        self.add(Title)

        Text1=Text(r"""A projectile follows a
parabola. Its height is
determined from its
initial height,""",font_size=72,font='TeX Gyre Adventor',color=BLACK).next_to(TextPoint,UP+RIGHT)
        Math1=MathTex(r'{{ y(t)=y_0 }}{{ +v_0t }}{{-\frac{1}{2}gt^2}}',color=BLACK).scale(2).next_to(MathPoint,RIGHT)
        Text2=Text(r"""its initial vertical speed,""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint,UP+RIGHT)
        Text3=Text(r"""and the acceleration
of gravity.""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint,UP+RIGHT)
        Math3 = MathTex(r'y(t)=y_0+v_0t-\frac{1}{2}gt^2', color=BLACK).scale(2).next_to(MathPoint,DOWN+RIGHT)
        self.play(FadeIn(Text1),FadeIn(Math1[0]))
        self.pause()
        self.play(FadeOut(Text1),FadeIn(Text2),FadeIn(Math1[1]))
        self.pause()
        self.play(FadeOut(Text2),FadeIn(Text3),FadeIn(Math1[2]))

        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10],x_length=10,y_length=12,
            axis_config={"include_tip": False,'color':BLACK},
        ).next_to(GraphPoint,DOWN+RIGHT)

        t = ValueTracker(0)

        root0 = 0
        root1 = 10
        amp = 100
        xmax = (root0 + root1) / 2
        ymax = (xmax - root0) * (xmax - root1)
        k = amp/ymax

        def func(x):
            return k*(x-root0)*(x-root1)

        graph = ax.plot(func, color='#0000ff')

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point,color='#808080',radius=0.2)
        TlabelPoint=Point([0,1,0])
        YlabelPoint=Point([0,0,0])
        tlabel=MathTex("t=").set_color(BLACK).scale(1.5).next_to(TlabelPoint,DOWN+LEFT)
        tnumber=DecimalNumber().set_color(BLACK).scale(1.5).next_to(tlabel,RIGHT)
        tnumber.add_updater(lambda number: number.set_value(t.get_value()))
        ylabel=MathTex("y(t)=").set_color(BLACK).scale(1.5).next_to(YlabelPoint,DOWN+LEFT)
        ynumber=DecimalNumber().set_color(BLACK).scale(1.5).next_to(ylabel,RIGHT)
        ynumber.add_updater(lambda number: number.set_value(func(t.get_value())))

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2], 200)
        minimum_index = 199

        self.play(FadeOut(Text3),FadeIn(ax),FadeIn(graph),FadeIn(dot),FadeIn(tlabel),FadeIn(tnumber),FadeIn(ylabel),FadeIn(ynumber))
        self.play(t.animate.set_value(x_space[minimum_index]),rate_func=linear,run_time=3)
        self.wait()
        Text4a = Text(r"""In this form, you can
answer questions about""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        Text4b = Text(r"""where the object is 
given a time,""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        self.play(FadeIn(Text4a))
        self.wait()
        self.play(FadeOut(Text4a),FadeIn(Text4b))
        self.wait()
        Text5 = Text(r"""like where is it 3
seconds after launch.""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        self.play(FadeOut(Text4b),FadeIn(Text5),t.animate.set_value(3))
        self.play(Wiggle(tnumber))
        self.play(Wiggle(ynumber))
        self.wait()
        Text6 = Text(r"""To answer questions like
when the object""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        Text7 = Text(r"""reaches a given height,""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        self.play(FadeOut(Text5),FadeIn(Text6))
        self.wait()
        self.play(FadeOut(Text6),FadeIn(Text7))
        self.wait()
        Text8 = Text(r"""like when does it
reach 75 feet,""", font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        self.play(FadeOut(Text7),FadeIn(Text8),t.animate.set_value(7.5))
        self.play(Wiggle(ynumber))
        self.play(Wiggle(tnumber))
        Text9 = Text(r"""you have to solve the
equation for t.""", t2s={" t.":ITALIC}, font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint, UP + RIGHT)
        self.play(FadeOut(Text8),FadeIn(Text9))
        self.wait()
        Text10 = Text(r"""This isn't easy, and
requires a trick.""", t2s={" t.": ITALIC}, font_size=72, font='TeX Gyre Adventor', color=BLACK).next_to(TextPoint,
                                                                                                              UP + RIGHT)
        self.play(FadeOut(Text9), FadeIn(Text10))
        self.wait()
        self.play(FadeOut(Text10),FadeOut(tlabel),FadeOut(tnumber),FadeOut(ylabel),FadeOut(ynumber),FadeOut(graph),FadeOut(ax),FadeOut(dot),FadeOut(Math1))



class Quadratic2(Scene):
    def construct(self):
        TextPoint=Point([frame_safe_x0,6,0])
        MathPoint=Point([frame_safe_x0+1,4,0])
        if True:
            # Draw the rectangle around the safe area
            self.add(Polygon([frame_safe_x0,frame_safe_y0,0],
                             [frame_safe_x1, frame_safe_y0, 0],
                             [frame_safe_x1, frame_safe_y1, 0],
                             [frame_safe_x0, frame_safe_y1, 0],color='#ff00ff'
                             ))
        Title=Text("Completing the square",font_size=72,font='TeX Gyre Adventor',color=BLACK).move_to([frame_safe_xc,frame_safe_y1-0.5,0])
        self.add(Title)

        Text1=Text(r"""Last time we had an
equation like this:""",font_size=72,font='TeX Gyre Adventor',color=BLACK).next_to(TextPoint,UP+RIGHT)
        Math1=MathTex(r'{{ y(t) = y_0 +  v_0 t }} {{-}} {{\frac{1}{2}gt^2}}',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        self.play(FadeIn(Text1),FadeIn(Math1))
        self.pause()
        Text2=Text(r"""Let's get everything
on one side:""",font_size=72,font='TeX Gyre Adventor',color=BLACK).next_to(TextPoint,UP+RIGHT)
        Math2a=MathTex(r'{{\frac{1}{2}gt^2}} {{+}} {{y(t) =  y_0    +    v_0 t }} ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        Math2b=MathTex(r'{{\frac{1}{2}gt^2}} {{+     y(t) =  y_0}}{{+}}{{v_0 t}} ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        self.play(FadeOut(Text1),FadeIn(Text2),TransformMatchingTex(Math1,Math2a))
        self.remove(Math2a)
        self.add(Math2b)
        Math3a=MathTex(r'{{\frac{1}{2}gt^2}} {{-}} {{v_0 t}}{{ + y(t) =    y_0}}   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        Math3b=MathTex(r'{{\frac{1}{2}gt^2     -     v_0 t     + y(t)}} {{ = }}{{y_0}}   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        self.play(TransformMatchingTex(Math2b,Math3a))
        self.remove(Math3a)
        self.add(Math3b)
        Math4a=MathTex(r'{{\frac{1}{2}gt^2     -     v_0 t     + y(t)}}{{-}}{{y_0}}{{=}}{{0}}   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        Math4b=MathTex(r'{{\frac{1}{2}g}}{{t^2     }}{{-v_0}}{{t+}}{y(t)-y_0}}{{=0}}   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        self.play(TransformMatchingTex(Math3b,Math4a))
        self.remove(Math4a)
        self.add(Math4b)
        self.pause(2)
        Text3=Text(r"""And rename
the variables:""",font_size=72,font='TeX Gyre Adventor',color=BLACK).next_to(TextPoint,UP+RIGHT)
        Math5a=MathTex(r'{{a}}{{t^2     }}{{+b}}t + {{c}}{{=0}}   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        Math5b=MathTex(r'{{a}}{{t}}^2  +b{{t}} + c=0   ',color=BLACK).scale(1.8).next_to(MathPoint,RIGHT)
        self.play(FadeOut(Text2),FadeIn(Text3),TransformMatchingTex(Math4b,Math5a))
        self.pause()


def main():
    """
    Do the PictureBox part of the scene
    :return:
    """


if __name__=="__main__":
    main()