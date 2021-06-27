from manim import *
import math

class unitCircle(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-2,
            x_max=2,
            x_axis_width=4,
            x_axis_label="",
            x_axis_config={"tick_frequency": 2},
            x_axis_visibility=False,
            y_min=-2,
            y_max=2,
            y_axis_height=4,
            y_axis_label="",
            y_axis_config={"tick_frequency": 2},
            y_axis_visibility=False,
            **kwargs           
        )
    
    def construct(self):
        # UNIT CIRCLE DIAGRAMS FUNCTIONS
        self.makePlane()
        self.makeCircleOutline()
        self.cameraInitialMovement()
        self.addSemicircles()
        self.drawRadii()
        self.centralAngle()
        self.drawTangents()
        self.braces()
        self.pointLabels()
        self.fadePlane()
        self.cameraRestoring()

        # #EXPLANATION
        self.considerAreasText()
        self.areasShaded()
        self.compareAreas()
        self.explainAreaSmall()
        self.explainAreaMedium()
        self.explainAreaLarge()

        # #FADE EVERYTHING
        self.fadeEverything()

    def makePlane(self):
        global number_plane_1
        number_plane_1 = NumberPlane(x_line_frequency=1,
                                y_line_frequency=1,
                                axis_config={"stroke_color": DARK_GRAY},
                                background_line_style={"stroke_color": DARK_GRAY})
        
        self.play(Write(number_plane_1))
    
    def makeCircleOutline(self):
        """DRAWING A CIRCLE - on top of which i'll put the graphs to make it work"""
        #circle defined
        global circ_main
        circ_main = Circle(stroke_color=BLUE).scale(2).shift(LEFT*5)

        #dot at circle and dot at center
        global dot_circ
        dot_circ = always_redraw(
            lambda : Dot(circ_main.get_end())
        )
        global dot_center
        dot_center = Dot(LEFT*5)
        
        #line from origin to circle
        global line_circ
        line_circ = always_redraw(
            lambda : Line(start=dot_center.get_center(), end=dot_circ.get_center())
        )
        
        #write stuff
        self.play(Write(dot_circ), Write(line_circ), Write(dot_center))
        self.play(Write(circ_main), run_time=3, rate_func=double_smooth)
    
    def cameraInitialMovement(self):
        """ saving camera location, and then zooming in to the circle """
        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(0.75).move_to(dot_circ.get_center()))
    
    def addSemicircles(self):
        """ Adding the semicircles so that i can use the tangent thing """
        #axes setup
        self.setup_axes(animate=False)
        self.axes.move_to(ORIGIN)
        self.axes.shift(LEFT*5)
        
        #equations of circle
        global equation_upper, equation_lower
        equation_upper = lambda x : math.sqrt((self.x_max)**2 - x**2)
        equation_lower = lambda x : -1*math.sqrt((self.x_max)**2 - x**2)

        #get_graph for upper and lower semicircle
        global graph_upper, graph_lower
        graph_upper = self.get_graph(equation_upper, color=BLUE)
        graph_lower = self.get_graph(equation_lower, color=BLUE)

        #write graphs
        self.add(graph_upper,graph_lower)
    
    def drawRadii(self):
        """ drawing the tangent triangle etc """
        #horizontal line (which i will extend later)
        global radius_horiz_end_val
        radius_horiz_end_val = ValueTracker(self.x_max)
        global radius_horiz
        radius_horiz = always_redraw(
            lambda : Line(start=dot_center.get_center(), end=self.coords_to_point(radius_horiz_end_val.get_value(),0))
        )
        global radius_horiz_end_dot
        radius_horiz_end_dot = always_redraw(
            lambda : Dot(radius_horiz.get_end())
        )

        #angled radius - can alter based on ValueTracker
        global theta
        theta = ValueTracker(0)
        global radius_ang_end_dot
        radius_ang_end_dot = always_redraw(
            lambda : Dot(self.coords_to_point(self.x_max * np.cos(theta.get_value()*DEGREES),
                                            equation_upper(self.x_max * np.cos(theta.get_value()*DEGREES))))
        )

        global radius_ang
        radius_ang = always_redraw(
            lambda : Line(start=dot_center.get_center() ,end=radius_ang_end_dot.get_center())
        )

        self.play(Write(radius_horiz), Write(radius_horiz_end_dot),
                Write(radius_ang_end_dot), Write(radius_ang))
        self.play(theta.animate.set_value(60))

    def centralAngle(self): 
        """ small arc to show angle """
        global central_angle
        central_angle = always_redraw(
            lambda : Angle(radius_horiz, radius_ang, radius=0.25, stroke_color=YELLOW)
        )

        global central_angle_label
        central_angle_label = always_redraw(
            lambda : MathTex("x", stroke_color=GREEN).scale(0.75).move_to(
                LEFT*5+UP*(0.3*self.x_max*np.sin(0.5*theta.get_value()*DEGREES))+RIGHT*(0.3*self.x_max*np.cos(0.5*theta.get_value()*DEGREES)))
        )

        self.play(Write(central_angle), Write(central_angle_label))
    
    def drawTangents(self):
        """ Drawing the tangent to the circle at the point defined by theta from above """
        #bigger tangent
        global big_tangent
        big_tangent = always_redraw(
            lambda : self.get_secant_slope_group(self.x_max * np.cos(theta.get_value()*DEGREES), graph_upper,
                                                dx=0.001, secant_line_color=RED, secant_line_length=6)
        )

        self.play(Write(big_tangent))
        self.wait(0.5)
        self.play(theta.animate.set_value(30))
        self.wait(0.5)
        self.play(theta.animate.set_value(45))
        self.wait(0.5)
        
        #smaller tangent
        global small_tangent
        small_tangent = always_redraw(
            lambda : Line(radius_ang_end_dot.get_center(), self.coords_to_point(
                                            math.sqrt((self.x_max)**2 + (self.x_max*np.tan(theta.get_value()*DEGREES))**2),
                                            0),
                                            )
        )
        global small_tangent_end_dot
        small_tangent_end_dot = always_redraw(
            lambda : Dot(self.coords_to_point(math.sqrt((self.x_max)**2 + (self.x_max*np.tan(theta.get_value()*DEGREES))**2),
                                            0))
        )

        global angled_rad
        angled_rad = always_redraw(
            lambda : Line(radius_ang.points[-1], radius_ang.points[0])
        )
        
        #right angle
        global right_angle
        right_angle = RightAngle(angled_rad, small_tangent, length=0.4, stroke_color=YELLOW)    
        
        self.play(Write(right_angle))
        self.wait(0.5)
        self.play(FadeOut(right_angle))
        self.play(Write(small_tangent), Write(small_tangent_end_dot), FadeOut(big_tangent))
        self.play(theta.animate.set_value(60))

        #extending horiz dot
        global dot_circ_copy
        dot_circ_copy = dot_circ.copy()

        #dropping perpendicular
        global dropped_dot
        dropped_dot = always_redraw(
            lambda : Dot(self.coords_to_point(self.x_max * np.cos(theta.get_value()*DEGREES), 0))
        )
        global dropped_perp
        dropped_perp = always_redraw(
            lambda : Line(radius_ang_end_dot.get_center(), dropped_dot.get_center())
        )

        #extended horizontal radius
        global radius_horiz_ext
        radius_horiz_ext = always_redraw(
            lambda : Line(dot_center.get_center(), self.coords_to_point(
                                            math.sqrt((self.x_max)**2 + (self.x_max*np.tan(theta.get_value()*DEGREES))**2), 0
            ))
        )

        self.play(Write(radius_horiz_ext), Write(dot_circ_copy), Write(dropped_dot), Write(dropped_perp))
    
    def braces(self):
        """ Braces around radii to show r=1 """
        global horiz_brace
        horiz_brace = always_redraw(
            lambda : Brace(radius_horiz)
        )
        global horiz_brace_label
        horiz_brace_label = always_redraw(
            lambda : MathTex("r=1").scale(0.6).next_to(horiz_brace, DOWN)
        )

        global angular_brace
        angular_brace = always_redraw(
            lambda : Brace(radius_ang, direction=radius_ang.copy().rotate(PI / 2).get_unit_vector())
        )
        global angular_brace_label
        angular_brace_label = always_redraw(
            lambda : MathTex("r=1").scale(0.6).next_to(angular_brace, LEFT)
        )

        self.play(Write(horiz_brace), Write(angular_brace))
        self.play(Write(horiz_brace_label), Write(angular_brace_label))

        self.play(FadeOut(horiz_brace), FadeOut(horiz_brace_label),
                FadeOut(angular_brace), FadeOut(angular_brace_label))
        
    def pointLabels(self):
        """ labelling the five important points """
        global ptA, ptB, ptC, ptD, ptE
        ptA = always_redraw(
            lambda : MathTex("\\text{A}").scale(0.75).next_to(dot_center, LEFT)
        )

        ptB = always_redraw(
            lambda : MathTex("\\text{B}").scale(0.75).next_to(radius_ang_end_dot, UP)
        )

        ptC = always_redraw(
            lambda : MathTex("\\text{C}").scale(0.75).next_to(small_tangent_end_dot, DOWN)
        )

        ptD = always_redraw(
            lambda : MathTex("\\text{D}").scale(0.75).next_to(radius_horiz_end_dot, DOWN)
        )

        ptE = always_redraw(
            lambda : MathTex("\\text{E}").scale(0.75).next_to(dropped_dot, DOWN)
        )

        self.play(Write(ptA),
                Write(ptB),
                Write(ptC),
                Write(ptD),
                Write(ptE))
        self.wait(0.5)

    def fadePlane(self):
        """ creating a VGroup so that i can move eveerything to the left together """
        global circle_group
        circle_group = VGroup()

        self.play(FadeOut(number_plane_1))

        circle_group.add(circ_main, dot_circ, line_circ, dot_center,
                    graph_upper, graph_lower,
                    radius_horiz, radius_horiz_end_dot, radius_ang, radius_ang_end_dot,
                    central_angle, central_angle_label,
                    small_tangent, small_tangent_end_dot ,
                    dot_circ_copy, dropped_dot, dropped_perp, radius_horiz_ext,
                    ptA, ptB, ptC, ptD, ptE)
        
        # self.play(circle_group.animate.shift(LEFT*5))
    
    def cameraRestoring(self):
        """ restore camera """
        self.play(Restore(self.camera.frame))

    def considerAreasText(self):
        """ text for Consider the following areas """
        global consider_area_text
        consider_area_text = MathTex("\\text{Consider the following areas:}").scale(0.8).shift(RIGHT*3.55)

        self.play(Write(consider_area_text))
        self.play(consider_area_text.animate.to_edge(UP))
    
    def areasShaded(self):
        """ outline and move shaded shapes """
        global area_ABE
        area_ABE = always_redraw(
            lambda : Polygon(dot_center.get_center(), radius_ang_end_dot.get_center(), dropped_dot.get_center(),
                        color=PINK, fill_color=PINK, fill_opacity=0.5)
        )
        global area_ABE_copy
        area_ABE_copy = area_ABE.copy()

        self.play(Write(area_ABE))
        self.wait(0.5)
        self.play(area_ABE_copy.animate.move_to(consider_area_text.get_center()+DOWN*1.5+LEFT*1.5))

        global area_ABD
        area_ABD = always_redraw(
            lambda : Sector(outer_radius=self.x_max, start_angle=0, angle=theta.get_value()*DEGREES,
                            stroke_width=DEFAULT_STROKE_WIDTH , stroke_color=BLUE, color=BLUE, fill_opacity=0.5).shift(LEFT*5)
        )
        global area_ABD_copy
        area_ABD_copy = area_ABD.copy()

        self.play(Write(area_ABD))
        self.wait(0.5)
        self.play(area_ABD_copy.animate.move_to(consider_area_text.get_center()+DOWN*1.5+RIGHT*1.5))

        global area_ABC
        area_ABC = always_redraw(
            lambda : Polygon(dot_center.get_center(), radius_ang_end_dot.get_center(), small_tangent_end_dot.get_center(),
                        color=GREEN, fill_color=GREEN, fill_opacity=0.5)
        )
        global area_ABC_copy
        area_ABC_copy = area_ABC.copy()

        self.play(Write(area_ABC))
        self.wait(0.5)
        self.play(area_ABC_copy.animate.move_to(consider_area_text.get_center()+DOWN*3.5))

        self.play(FadeOut(consider_area_text))
    
    def compareAreas(self):
        """ areas are less than the other area """
        self.play(area_ABE_copy.animate.move_to(RIGHT*2).scale(0.5),
                area_ABD_copy.animate.move_to(RIGHT*3.45).scale(0.5),
                area_ABC_copy.animate.move_to(RIGHT*5.3).scale(0.5))
        
        global geq_1, geq_2
        geq_1 = always_redraw(
            lambda : MathTex("\\text{<}").scale(0.8).next_to(area_ABE_copy, RIGHT*0.75)
        )
        geq_2 = always_redraw(
            lambda : MathTex("\\text{<}").scale(0.8).next_to(area_ABD_copy, RIGHT*0.5)
        )

        self.play(Write(geq_1), Write(geq_2))
        self.wait(0.5)
    
    def explainAreaSmall(self):
        """ explain definitions of triangle ABE """
        
        #EXPLANATION NO. 1
        #fadeout the non-required areas
        self.play(FadeOut(area_ABC_copy), FadeOut(area_ABD_copy),
                FadeOut(geq_2), FadeOut(geq_1),
                FadeOut(area_ABC), FadeOut(area_ABD))
        
        #expand the required area
        self.play(area_ABE_copy.animate.scale(2).move_to(RIGHT*2))

        #surrounding text
        abe_text_1 = always_redraw(
            lambda : MathTex("=", "\\text{Area of } \\triangle ABE").scale(0.8).next_to(area_ABE_copy, RIGHT)
        )

        #half base height
        abe_text_2 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\times", "\\text{base}", "\\times", "\\text{height}").scale(0.8).next_to(area_ABE_copy, RIGHT)
        )

        #write texts
        self.play(Write(abe_text_1))
        self.wait()
        self.play(ReplacementTransform(abe_text_1[0], abe_text_2[0]),
                ReplacementTransform(abe_text_1[1:], abe_text_2[1:]))
        self.wait()

        #defining braces
        abe_base_brace = always_redraw(
            lambda : Brace(radius_ang, DOWN)
        )
        abe_base_brace_label = always_redraw(
            lambda : MathTex("R\\cos\\theta").scale(0.6).next_to(abe_base_brace, DOWN)
        )
        abe_height_brace = always_redraw(
            lambda : Brace(radius_ang, LEFT)
        )
        abe_height_brace_label = always_redraw(
            lambda : MathTex("R\\sin\\theta").scale(0.6).next_to(abe_height_brace, LEFT)
        )

        self.play(Write(abe_base_brace), Write(abe_height_brace))
        self.play(Write(abe_base_brace_label), Write(abe_height_brace_label))
        self.wait()

        
        #back to editing the equation
        abe_text_3 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\times", "R\\cos\\theta", "\\times", "R\\sin\\theta").scale(0.8).next_to(area_ABE_copy, RIGHT)
        )

        self.play(ReplacementTransform(abe_text_2[0:], abe_text_3[0:]))
        self.wait(0.5)
        self.play(FadeOut(abe_base_brace), FadeOut(abe_height_brace),
                FadeOut(abe_base_brace_label), FadeOut(abe_height_brace_label))
        
        abe_text_4 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\times", "\\cos x", "\\times", "\\sin x").scale(0.8).next_to(area_ABE_copy, RIGHT)
        )
        self.play(ReplacementTransform(abe_text_3[0:], abe_text_4[0:]))

        abe_text_5 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\sin x", "\\cos x").scale(0.8).next_to(area_ABE_copy, RIGHT)
        )
        self.play(ReplacementTransform(abe_text_4[0:2], abe_text_5[0:2]),
                ReplacementTransform(abe_text_4[2:], abe_text_5[2:]))

        #vgroup for drawing box
        abe_group = VGroup(abe_text_5, area_ABE_copy)
        abe_formula_box = SurroundingRectangle(abe_group, color=PINK)

        self.play(Write(abe_formula_box))
        self.wait()

        #remove all elements
        self.play(FadeOut(abe_formula_box), FadeOut(abe_text_5), FadeOut(area_ABE_copy), FadeOut(area_ABE))
    
    def explainAreaMedium(self):
        #add required elements
        self.play(Write(area_ABD), FadeIn(area_ABD_copy))

        #scale up representative figure for equation
        self.play(area_ABD_copy.animate.scale(2).move_to(RIGHT*2))

        abd_text_1 = always_redraw(
            lambda : MathTex("=", "\\text{Area of sector } ABD").scale(0.7).next_to(area_ABD_copy, RIGHT)
        )

        abd_text_2 = always_redraw(
            lambda : MathTex("=", "{\\theta", "\\over", "2\\pi}", "\\times", "\\pi R^2").scale(0.8).next_to(area_ABD_copy, RIGHT)
        )

        self.play(Write(abd_text_1))
        self.wait()
        self.play(ReplacementTransform(abd_text_1[0], abd_text_2[0]),
                ReplacementTransform(abd_text_1[1:], abd_text_2[1:]))
        self.wait()

        self.play(Write(horiz_brace), Write(angular_brace))
        self.play(Write(horiz_brace_label), Write(angular_brace_label))

        self.wait()

        self.play(FadeOut(horiz_brace), FadeOut(horiz_brace_label),
                FadeOut(angular_brace), FadeOut(angular_brace_label))
        
        abd_text_3 = always_redraw(
            lambda : MathTex("=", "{x", "\\over", "2\\pi}", "\\times", "\\pi").scale(0.8).next_to(area_ABD_copy, RIGHT)
        )

        self.play(ReplacementTransform(abd_text_2[0], abd_text_3[0]),
                ReplacementTransform(abd_text_2[1], abd_text_3[1]),
                ReplacementTransform(abd_text_2[2:4], abd_text_3[2:4]),
                ReplacementTransform(abd_text_2[4], abd_text_3[4]),
                ReplacementTransform(abd_text_2[5], abd_text_3[5]))
        self.wait()

        abd_text_4 = always_redraw(
            lambda : MathTex("=", "{x", "\\over", "2}").scale(0.8).next_to(area_ABD_copy, RIGHT)
        )

        self.play(ReplacementTransform(abd_text_3[0:3], abd_text_4[0:3]),
                ReplacementTransform(abd_text_3[3:], abd_text_4[3]),)
        
        abd_group = VGroup(area_ABD_copy, abd_text_4)
        abd_formula_box = SurroundingRectangle(abd_group, color=BLUE)

        self.play(Write(abd_formula_box))
        self.wait()

        #remove all elements
        self.play(FadeOut(abd_formula_box), FadeOut(abd_text_4), FadeOut(area_ABD_copy), FadeOut(area_ABD))
    
    def explainAreaLarge(self):
        self.play(Write(area_ABC), FadeIn(area_ABC_copy))

        self.play(area_ABC_copy.animate.move_to(RIGHT))

        abc_text_1 = always_redraw(
            lambda : MathTex("=", "\\text{Area of } \\triangle ABC").scale(0.8).next_to(area_ABC_copy, RIGHT)
        )
        
        abc_text_2 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "(AB)", "(BC)", "(\\sin", "C)").scale(0.8).next_to(area_ABC_copy, RIGHT)
        )

        self.play(Write(abc_text_1))
        
        self.wait()
        self.play(ReplacementTransform(abc_text_1[0], abc_text_2[0]),
                (ReplacementTransform(abc_text_1[1:], abc_text_2[1:])))
        self.wait()

        abc_text_3 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\text{(radius)}", "(\\tan x)", "(\\sin", "90^\\circ)").scale(0.8).next_to(area_ABC_copy, RIGHT)
        )

        self.play(ReplacementTransform(abc_text_2[0:], abc_text_3[0:]))
        self.wait()

        abc_text_4 = always_redraw(
            lambda : MathTex("=", "\\dfrac{1}{2}", "\\tan x").scale(0.8).next_to(area_ABC_copy, RIGHT)
        )

        self.play(ReplacementTransform(abc_text_3[0], abc_text_4[0]),
                ReplacementTransform(abc_text_3[1], abc_text_4[1]),
                ReplacementTransform(abc_text_3[2:], abc_text_4[2]),)
        self.wait()

        abc_group = VGroup(abc_text_4, area_ABC_copy)
        abc_formula_box = SurroundingRectangle(abc_group, color=GREEN)

        self.play(Write(abc_formula_box))
        self.wait()

        #remove all elements
        self.play(FadeOut(abc_formula_box), FadeOut(abc_text_4), FadeOut(area_ABC_copy), FadeOut(area_ABC))

    def fadeEverything(self):
        self.play(FadeOut(circle_group))

        area_ABE_copy.move_to(LEFT*2)

        area_ABD_copy.move_to(ORIGIN)

        area_ABC_copy.move_to(RIGHT*3.5)
        area_ABC_copy.scale(2)

        sign1 = MathTex("\\text{<}").next_to(area_ABE_copy, RIGHT)
        sign2 = MathTex("\\text{<}").next_to(area_ABD_copy, RIGHT)

        final_group = VGroup(area_ABE_copy, area_ABD_copy, area_ABC_copy,
                    sign1, sign2)
        final_group.move_to(ORIGIN)

        self.play(Write(area_ABE_copy), Write(area_ABD_copy), Write(area_ABC_copy))
        self.play(Write(sign1), Write(sign2))
        self.wait(1.5)

        final_eq_1 = MathTex("{1", "\\over", "2}", "\\sin x", "\\cos x", "\\leq",
                        "{1", "\\over", "2}", "x", "\\leq",
                        "{1", "\\over", "2}", "\\tan x")
        self.play(ReplacementTransform(final_group, final_eq_1))
        self.wait()

        final_eq_2 = MathTex("\\sin x", "\\cos x", "\\leq", "x", "\\leq", "{\\sin x", "\\over", "\\cos x}")

        self.play(ReplacementTransform(final_eq_1[0:4], final_eq_2[0]),
                ReplacementTransform(final_eq_1[4:6], final_eq_2[1:3]),
                ReplacementTransform(final_eq_1[6:10], final_eq_2[3]),
                ReplacementTransform(final_eq_1[10], final_eq_2[4]),
                ReplacementTransform(final_eq_1[11:15], final_eq_2[5:]),)
        self.wait()

        final_eq_3 = MathTex("\\cos x", "\\leq", "{x", "\\over", "\\sin x}", "\\leq", "{1", "\\over", "\\cos x}")

        self.play(ReplacementTransform(final_eq_2[0], final_eq_3[4]),
                ReplacementTransform(final_eq_2[1], final_eq_3[0]),
                ReplacementTransform(final_eq_2[2], final_eq_3[1]),
                ReplacementTransform(final_eq_2[3], final_eq_3[2]),
                ReplacementTransform(final_eq_2[4:], final_eq_3[5:]))
        self.play(Write(final_eq_3[3]))