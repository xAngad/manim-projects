""" ManimCE """

from manim import *
import numpy as np

class cubicRootShifting(GraphScene):
    def setup(self):
        GraphScene.setup(self)
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            graph_origin=ORIGIN,
            x_min=-10,
            x_max=10,
            y_min=-5,
            y_max=5,
            x_axis_label="",
            y_axis_label="",
            x_axis_config={"tick_frequency": 1},
            y_axis_config={"tick_frequency": 1},
            # y_labeled_nums=[-15, 15],
            # x_labeled_nums=[-5,5],
            **kwargs
        )
    
    def construct(self):
        """ x and y axis """
        self.setup_axes(animate=False)
        self.play(Write(self.axes))
        
        """ Setup values of coefficients and roots """
        a = ValueTracker(1)
        b = ValueTracker(0)
        alpha = ValueTracker(-2)
        beta = ValueTracker(-1)
        gamma = ValueTracker(1)

        
        """ Equation of cubic polynomial """
        def eq1(x):
            return ((a.get_value()*(x-b.get_value()) - alpha.get_value())*(a.get_value()*(x-b.get_value()) - beta.get_value())*(a.get_value()*(x-b.get_value()) - gamma.get_value()))

        
        """ Graph functions """
        graf1 = always_redraw(
            lambda : self.get_graph(eq1, color=RED)
        )
        graf2 = self.get_graph(
                lambda x : ((np.cbrt(x) - alpha.get_value())*(np.cbrt(x) - beta.get_value())*(np.cbrt(x) - gamma.get_value())), color=RED
        )

        self.play(FadeIn(graf1))
        

        graph_grp = VGroup(self.axes, graf1)
        self.play(graph_grp.animate.scale(0.75, about_point=ORIGIN), run_time=1)
        self.play(graph_grp.animate.to_edge(LEFT), run_time=1)

        """ Texts #1 """
        fx_1 = MathTex("f", "(", "x", ")", "=",
                    "p", "{x", "^3}",
                    "+",
                    "q", "{x", "^2}",
                    "+",
                    "r", "x",
                    "+",
                    "s").scale(0.75).shift(RIGHT*3.5+UP*0.5)
        fx_1[0:4].set_color(RED)
        
        fx_shifted = MathTex("f", "(", "a", "(", "x", "-", "b", ")", ")", "=",
                    "p", "(", "{a", "(", "x", "-", "b", ")", ")", "^3}",
                    "+",
                    "q", "(", "{a", "(", "x", "-", "b", ")", ")", "^2}",
                    "+",
                    "r", "(", "a", "(", "x", "-", "b", ")", ")",
                    "+",
                    "s").scale(0.5).to_edge(RIGHT).shift(DOWN*0.5)
        fx_shifted[0:2].set_color(RED)
        fx_shifted[4].set_color(RED)
        fx_shifted[8].set_color(RED)

        """ LOL """
        self.play(Write(fx_1))
        self.wait(0.5)
        self.play(ReplacementTransform(fx_1.copy()[0], fx_shifted[0]),
                ReplacementTransform(fx_1.copy()[1], fx_shifted[1]),
                ReplacementTransform(fx_1.copy()[2], fx_shifted[4]),
                ReplacementTransform(fx_1.copy()[3], fx_shifted[8]),
                ReplacementTransform(fx_1.copy()[4], fx_shifted[9]),
                ReplacementTransform(fx_1.copy()[5], fx_shifted[10]),
                ReplacementTransform(fx_1.copy()[6], fx_shifted[14]),
                ReplacementTransform(fx_1.copy()[7], fx_shifted[19]),
                ReplacementTransform(fx_1.copy()[8], fx_shifted[20]),
                ReplacementTransform(fx_1.copy()[9], fx_shifted[21]),
                ReplacementTransform(fx_1.copy()[10], fx_shifted[25]),
                ReplacementTransform(fx_1.copy()[11], fx_shifted[30]),
                ReplacementTransform(fx_1.copy()[12], fx_shifted[31]),
                ReplacementTransform(fx_1.copy()[13], fx_shifted[32]),
                ReplacementTransform(fx_1.copy()[14], fx_shifted[36]),
                ReplacementTransform(fx_1.copy()[15], fx_shifted[41]),
                ReplacementTransform(fx_1.copy()[16], fx_shifted[42]),)
        self.wait(0.5)
        self.play(Write(fx_shifted[2]),
                Write(fx_shifted[3]),
                Write(fx_shifted[5]),
                Write(fx_shifted[6]),
                Write(fx_shifted[7]),
                Write(fx_shifted[11]),
                Write(fx_shifted[12]),
                Write(fx_shifted[13]),
                Write(fx_shifted[15]),
                Write(fx_shifted[16]),
                Write(fx_shifted[17]),
                Write(fx_shifted[18]),
                Write(fx_shifted[22]),
                Write(fx_shifted[23]),
                Write(fx_shifted[24]),
                Write(fx_shifted[26]),
                Write(fx_shifted[27]),
                Write(fx_shifted[28]),
                Write(fx_shifted[29]),
                Write(fx_shifted[33]),
                Write(fx_shifted[34]),
                Write(fx_shifted[35]),
                Write(fx_shifted[37]),
                Write(fx_shifted[38]),
                Write(fx_shifted[39]),
                Write(fx_shifted[40]))
        self.wait()

        """ explanation of a and b with arrows """
        a_expl = MathTex("a", "\\text{ is the horizontal `stretch'}").scale(0.4).shift(DOWN*2)
        b_expl = MathTex("b", "\\text{ is the horizontal `shift'}").scale(0.4).shift(RIGHT*2+DOWN*2)
        a_arrow = Arrow(a_expl.get_top(), fx_shifted[2].get_bottom(), color=YELLOW)
        b_arrow = Arrow(b_expl.get_top(), fx_shifted[6].get_bottom(), color=YELLOW)
        self.play(FadeIn(a_expl), FadeIn(a_arrow))
        self.wait()
        self.play(FadeOut(a_expl), FadeOut(a_arrow))
        self.wait(0.5)
        self.play(FadeIn(b_expl), FadeIn(b_arrow))
        self.wait()
        self.play(FadeOut(b_expl), FadeOut(b_arrow))

        """ a and b values and labels """
        a_lab = always_redraw(
            lambda : MathTex("a", "=").scale(0.6).next_to(fx_shifted, DOWN*2)
        )
        a_val = always_redraw(
            lambda : MathTex(round(a.get_value(), 1)).scale(0.6).next_to(a_lab, RIGHT)
        )
        b_lab = always_redraw(
            lambda : MathTex("b", "=").scale(0.6).next_to(a_lab, DOWN*2)
        )
        b_val = always_redraw(
            lambda : MathTex(round(b.get_value(), 1)).scale(0.6).next_to(b_lab, RIGHT)
        )

        """ Animate coefficient values and rest """
        self.play(Write(a_lab), Write(b_lab))
        self.play(Write(a_val), Write(b_val))
        self.wait()
        self.play(a.animate.set_value(0.5))
        self.wait(0.5)
        self.play(a.animate.set_value(-2))
        self.wait()
        self.play(b.animate.set_value(2))
        self.wait()
        self.play(b.animate.set_value(-2))
        self.wait()
        self.play(a.animate.set_value(1), b.animate.set_value(0))
        self.wait(1.5)

        """ Fading OG equation and adding new texts """
        self.play(FadeOut(a_lab), FadeOut(a_val), FadeOut(b_lab), FadeOut(b_val), FadeOut(fx_1))
        self.play(fx_shifted.animate.to_edge(UP, buff=LARGE_BUFF))
        
        comm_1 = MathTex("\\text{When values of }" "a", "\\text{ and }", "b", "\\text{ are altered}").scale(0.6).move_to(RIGHT*3.5+UP*0.25)
        comm_2 = MathTex("\\text{the value of the roots change as well}").scale(0.6).move_to(RIGHT*3.5+DOWN*0.25)
        comm_3 = MathTex("(", "\\alpha_i =", alpha.get_value(), "\\text{, }",
                    "\\beta_i =", beta.get_value(), "\\text{, }",
                    "\\gamma_i =", gamma.get_value(), ")").scale(0.6).move_to(RIGHT*3.5+DOWN*0.75)

        self.play(Write(comm_1))
        self.play(Write(comm_2))
        self.wait()
        self.play(Write(comm_3))
        self.wait(0.5)

        self.play(comm_1.animate.shift(UP*1.5), comm_2.animate.shift(UP*1.5), comm_3.animate.shift(UP*1.5))
        self.wait()

        label_a = always_redraw(
            lambda : MathTex("a", "=").scale(0.75).move_to(RIGHT*3)
        )
        label_b = always_redraw(
            lambda : MathTex("b", "=").scale(0.75).next_to(label_a, DOWN).align_to(label_a, RIGHT)
        )
        label_alpha = always_redraw(
            lambda : MathTex("\\alpha", "=").scale(0.75).next_to(label_b, DOWN, buff=1).align_to(label_b, RIGHT)
        )
        label_beta = always_redraw(
            lambda : MathTex("\\beta", "=").scale(0.75).next_to(label_alpha, DOWN).align_to(label_alpha, RIGHT)
        )
        label_gamma = always_redraw(
            lambda : MathTex("\\gamma", "=").scale(0.75).next_to(label_beta, DOWN).align_to(label_beta, RIGHT)
        )

        value_a = always_redraw(
            lambda : MathTex(round(a.get_value(), 1)).scale(0.75).next_to(label_a, RIGHT)
        )
        f_always(value_a.set_color, lambda : GOLD)
        value_b = always_redraw(
            lambda : MathTex(round(b.get_value(), 1)).scale(0.75).next_to(label_b, RIGHT)
        )
        f_always(value_b.set_color, lambda : PINK)
        value_alpha = always_redraw(
            lambda : MathTex(round((alpha.get_value()/a.get_value())+b.get_value(), 1)).scale(0.75).next_to(label_alpha, RIGHT)
        )
        f_always(value_alpha.set_color, lambda : YELLOW)
        value_beta = always_redraw(
            lambda : MathTex(round((beta.get_value()/a.get_value())+b.get_value(), 1)).scale(0.75).next_to(label_beta, RIGHT)
        )
        f_always(value_beta.set_color, lambda : GREEN)
        value_gamma = always_redraw(
            lambda : MathTex(round((gamma.get_value()/a.get_value())+b.get_value(), 1)).scale(0.75).next_to(label_gamma, RIGHT)
        )
        f_always(value_gamma.set_color, lambda : BLUE_B)

        """ Dots at roots """
        dot_r1 = always_redraw(
            lambda : Dot(self.coords_to_point((alpha.get_value()/a.get_value())+b.get_value(), 0))
        )
        dot_r2 = always_redraw(
            lambda : Dot(self.coords_to_point((beta.get_value()/a.get_value())+b.get_value(), 0))
        )
        dot_r3 = always_redraw(
            lambda : Dot(self.coords_to_point((gamma.get_value()/a.get_value())+b.get_value(), 0))
        )

        """ Root indicator triangle """
        tri1 = always_redraw(
            lambda : Triangle(color=GREY_A, fill_color=GREY_A, fill_opacity=1).move_to(dot_r1.get_bottom()+DOWN*0.25).scale(0.1)
        )
        tri2 = always_redraw(
            lambda : Triangle(color=GREY_A, fill_color=GREY_A, fill_opacity=1).move_to(dot_r2.get_bottom()+DOWN*0.25).scale(0.1)
        )
        tri3 = always_redraw(
            lambda : Triangle(color=GREY_A, fill_color=GREY_A, fill_opacity=1).move_to(dot_r3.get_bottom()+DOWN*0.25).scale(0.1)
        )

        tri1_lab = always_redraw(
            lambda : MathTex(round(((alpha.get_value()/a.get_value())+b.get_value()), 1)).scale(0.4).next_to(tri1, DOWN)
        )
        f_always(tri1_lab.set_color, lambda : YELLOW)

        tri2_lab = always_redraw(
            lambda : MathTex(round(((beta.get_value()/a.get_value())+b.get_value()), 1)).scale(0.4).next_to(tri2, DOWN)
        )
        f_always(tri2_lab.set_color, lambda : GREEN)

        tri3_lab = always_redraw(
            lambda : MathTex(round(((gamma.get_value()/a.get_value())+b.get_value()), 1)).scale(0.4).next_to(tri3, DOWN)
        )
        f_always(tri3_lab.set_color, lambda : BLUE_B)

        expl_alpha = always_redraw(
            lambda : MathTex("=", "{\\alpha_i", "\\over", round(a.get_value(), 1), "}", "+", "(", round(b.get_value(), 1), ")").scale(0.5).next_to(value_alpha, RIGHT)
        )
        f_always(expl_alpha[1].set_color, lambda : BLUE_A)
        f_always(expl_alpha[3].set_color, lambda : GOLD)
        f_always(expl_alpha[7].set_color, lambda : PINK)
        
        expl_beta = always_redraw(
            lambda : MathTex("=", "{\\beta_i", "\\over", round(a.get_value(), 1), "}", "+", "(", round(b.get_value(), 1), ")").scale(0.5).next_to(value_beta, RIGHT)
        )
        f_always(expl_beta[1].set_color, lambda : BLUE_A)
        f_always(expl_beta[3].set_color, lambda : GOLD)
        f_always(expl_beta[7].set_color, lambda : PINK)
        
        expl_gamma = always_redraw(
            lambda : MathTex("=", "{\\gamma_i", "\\over", round(a.get_value(), 1), "}", "+", "(", round(b.get_value(), 1), ")").scale(0.5).next_to(value_gamma, RIGHT)
        )
        f_always(expl_gamma[1].set_color, lambda : BLUE_A)
        f_always(expl_gamma[3].set_color, lambda : GOLD)
        f_always(expl_gamma[7].set_color, lambda : PINK)

        self.play(Write(dot_r1), Write(dot_r2), Write(dot_r3))
        self.play(FadeIn(tri1), FadeIn(tri2), FadeIn(tri3), Write(tri1_lab), Write(tri2_lab), Write(tri3_lab))
        self.wait()
        
        self.play(Write(label_a), Write(label_b))
        self.play(Write(value_a), Write(value_b))
        self.wait(0.5)

        self.play(Write(label_alpha), Write(label_beta), Write(label_gamma))
        self.play(Write(value_alpha), Write(value_beta), Write(value_gamma))
        self.wait(0.5)

        self.play(Write(expl_alpha), Write(expl_beta), Write(expl_gamma))
        self.wait()

        
        self.play(a.animate.set_value(0.5), b.animate.set_value(-1))
        self.wait(1.5)
        self.play(a.animate.set_value(0.25), b.animate.set_value(1))
        self.wait(1.5)
        self.play(b.animate.set_value(2))
        self.wait(1.5)
        self.play(a.animate.set_value(2))
        self.wait(1.5)
        self.play(a.animate.set_value(1), b.animate.set_value(0))
        self.wait()

        