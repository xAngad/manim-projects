from manim import *

class complexB(Scene):
    def construct(self):
        """ Setup Complex Plane """
        global axes
        axes = ComplexPlane(
            x_range=(-16, 16, 1),
            y_range=(-2 * config["frame_y_radius"], 2 * config["frame_y_radius"], 1),
            x_length=2*config["frame_x_radius"],
            y_length=2*config["frame_y_radius"]
        )
        axes.add_coordinates()
        axes.set_opacity(0.5)
        self.add(axes)

        global modulus, theta
        modulus = 2
        denom = ValueTracker(2)


        """ Overlay for Equations """
        """ VERY IMPORTANT """
        overlay_right = ScreenRectangle(aspect_ratio=2.0/3.0, height=7,
                                    stroke_opacity=0, fill_color=BLACK, fill_opacity=0.75)
        overlay_right.shift(RIGHT * 4)
        self.add(overlay_right)


        """ Complex Dot """
        w = always_redraw(
            lambda : Dot(axes.c2p(modulus * np.cos(PI/denom.get_value()),
                                modulus * np.sin(PI/denom.get_value())))
        )


        """ Equations """
        w_eq_main = MathTex("w", "=", "2", "\\left(", "\\cos", "{\\pi", "\\over", "n}", "+",
                                "i", "\\sin", "{\\pi", "\\over", "n", "}", "\\right)").move_to(overlay_right.get_center())
        w_eq_main.scale_to_fit_width(4.5)

        w_eq_n_1 = always_redraw(
            lambda : MathTex("w", "=", "2", "\\left(", "\\cos", "{\\pi", "\\over", round(denom.get_value(), 2), "}", "+",
                                "i", "\\sin", "{\\pi", "\\over", round(denom.get_value(), 2), "}", "\\right)").move_to(overlay_right.get_center())
        )
        w_eq_n_1.scale_to_fit_width(4.5)
        self.add(w_eq_main)

        """ Text explanations #1 """
        words_1 = MathTex("\\text{When }", "w", "\\text{ is raised}").move_to(overlay_right.get_center()+UP*2.5)
        words_2 = MathTex("\\text{to a power }", "m").move_to(overlay_right.get_center()+UP*2)

        self.play(Write(words_1), Write(words_2))

        w_eq_m_1 = MathTex("{w", "^m}", "=", "{2", "^m}", "{\\left(", "\\cos", "{\\pi", "\\over", "n}", "+",
                                "i", "\\sin", "{\\pi", "\\over", "n", "}", "\\right)", "^m}").move_to(overlay_right.get_center())
        w_eq_m_1.scale_to_fit_width(4.5)

        w_eq_m_2 = MathTex("{w", "^m}", "=", "{2", "^m}", "\\left(", "\\cos", "{m", "\\pi", "\\over", "n}", "+",
                                "i", "\\sin", "{m", "\\pi", "\\over", "n", "}", "\\right)").move_to(overlay_right.get_center())
        w_eq_m_2.scale_to_fit_width(4.5)

        self.play(TransformMatchingShapes(w_eq_main, w_eq_m_1))
        self.wait()
        self.play(TransformMatchingShapes(w_eq_m_1, w_eq_m_2))
        self.wait()

        words_3 = MathTex("\\text{if }", "m", "=", "n", ",").move_to(overlay_right.get_center()+DOWN*2).scale(0.6)
        words_4 = MathTex("\\theta", "=", "\\pi").move_to(overlay_right.get_center()+DOWN*2.5).scale(0.6)

        self.play(Write(words_3), Write(words_4))
        self.wait(2)
        self.play(FadeOut(words_1), FadeOut(words_2), FadeOut(words_3), FadeOut(words_4))
        self.wait()

        """ Varying 'm' and 'n' to show roots """
        m = ValueTracker(1)

        #n2
        n2m1 = MathTex("=",
                            "{2", "^", "1", "}",
                            "\\left(", "\\cos", "{", "\\pi", "\\over", "2", "}", "+",
                            "i", "\\sin", "{", "\\pi", "\\over", "2", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        n2m2 = MathTex("=",
                            "{2", "^", "2", "}",
                            "\\left(", "\\cos", "{", "2", "\\pi", "\\over", "2", "}", "+",
                            "i", "\\sin", "{", "2", "\\pi", "\\over", "2", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        
        #n3
        n3m1 = MathTex("=",
                            "{2", "^", "1", "}",
                            "\\left(", "\\cos", "{", "\\pi", "\\over", "3", "}", "+",
                            "i", "\\sin", "{", "\\pi", "\\over", "3", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        n3m2 = MathTex("=",
                            "{2", "^", "2", "}",
                            "\\left(", "\\cos", "{", "2", "\\pi", "\\over", "3", "}", "+",
                            "i", "\\sin", "{", "2", "\\pi", "\\over", "3", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        n3m3 = MathTex("=",
                            "{2", "^", "3", "}",
                            "\\left(", "\\cos", "{", "3", "\\pi", "\\over", "3", "}", "+",
                            "i", "\\sin", "{", "3", "\\pi", "\\over", "3", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        #n3
        n4m1 = MathTex("=",
                            "{2", "^", "1", "}",
                            "\\left(", "\\cos", "{", "\\pi", "\\over", "4", "}", "+",
                            "i", "\\sin", "{", "\\pi", "\\over", "4", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        n4m2 = MathTex("=",
                            "{2", "^", "2", "}",
                            "\\left(", "\\cos", "{", "2", "\\pi", "\\over", "4", "}", "+",
                            "i", "\\sin", "{", "2", "\\pi", "\\over", "4", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        n4m3 = MathTex("=",
                            "{2", "^", "3", "}",
                            "\\left(", "\\cos", "{", "3", "\\pi", "\\over", "4", "}", "+",
                            "i", "\\sin", "{", "3", "\\pi", "\\over", "4", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5) 
        n4m4 = MathTex("=",
                            "{2", "^", "4", "}",
                            "\\left(", "\\cos", "{", "4", "\\pi", "\\over", "4", "}", "+",
                            "i", "\\sin", "{", "4", "\\pi", "\\over", "4", "}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.5) 
        
        
        self.play(TransformMatchingShapes(w_eq_m_2, n2m1))

        n2 = MathTex("n", "=", "2").move_to(overlay_right.get_center()+UP*2.5)
        n3 = MathTex("n", "=", "3").move_to(overlay_right.get_center()+UP*2.5)
        n4= MathTex("n", "=", "4").move_to(overlay_right.get_center()+UP*2.5)
        m1 = MathTex("m", "=", "1").move_to(overlay_right.get_center()+UP*1.75)
        m2 = MathTex("m", "=", "2").move_to(overlay_right.get_center()+UP*1.75)
        m3 = MathTex("m", "=", "3").move_to(overlay_right.get_center()+UP*1.75)
        m4 = MathTex("m", "=", "4").move_to(overlay_right.get_center()+UP*1.75)

        # Arrays of dots
        n_2_dots = [
            Dot(axes.c2p(0, 2), color=YELLOW),
            Dot(axes.c2p(-4, 0), color=YELLOW)
        ]
        
        n_3_dots = [
            Dot(axes.c2p(1, np.sqrt(3)), color=YELLOW),
            Dot(axes.c2p(-2, 2*np.sqrt(3)), color=YELLOW),
            Dot(axes.c2p(-8, 0), color=YELLOW)
        ]

        n_4_dots = [
            Dot(axes.c2p(np.sqrt(2), np.sqrt(2)), color=YELLOW),
            Dot(axes.c2p(0, 4), color=YELLOW),
            Dot(axes.c2p(-4*np.sqrt(2), 4*np.sqrt(2)), color=YELLOW),
            Dot(axes.c2p(-16, 0), color=YELLOW)
        ]

        self.play(Write(n2), Write(m1))
        self.wait()

        # n = 2
        self.play(Write(n_2_dots[0]))
        self.wait(1.5)
        self.play(Write(n_2_dots[1]), TransformMatchingShapes(n2m1, n2m2), TransformMatchingShapes(m1, m2))
        self.wait(1.5)
        self.play(FadeOut(n_2_dots[0]), FadeOut(n_2_dots[1]))

        # # n = 3
        self.play(Write(n_3_dots[0]), TransformMatchingShapes(n2m2, n3m1), TransformMatchingShapes(m2, m1), TransformMatchingShapes(n2, n3))
        self.wait(1.5)
        self.play(Write(n_3_dots[1]), TransformMatchingShapes(n3m1, n3m2), TransformMatchingShapes(m1, m2))
        self.wait(1.5)
        self.play(Write(n_3_dots[2]), TransformMatchingShapes(n3m2, n3m3), TransformMatchingShapes(m2, m3))
        self.wait(1.5)
        self.play(FadeOut(n_3_dots[0]), FadeOut(n_3_dots[1]), FadeOut(n_3_dots[2]))

        # n = 4
        self.play(Write(n_4_dots[0]), TransformMatchingShapes(n3m3, n4m1), TransformMatchingShapes(m3, m1), TransformMatchingShapes(n3, n4))
        self.wait(1.5)
        self.play(Write(n_4_dots[1]), TransformMatchingShapes(n4m1, n4m2), TransformMatchingShapes(m1, m2))
        self.wait(1.5)
        self.play(Write(n_4_dots[2]), TransformMatchingShapes(n4m2, n4m3), TransformMatchingShapes(m2, m3))
        self.wait(1.5)
        self.play(Write(n_4_dots[3]), TransformMatchingShapes(n4m3, n4m4), TransformMatchingShapes(m3, m4))
        self.wait(2.5)

        self.play(FadeOut(n4m4), FadeOut(m4), FadeOut(n4))
        self.wait()

        w0_eq = always_redraw(
            lambda : MathTex("\\text{Lastly, }", "w^0", "\\text{ always equals 1.}").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        )
        w0 = Dot(axes.c2p(1, 0), color=YELLOW)
        self.play(Write(w0_eq), Write(w0))
        self.wait(1.5)
        self.play(FadeOut(w0_eq))
        self.wait(1)

        d1_lab = MathTex("w^0").scale(0.5).next_to(w0, DOWN)
        d2_lab = MathTex("w^1").scale(0.5).next_to(n_4_dots[0], UR)
        d3_lab = MathTex("w^2").scale(0.5).next_to(n_4_dots[1], UP)
        d4_lab = MathTex("w^3").scale(0.5).next_to(n_4_dots[2], UP)
        d5_lab = MathTex("w^4").scale(0.5).next_to(n_4_dots[3], DR)

        """ Explanations #2 """
        poly_exp_1_1 = MathTex("\\text{When plotted, }", "w^0,", "w^1,", "w^2,", "\\dots", "w^n").move_to(overlay_right.get_center()+UP*0.5).scale_to_fit_width(4.5)
        poly_exp_1_2 = MathTex("\\text{create an }", "(n+1)", "\\text{-sided polygon}").move_to(overlay_right.get_center()).scale_to_fit_width(4.5)
        poly_exp_1_3 = MathTex("\\text{comprising of }", "n", "\\text{ triangles}").move_to(overlay_right.get_center()+DOWN*0.5).scale_to_fit_width(4.5)

        poly = Polygon(w0.get_center(), n_4_dots[0].get_center(), n_4_dots[1].get_center(), n_4_dots[2].get_center(), n_4_dots[3].get_center(),
                    fill_color=WHITE, fill_opacity=0.5,
                    stroke_color=WHITE, stroke_opacity=1)
        tri1 = Polygon(axes.c2p(0, 0), w0.get_center(), n_4_dots[0].get_center(),
                    fill_color=RED, fill_opacity=0.5, stroke_color=RED, stroke_opacity=1)
        tri2 = Polygon(axes.c2p(0, 0), n_4_dots[0].get_center(), n_4_dots[1].get_center(),
                    fill_color=BLUE, fill_opacity=0.5, stroke_color=BLUE, stroke_opacity=1)
        tri3 = Polygon(axes.c2p(0, 0), n_4_dots[1].get_center(), n_4_dots[2].get_center(),
                    fill_color=GREEN, fill_opacity=0.5, stroke_color=GREEN, stroke_opacity=1)
        tri4 = Polygon(axes.c2p(0, 0), n_4_dots[2].get_center(), n_4_dots[3].get_center(),
                    fill_color=PURPLE, fill_opacity=0.5, stroke_color=PURPLE, stroke_opacity=1)

        self.play(Write(poly_exp_1_1),
                FadeIn(d1_lab), FadeIn(d2_lab), FadeIn(d3_lab), FadeIn(d4_lab), FadeIn(d5_lab))
        self.wait()
        self.play(Write(poly_exp_1_2), Write(poly))
        self.wait()
        self.play(Write(poly_exp_1_3), Write(tri1), Write(tri2), Write(tri3), Write(tri4))
        # self.wait(2)
        self.play(FadeOut(poly_exp_1_1), FadeOut(poly_exp_1_2), FadeOut(poly_exp_1_3))

        """ Calculating areas """
        dots = [
            Dot(axes.c2p(0, 0), color=WHITE),
            Dot(axes.c2p(1, 0), color=WHITE),
            Dot(axes.c2p(np.sqrt(2), np.sqrt(2)), color=WHITE),
            Dot(axes.c2p(0, 4), color=WHITE),
            Dot(axes.c2p(-4*np.sqrt(2), 4*np.sqrt(2)), color=WHITE),
            Dot(axes.c2p(-16, 0), color=WHITE)
        ]

        ''' triangle #1 '''
        tri1_copy = tri1.copy()
        calc_area = MathTex("\\text{Area}", "=").move_to(overlay_right.get_center()+UP*1.5+LEFT*0.5)
        calc_1_1 = MathTex("=", "{1", "\\over", "2}",
                        "\\left|w^0\\right|", "\\left|w^1\\right|", "\\sin\\theta").move_to(overlay_right.get_center())
        calc_1_2 = MathTex("=", "{1", "\\over", "2}",
                        "R^0", "R^1", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        calc_1_3 = MathTex("=", "{1", "\\over", "2}",
                        "R", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        
        # Area title
        self.play(Write(calc_area))

        # Triangle 1
        self.play(tri1_copy.animate.scale(0.5).next_to(calc_area, RIGHT, buff=0.5))
        self.wait()
        self.play(Write(calc_1_1), Write(dots[0]), Write(dots[1]), Write(dots[2]), tri1.animate.set_opacity(1))
        self.wait()
        self.play(Write(calc_1_2))
        self.wait()
        self.play(TransformMatchingShapes(calc_1_2, calc_1_3))
        self.wait(2)
        self.play(FadeOut(calc_1_1), FadeOut(calc_1_3), FadeOut(tri1_copy),
                FadeOut(dots[0]), FadeOut(dots[1]), FadeOut(dots[2]),
                tri1.animate.set_opacity(0.5))
        self.wait(1.5)

        ''' triangle #2 '''
        tri2_copy = tri2.copy()
        calc_2_1 = MathTex("=", "{1", "\\over", "2}",
                        "\\left|w^1\\right|", "\\left|w^2\\right|", "\\sin\\theta").move_to(overlay_right.get_center())
        calc_2_2 = MathTex("=", "{1", "\\over", "2}",
                        "R^1", "R^2", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        calc_2_3 = MathTex("=", "{1", "\\over", "2}",
                        "R^3", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        
        # Triangle 1
        self.play(tri2_copy.animate.scale(0.5).next_to(calc_area, RIGHT, buff=0.4))
        self.wait()
        self.play(Write(calc_2_1), Write(dots[0]), Write(dots[2]), Write(dots[3]), tri2.animate.set_opacity(1))
        self.wait()
        self.play(Write(calc_2_2))
        self.wait()
        self.play(TransformMatchingShapes(calc_2_2, calc_2_3))
        self.wait(2)
        self.play(FadeOut(calc_2_1), FadeOut(calc_2_3), FadeOut(tri2_copy),
                FadeOut(dots[0]), FadeOut(dots[2]), FadeOut(dots[3]),
                tri2.animate.set_opacity(0.5))
        self.wait(1.5)

        ''' triangle #3 '''
        tri3_copy = tri3.copy()
        calc_3_1 = MathTex("=", "{1", "\\over", "2}",
                        "\\left|w^2\\right|", "\\left|w^3\\right|", "\\sin\\theta").move_to(overlay_right.get_center())
        calc_3_2 = MathTex("=", "{1", "\\over", "2}",
                        "R^2", "R^3", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        calc_3_3 = MathTex("=", "{1", "\\over", "2}",
                        "R^5", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        
        # Triangle 1
        self.play(tri3_copy.animate.scale(0.5).next_to(calc_area, RIGHT, buff=0.25))
        self.wait()
        self.play(Write(calc_3_1), Write(dots[0]), Write(dots[3]), Write(dots[4]), tri3.animate.set_opacity(1))
        self.wait()
        self.play(Write(calc_3_2))
        self.wait()
        self.play(TransformMatchingShapes(calc_3_2, calc_3_3))
        self.wait(2)
        self.play(FadeOut(calc_3_1), FadeOut(calc_3_3), FadeOut(tri3_copy),
                FadeOut(dots[0]), FadeOut(dots[3]), FadeOut(dots[4]),
                tri3.animate.set_opacity(0.5))
        self.wait(1.5)

        ''' triangle #4 '''
        tri4_copy = tri4.copy()
        calc_4_1 = MathTex("=", "{1", "\\over", "2}",
                        "\\left|w^3\\right|", "\\left|w^4\\right|", "\\sin\\theta").move_to(overlay_right.get_center())
        calc_4_2 = MathTex("=", "{1", "\\over", "2}",
                        "R^3", "R^4", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        calc_4_3 = MathTex("=", "{1", "\\over", "2}",
                        "R^7", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*1.5)
        
        # Triangle 1
        self.play(tri4_copy.animate.scale(0.25).next_to(calc_area, RIGHT, buff=0))
        self.wait()
        self.play(Write(calc_4_1), Write(dots[0]), Write(dots[4]), Write(dots[5]), tri4.animate.set_opacity(1))
        self.wait()
        self.play(Write(calc_4_2))
        self.wait()
        self.play(TransformMatchingShapes(calc_4_2, calc_4_3))
        self.wait(2)
        self.play(FadeOut(calc_4_1), FadeOut(calc_4_3), FadeOut(tri4_copy),
                FadeOut(dots[0]), FadeOut(dots[4]), FadeOut(dots[5]),
                tri4.animate.set_opacity(0.5))
        self.wait(1.5)

        """ Combining results """
        area_total = MathTex("\\text{Total Area}", "=").move_to(overlay_right.get_center()+UP*3)
        self.play(TransformMatchingShapes(calc_area, area_total))
        comb_area_1_1 = MathTex("+", "{1", "\\over", "2}",
                        "R^0", "R^1", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+UP*1.5).scale(0.7)
        comb_area_2_1 = MathTex("+", "{1", "\\over", "2}",
                        "R^1", "R^2", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+UP*0.7).scale(0.7)
        comb_area_3_1 = MathTex("+", "{1", "\\over", "2}",
                        "R^2", "R^3", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*0.1).scale(0.7)
        comb_area_4_1 = MathTex("+", "{1", "\\over", "2}",
                        "R^3", "R^4", "\\sin", "{\\pi", "\\over", "3}").move_to(overlay_right.get_center()+DOWN*0.9).scale(0.7)
        self.play(Write(comb_area_1_1))
        self.play(Write(comb_area_2_1))
        self.play(Write(comb_area_3_1))
        self.play(Write(comb_area_4_1))

        if_n = MathTex("\\text{If there were }", "n", "\\text{ triangles:}").move_to(overlay_right.get_center()+UP*2.25).scale_to_fit_width(4)

        comb_area_1_2 = MathTex("+", "{1", "\\over", "2}",
                        "R^0", "R^1", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+UP*1.5).scale(0.7)
        comb_area_2_2 = MathTex("+", "{1", "\\over", "2}",
                        "R^1", "R^2", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+UP*0.7).scale(0.7)
        comb_area_3_2 = MathTex("+", "{1", "\\over", "2}",
                        "R^2", "R^3", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*0.1).scale(0.7)
        comb_area_4_2 = MathTex("+", "{1", "\\over", "2}",
                        "R^3", "R^4", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*0.9).scale(0.7)

        comb_dots = MathTex("\\vdots").move_to(overlay_right.get_center()+DOWN*1.7).scale(1)
        
        comb_area_n_1 = MathTex("+", "{1", "\\over", "2}",
                        "R^{n-1}", "R^n", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*2.5).scale(0.7)
            
        self.play(Write(if_n))
        self.wait(0.5)
        self.play(Write(comb_dots))
        self.play(Write(comb_area_n_1),
                TransformMatchingShapes(comb_area_1_1, comb_area_1_2),
                TransformMatchingShapes(comb_area_2_1, comb_area_2_2),
                TransformMatchingShapes(comb_area_3_1, comb_area_3_2),
                TransformMatchingShapes(comb_area_4_1, comb_area_4_2))
        self.wait(1.5)

        comb_area_1_3 = MathTex("+", "{1", "\\over", "2}",
                        "R^1", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+UP*1.5).scale(0.7)
        comb_area_2_3 = MathTex("+", "{1", "\\over", "2}",
                        "R^3", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+UP*0.7).scale(0.7)
        comb_area_3_3 = MathTex("+", "{1", "\\over", "2}",
                        "R^5", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*0.1).scale(0.7)
        comb_area_4_3 = MathTex("+", "{1", "\\over", "2}",
                        "R^6", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*0.9).scale(0.7)
        comb_area_n_2 = MathTex("+", "{1", "\\over", "2}",
                        "R^{2n-1}", "\\sin", "{\\pi", "\\over", "n}").move_to(overlay_right.get_center()+DOWN*2.5).scale(0.7)
        
        self.play(TransformMatchingShapes(comb_area_1_2, comb_area_1_3),
                TransformMatchingShapes(comb_area_2_2, comb_area_2_3),
                TransformMatchingShapes(comb_area_3_2, comb_area_3_3),
                TransformMatchingShapes(comb_area_4_2, comb_area_4_3),
                TransformMatchingShapes(comb_area_n_1, comb_area_n_2))
        self.wait(2)
        
        comb_area_comb_1 = MathTex("{1", "\\over", "2}", "\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "R^1", "+", "R^3", "+", "R^5", "+", "\\dots", "+" "R^{2n-1}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)
        
        self.play(TransformMatchingShapes(comb_area_1_3, comb_area_comb_1),
                TransformMatchingShapes(comb_area_2_3, comb_area_comb_1),
                TransformMatchingShapes(comb_area_3_3, comb_area_comb_1),
                TransformMatchingShapes(comb_area_4_3, comb_area_comb_1),
                TransformMatchingShapes(comb_area_n_2, comb_area_comb_1),
                TransformMatchingShapes(comb_dots, comb_area_comb_1))
        self.wait()

        comb_area_comb_2 = MathTex("{1", "\\over", "2}", "\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "2^1", "+", "2^3", "+", "2^5", "+", "\\dots", "+" "2^{2n-1}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)

        self.play(TransformMatchingShapes(comb_area_comb_1, comb_area_comb_2))
        self.wait(2)

        comb_area_comb_3 = MathTex("\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "2^0", "+", "2^2", "+", "2^4", "+", "\\dots", "+" "2^{2n-2}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)

        self.play(TransformMatchingShapes(comb_area_comb_2, comb_area_comb_3))
        self.wait(2)
        
        comb_area_comb_4 = MathTex("\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "4^0", "+", "4^1", "+", "4^2", "+", "\\dots", "+" "4^{n-1}", "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)
        
        self.play(TransformMatchingShapes(comb_area_comb_3, comb_area_comb_4))
        self.wait(1.5)

        brace1 = BraceLabel(comb_area_comb_4[5:14], "\\text{Geometric Series}")
        self.play(Write(brace1))
        self.wait(1.5)
        self.play(FadeOut(brace1))

        comb_area_comb_5 = MathTex("\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "{1(4^n-1)", "\\over", "4-1}" "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)
        
        self.play(TransformMatchingShapes(comb_area_comb_4, comb_area_comb_5))
        self.wait(1.5)

        comb_area_comb_6 = MathTex("\\sin", "{\\pi", "\\over", "n}",
                                "\\left(", "{4^n-1", "\\over", "3}" "\\right)").move_to(overlay_right.get_center()).scale_to_fit_width(4.6)
        
        self.play(TransformMatchingShapes(comb_area_comb_5, comb_area_comb_6))
        self.play(Write(SurroundingRectangle(comb_area_comb_6, color=RED)))