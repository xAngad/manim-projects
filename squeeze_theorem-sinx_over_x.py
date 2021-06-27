from manim import *
import math

class squeezeTheorem(GraphScene):
    def setup(self):
        GraphScene.setup(self)
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-2,
            x_max=2,
            x_axis_width=6,
            x_axis_label="",
            x_axis_config={"tick_frequency": 0.5},
            x_axis_visibility=True,
            y_min=-1,
            y_max=2,
            y_axis_height=6,
            y_axis_label="",
            y_bottom_tick=-1,
            y_axis_config={"tick_frequency": 1},
            y_axis_visibility=True,
            **kwargs 
        )
    
    def construct(self):
        self.eqDefine()
        self.explanations()

    def eqDefine(self):
        """ setting up axes + defining equation for curves """
        #axes
        self.setup_axes(animate=False)
        self.axes.move_to(ORIGIN)

        #equations
        fx = lambda x : math.cos(x)
        gx = lambda x : x/np.sin(x)
        hx = lambda x : 1/math.cos(x)

        fx_graph = self.get_graph(fx, color=GREEN)
        gx_graph = self.get_graph(gx, discontinuities=[ inverse_interpolate(self.x_min, self.x_max, 0)], color=RED)
        # gx_graph2 = self.get_graph(gx_2, x_min=0.01, color=GREEN)
        hx_graph = self.get_graph(hx, x_min=-1.2, x_max=1.2, color=BLUE)

        self.play(Write(self.axes))
        self.play(Write(fx_graph))
        self.play(Write(gx_graph))
        self.play(Write(hx_graph))

        graphs_group = VGroup(self.axes, fx_graph, gx_graph, hx_graph)
        self.play(graphs_group.animate.to_edge(LEFT))
    
    def explanations(self):
        fx_eq = MathTex("f(x)", "=\\cos(x)").set_color(GREEN).move_to(RIGHT*3+DOWN*1.5)
        gx_eq = MathTex("g(x)", "=\\dfrac{x}{\\sin(x)}").set_color(RED).move_to(RIGHT*3)
        hx_eq = MathTex("h(x)", "=\\dfrac{1}{\\cos(x)}").set_color(BLUE).move_to(RIGHT*3+UP*1.5)

        self.play(Write(fx_eq), Write(gx_eq), Write(hx_eq))
        self.wait(1.5)

        leq_1 = MathTex("f(x)", "\\leq", "g(x)", "\\leq", "h(x)").move_to(RIGHT*3)
        leq_1[0].set_color(GREEN)
        leq_1[2].set_color(RED)
        leq_1[4].set_color(BLUE)

        self.play(ReplacementTransform(fx_eq[0], leq_1[0]),
                ReplacementTransform(gx_eq[0], leq_1[2]),
                ReplacementTransform(hx_eq[0], leq_1[4]),
                FadeOut(fx_eq[1:]), FadeOut(gx_eq[1:]), FadeOut(hx_eq[1:]))
        self.play(Write(leq_1[1]), Write(leq_1[3]))
        self.wait(1.5)
        
        leq_2 = MathTex("\\cos(x)", "\\leq", "\\dfrac{x}{\\sin(x)}", "\\leq", "\\dfrac{1}{\\cos(x)}").move_to(RIGHT*3)
        leq_2[0].set_color(GREEN)
        leq_2[2].set_color(RED)
        leq_2[4].set_color(BLUE)

        self.play(ReplacementTransform(leq_1[0:], leq_2[0:]))
        self.wait(1.5)

        self.play(leq_2.animate.to_edge(UP))

        acc_sq = MathTex("\\text{According to the squeeze theorem: }").scale(0.75).move_to(RIGHT*3+UP*1.2)
        sq_1 = MathTex("\\text{If }", "f(x)", "\\leq", "g(x)", "\\leq", "h(x)").scale(0.75).move_to(RIGHT*3+UP*0.4)
        sq_1[1].set_color(GREEN)
        sq_1[3].set_color(RED)
        sq_1[5].set_color(BLUE)
        
        sq_2 = MathTex("\\text{and }", "\\lim\\limits_{x\\to a}", "f(x)", "=", "\\lim\\limits_{x\\to a}", "h(x)", "=", "L").scale(0.75).move_to(RIGHT*3+DOWN*0.4)
        sq_2[2].set_color(GREEN)
        sq_2[5].set_color(BLUE)
        sq_2[7].set_color(GOLD_E)

        sq_3 = MathTex("\\text{then }", "\\lim\\limits_{x\\to a}", "g(x)", "=", "L").scale(0.75).move_to(RIGHT*3+DOWN*1.2)
        sq_3[2].set_color(RED)
        sq_3[4].set_color(GOLD_E)

        self.play(Write(acc_sq))
        self.play(Write(sq_1))
        self.wait(0.5)
        self.play(Write(sq_2))
        self.wait(0.5)
        self.play(Write(sq_3))

        sq_group = VGroup(sq_1, sq_2, sq_3)
        sq_frame = SurroundingRectangle(sq_group, stroke_color=WHITE)
        self.play(Write(sq_frame))
        self.wait(2.5)

        self.play(FadeOut(sq_group), FadeOut(sq_frame), FadeOut(acc_sq))

        self.play(leq_2.animate.move_to(RIGHT*3))
        self.wait()

        leq_3 = MathTex("\\lim\\limits_{x\\to 0}", "\\cos(x)", "\\leq",
                    "\\lim\\limits_{x\\to 0}", "\\dfrac{x}{\\sin(x)}", "\\leq",
                    "\\lim\\limits_{x\\to 0}", "\\dfrac{1}{\\cos(x)}").scale(0.75).move_to(RIGHT*3)
        leq_3[1].set_color(GREEN)
        leq_3[4].set_color(RED)
        leq_3[7].set_color(BLUE)

        self.play(ReplacementTransform(leq_2[0], leq_3[1]),
                ReplacementTransform(leq_2[1], leq_3[2]),
                ReplacementTransform(leq_2[2], leq_3[4]),
                ReplacementTransform(leq_2[3], leq_3[5]),
                ReplacementTransform(leq_2[4], leq_3[7]))
        self.play(Write(leq_3[0]), Write(leq_3[3]), Write(leq_3[6]))
        self.wait(1.5)

        leq_4 = MathTex("1", "\\leq",
                    "\\lim\\limits_{x\\to 0}", "\\dfrac{x}{\\sin(x)}", "\\leq",
                    "1").scale(0.75).move_to(RIGHT*3)
        leq_4[3].set_color(RED)
        leq_4[0].set_color(GOLD_E)
        leq_4[5].set_color(GOLD_E)

        self.play(ReplacementTransform(leq_3[0:2], leq_4[0]),
                ReplacementTransform(leq_3[2], leq_4[1]),
                ReplacementTransform(leq_3[3], leq_4[2]),
                ReplacementTransform(leq_3[4], leq_4[3]),
                ReplacementTransform(leq_3[5], leq_4[4]),
                ReplacementTransform(leq_3[6:], leq_4[5]))
        self.wait(1.5)
