from manim import *
import math
from scipy.integrate import quad

class instagramPromo(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=8.5,
            x_axis_width=6,
            y_min=0,
            y_max=5,
            y_axis_height=6,
            **kwargs
        )
    
    def construct(self):
        self.setup_axes(animate=False)
        self.axes.move_to(ORIGIN)

        eq = lambda x: -0.05 * x ** 3 + 0.5 * x ** 2 - x + 3

        graf = self.get_graph(eq, color=RED, x_max=8)
        self.add(self.axes)
        self.play(Write(graf), run_time=1)

        b = ValueTracker(1)

        tangent = always_redraw(
            lambda : self.get_secant_slope_group(b.get_value(), graf, dx=0.01, secant_line_color=BLUE, secant_line_length=4)
        )
        tangent_dot = always_redraw(
            lambda : Dot(self.coords_to_point(b.get_value(), eq(b.get_value())))
        )

        a = ValueTracker(0)
        

        area = always_redraw(
            lambda : self.get_area(graf, t_min=a.get_value(), t_max=b.get_value(), dx_scaling=0.5, area_color=PINK)
        )

        a_dot = always_redraw(
            lambda : Dot(self.coords_to_point(a.get_value(), eq(a.get_value())))
        )

        slope_label = MathTex("\\text{Slope: }").scale(0.75).move_to(UP*2.25+LEFT*2.25)
        slope_val = always_redraw(
            lambda : MathTex(round(self.slope_of_tangent(b.get_value(), graf), 2)).scale(0.75).next_to(slope_label, RIGHT)
        )

        area_label = MathTex("\\text{Area: }").scale(0.75).move_to(UP*1.75+LEFT*2.25)
        area_val = always_redraw(
            lambda : MathTex(round(quad(eq, a.get_value(), b.get_value())[0], 2)).scale(0.75).next_to(area_label)
        )

        self.play(Write(a_dot), Write(tangent), Write(tangent_dot), run_time=1)
        self.play(Write(area), run_time=1)
        self.play(Write(slope_label), Write(slope_val), Write(area_label), Write(area_val))
        self.play(b.animate.set_value(6), run_time=1.5, rate_func=smooth)
        self.wait()

        



