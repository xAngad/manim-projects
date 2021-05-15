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
            x_min=-9,
            x_max=9,
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
        self.axes.scale(0.75).to_edge(LEFT)
        self.play(Write(self.axes))
        
        """ Setup values of coefficients and roots """
        a = ValueTracker(1)
        b = ValueTracker(0)
        alpha = ValueTracker(-2)
        beta = ValueTracker(0)
        gamma = ValueTracker(2)
        n = ValueTracker(1)

        
        """ Equation of cubic polynomial """
        def eq1(x):
            return ((x + 2) * (x) * (x - 2))

        def eq2(x):
            return ((np.cbrt(x) + 2) * (np.cbrt(x)) * (np.cbrt(x) - 2))
        
        def eq_sq(x):
            return ((np.power(x, 2) + 2) * (np.power(x, 2)) * (np.power(x, 2) - 2))
        
        def eq_cub(x):
            return ((np.power(x, 3) + 2) * (np.power(x, 3)) * (np.power(x, 3) - 2))
        
        """ Graph functions """
        graf1 = self.get_graph(eq1, color=RED)
        graf2 = self.get_graph(eq2, color=RED)
        graf3 = self.get_graph(eq_sq, color=RED, x_min=-2, x_max=2)
        graf4 = self.get_graph(eq_cub, color=RED, x_min=-2, x_max=2)

        self.play(Write(graf1))

        """ Texts """
        fx_1 = MathTex("f", "(", "x", ")", "=",
                    "p", "{x", "^3}",
                    "+",
                    "q", "{x", "^2}",
                    "+",
                    "r", "x",
                    "+",
                    "s").scale(0.75).shift(RIGHT*3.5)
        f_always(fx_1[2].set_color, lambda : RED)
        f_always(fx_1[6].set_color, lambda : RED)
        f_always(fx_1[10].set_color, lambda : RED)
        f_always(fx_1[14].set_color, lambda : RED)

        fx_2 = MathTex("f", "(", "{x", "^n}", ")", "=",
                    "p", "{x", "^{3n}}",
                    "+",
                    "q", "{x", "^{2n}}",
                    "+",
                    "r", "{x^n}",
                    "+",
                    "s").scale(0.75).shift(RIGHT*3.5).to_edge(UP, buff=LARGE_BUFF)
        f_always(fx_2[2].set_color, lambda : RED)
        f_always(fx_2[7].set_color, lambda : RED)
        f_always(fx_2[11].set_color, lambda : RED)
        f_always(fx_2[15].set_color, lambda : RED)

        self.play(Write(fx_1))
        self.wait()
        self.play(fx_1.animate.to_edge(UP, buff=LARGE_BUFF))

        comm_1 = MathTex("\\text{When }", "x", "\\text{ is raised to some power, }", "n").scale(0.6).move_to(RIGHT*3.5+UP*0.25)
        comm_2 = MathTex("\\text{the roots are raised to }", "\\frac{1}{n}").scale(0.6).move_to(RIGHT*3.5+DOWN*0.25)
        comm_3 = MathTex("(", "\\alpha_i =", alpha.get_value(), "\\text{, }",
                    "\\beta_i =", beta.get_value(), "\\text{, }",
                    "\\gamma_i =", gamma.get_value(), ")").scale(0.6).move_to(RIGHT*3.5+DOWN*0.75)

        self.play(Write(comm_1), ReplacementTransform(fx_1, fx_2))
        self.play(Write(comm_2))
        self.wait(0.5)
        self.play(Write(comm_3))

        self.wait(1.5)

        self.play(comm_1.animate.shift(UP*1.5), comm_2.animate.shift(UP*1.5), comm_3.animate.shift(UP*1.5))
        self.wait()

        """ Root labels """
        label_n = always_redraw(
            lambda : MathTex("n", "=").scale(0.75).move_to(RIGHT*3)
        )
        label_alpha = always_redraw(
            lambda : MathTex("\\alpha", "=").scale(0.75).next_to(label_n, DOWN, buff=1).align_to(label_n, RIGHT)
        )
        label_beta = always_redraw(
            lambda : MathTex("\\beta", "=").scale(0.75).next_to(label_alpha, DOWN).align_to(label_alpha, RIGHT)
        )
        label_gamma = always_redraw(
            lambda : MathTex("\\gamma", "=").scale(0.75).next_to(label_beta, DOWN).align_to(label_beta, RIGHT)
        )
        
        """ Root values """
        value_n = always_redraw(
            lambda : MathTex(round(n.get_value(), 2)).scale(0.75).next_to(label_n, RIGHT)
        )
        value_alpha = always_redraw(
            lambda : MathTex(round(alpha.get_value(), 2)).scale(0.75).next_to(label_alpha, RIGHT)
        )
        f_always(value_alpha.set_color, lambda : YELLOW)
        value_beta = always_redraw(
            lambda : MathTex(round(beta.get_value(), 2)).scale(0.75).next_to(label_beta, RIGHT)
        )
        f_always(value_beta.set_color, lambda : GREEN)
        value_gamma = always_redraw(
            lambda : MathTex(round(gamma.get_value(), 2)).scale(0.75).next_to(label_gamma, RIGHT)
        )
        f_always(value_gamma.set_color, lambda : BLUE_B)

        """ Formulae for roots """
        expl_alpha = always_redraw(
            lambda : MathTex("=", "{\\alpha_i", "^{1", "\\over", round(n.get_value(), 2), "}", "}").scale(0.5).next_to(value_alpha, RIGHT)
        )
        f_always(expl_alpha[1].set_color, lambda : BLUE_A)
        
        expl_beta = always_redraw(
            lambda : MathTex("=", "{\\beta_i", "^{1", "\\over", round(n.get_value(), 2), "}", "}").scale(0.5).next_to(value_beta, RIGHT)
        )
        f_always(expl_beta[1].set_color, lambda : BLUE_A)
        
        expl_gamma = always_redraw(
            lambda : MathTex("=", "{\\gamma_i", "^{1", "\\over", round(n.get_value(), 2), "}", "}").scale(0.5).next_to(value_gamma, RIGHT)
        )
        f_always(expl_gamma[1].set_color, lambda : BLUE_A)

        self.play(Write(label_alpha), Write(label_beta), Write(label_gamma), Write(label_n))
        self.play(Write(value_alpha), Write(value_beta), Write(value_gamma), Write(value_n))
        self.play(Write(expl_alpha), Write(expl_beta), Write(expl_gamma))

        self.play(ReplacementTransform(graf1, graf2),
                n.animate.set_value(0.33),
                alpha.animate.set_value(-8),
                beta.animate.set_value(0),
                gamma.animate.set_value(8))
        self.wait(2)
        self.play(ReplacementTransform(graf2, graf4),
                n.animate.set_value(3),
                alpha.animate.set_value(-1.26),
                beta.animate.set_value(0),
                gamma.animate.set_value(1.26))