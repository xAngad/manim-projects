from manim import *
import numpy as np

""" Equation of curve """
def f(x):
    return (np.power(x, 2) + 1)

""" Constants """
lower = 0
upper = 3

class riemannSum(GraphScene):
    def setup(self):
        GraphScene.setup(self)
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            graph_origin = LEFT * 5 + DOWN * 3,
            x_min = -1,
            x_max = 4,
            x_axis_width = 6,
            x_axis_label = "",
            x_axis_config = {"include_tip": True},
            x_labeled_nums = [0, 1, 2, 3],
            y_min = 0,
            y_max = 10,
            y_axis_height = 6,
            y_axis_label = "",
            y_axis_config = {"include_tip": True},
            y_labeled_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            num_rects=100,
            **kwargs
        )
    
    def construct(self):
        self.drawGraph()
        self.previewRiemann()
        self.showAreas()
        self.tableValues()

    def drawGraph(self):
        """ Axes and graph definition """
        self.setup_axes()
        global graph_main
        graph_main = self.get_graph(f, color=RED, x_min=-0.5, x_max=3.1)

        self.add(self.axes)
        self.add(graph_main)
        # self.play(Write(graph_main))


    def previewRiemann(self):
        """ Show vertical lines and actual area """
        line_1 = self.get_vertical_line_to_graph(lower, graph_main, DashedLine, color=GOLD)
        line_2 = self.get_vertical_line_to_graph(upper, graph_main, DashedLine, color=GOLD)
        area_full_preview = self.get_area(graph_main, t_min = lower, t_max = upper, dx_scaling=0.5, area_color=RED_A)

        self.play(Write(line_1), Write(line_2))
        self.play(Write(area_full_preview))
        
        """ Show n riemann rectangles to explain the process """
        global text_preview_1
        text_preview_1 = MathTex("\\text{The shaded ", "area", " can be approximated}").scale(0.75).shift(RIGHT*3.25+UP*0.25)
        f_always(text_preview_1[1].set_color, lambda : RED_A)
        global text_preview_2
        text_preview_2 = always_redraw(
            lambda : MathTex("\\text{by constructing rectangles of width }", "\\Delta x").scale(0.75).next_to(text_preview_1, DOWN)
        )
        area_preview = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/8, input_sample_type="left", stroke_width=0.1)

        self.play(Write(text_preview_1), Write(text_preview_2))
        self.wait()
        self.play(text_preview_1.animate.to_edge(UP), FadeOut(area_full_preview), FadeIn(area_preview))
        self.wait()

        """ Brace delta x """
        delta_brace = Brace(area_preview[0], DOWN, buff=0.15)
        delta_brace_label = always_redraw(
            lambda : MathTex("\\Delta x").scale(0.5).next_to(delta_brace, DOWN, buff=0.1)
        )
        self.play(Write(delta_brace), Write(delta_brace_label))
        self.wait()
        # self.play(delta_brace.animate.become(Brace(area_preview[1], DOWN, buff=0.15)))
        for i in range(1, len(area_preview)):
            self.play(delta_brace.animate.become(Brace(area_preview[i], DOWN, buff=0.15)), run_time=0.5)
        self.play(FadeOut(delta_brace_label), FadeOut(delta_brace))
        self.play(FadeOut(area_preview))

    
    def showAreas(self):
        """ Area #1 : 1 rectangle """
        # Rectangle
        area_1 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/1, input_sample_type="left", stroke_width=0)
        
        # Copy, width, and height
        area_1_copy = area_1.copy()
        width_brace_1 = Brace(area_1, DOWN, buff=0.1)
        width_label_1 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_1, DOWN)
        height_brace_1 = Brace(area_1, RIGHT, buff=0.1)
        height_label_1 = MathTex("h").scale(0.5).next_to(height_brace_1, RIGHT)
        
        # Explanation
        area_1_text = MathTex("\\text{Area}", "=").scale(0.75).shift(RIGHT*3.25)
        area_1_text_1 = MathTex("\\Delta x", "\\times", "h").scale(0.75).next_to(area_1_text, RIGHT)
        area_1_text_2 = MathTex("3", "\\times", "1").scale(0.75).next_to(area_1_text, RIGHT)
        area_1_text_3 = MathTex("3").scale(0.75).next_to(area_1_text, RIGHT)
        no_of_tris_1 = MathTex("\\text{Number of rectangles: }", 1).scale(0.8).next_to(area_1_text, UP, buff = 1.5)

        self.play(Write(area_1),
                Write(width_brace_1), Write(width_label_1),
                Write(height_brace_1), Write(height_label_1))
        self.play(Write(area_1_text), Write(no_of_tris_1))
        self.play(area_1_copy.animate.move_to(RIGHT*5).scale(0.5))
        self.wait()
        self.play(ReplacementTransform(area_1_copy, area_1_text_1),
                FadeOut(width_brace_1), FadeOut(width_label_1),
                FadeOut(height_brace_1), FadeOut(height_label_1))
        self.wait()
        self.play(ReplacementTransform(area_1_text_1, area_1_text_2))
        self.wait()
        self.play(ReplacementTransform(area_1_text_2, area_1_text_3))
        self.play(Flash(area_1_text_3, flash_radius=0.2))
        self.wait(0.5)
        self.play(FadeOut(area_1_text_3))

        """ Area #2 : 2 rectangles """
        # Rectangles
        area_2 = self.get_riemann_rectangles(graph_main, 0, 3, dx=1.5, input_sample_type="left", stroke_width=0)

        # Copy
        area_2_copy = area_2.copy()

        # Width braces
        width_brace_2_1 = Brace(area_2[0], DOWN, buff=0.1)
        width_label_2_1 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_2_1, DOWN)
        width_brace_2_2 = Brace(area_2[1], DOWN, buff=0.1)
        width_label_2_2 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_2_2, DOWN)
        
        # Height braces
        height_brace_2_1 = Brace(area_2[0], RIGHT, buff=0.1)
        height_label_2_1 = MathTex("h_1").scale(0.5).next_to(height_brace_2_1, RIGHT)
        height_brace_2_2 = Brace(area_2[1], RIGHT, buff=0.1)
        height_label_2_2 = MathTex("h_2").scale(0.5).next_to(height_brace_2_2, RIGHT)

        #Explanation
        area_2_text_1 = MathTex("\\Delta x", "\\times", "h_1", "\\\\", "+", "\\Delta x", "\\times", "h_2").scale(0.75).next_to(area_1_text, RIGHT)
        area_2_text_2 = MathTex("1.5", "\\times", "1", "\\\\", "+", "1.5", "\\times", "3.25").scale(0.75).next_to(area_1_text, RIGHT)
        area_2_text_3 = MathTex("1.5", "\\\\", "+", "4.875").scale(0.75).next_to(area_1_text, RIGHT)
        area_2_text_4 = MathTex("6.375").scale(0.75).next_to(area_1_text, RIGHT)
        no_of_tris_2 = MathTex("\\text{Number of rectangles: }", 2).scale(0.8).next_to(area_1_text, UP, buff = 1.5)
        

        self.play(ReplacementTransform(area_1, area_2), ReplacementTransform(no_of_tris_1, no_of_tris_2))
        self.play(Write(width_brace_2_1), Write(width_brace_2_2), Write(width_label_2_1), Write(width_label_2_2),
                Write(height_brace_2_1), Write(height_brace_2_2), Write(height_label_2_1), Write(height_label_2_2))
        self.play(area_2_copy.animate.move_to(RIGHT*5).scale(0.4))
        self.wait()
        self.play(ReplacementTransform(area_2_copy, area_2_text_1),
                FadeOut(width_brace_2_1), FadeOut(width_brace_2_2), FadeOut(width_label_2_1), FadeOut(width_label_2_2),
                FadeOut(height_brace_2_1), FadeOut(height_brace_2_2), FadeOut(height_label_2_1),FadeOut(height_label_2_2))
        self.wait()
        self.play(ReplacementTransform(area_2_text_1, area_2_text_2))
        self.wait()
        self.play(ReplacementTransform(area_2_text_2, area_2_text_3))
        self.wait()
        self.play(ReplacementTransform(area_2_text_3, area_2_text_4))
        self.wait()
        self.play(Flash(area_2_text_4, flash_radius=0.4))
        self.wait(0.5)
        self.play(FadeOut(area_2_text_4))
        
        """ Area #3 : 4 rectangles """
        area_3 = self.get_riemann_rectangles(graph_main, 0, 3, dx=1, input_sample_type="left", stroke_width=0)

        # Copy
        area_3_copy = area_3.copy()

        # Width braces
        width_brace_3_1 = Brace(area_3[0], DOWN, buff=0.1)
        width_label_3_1 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_3_1, DOWN)
        width_brace_3_2 = Brace(area_3[1], DOWN, buff=0.1)
        width_label_3_2 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_3_2, DOWN)
        width_brace_3_3 = Brace(area_3[2], DOWN, buff=0.1)
        width_label_3_3 = MathTex("\\Delta x").scale(0.5).next_to(width_brace_3_3, DOWN)
        
        # Height braces
        height_brace_3_1 = Brace(area_3[0], RIGHT, buff=0.1)
        height_label_3_1 = MathTex("h_1").scale(0.5).next_to(height_brace_3_1, RIGHT)
        height_brace_3_2 = Brace(area_3[1], RIGHT, buff=0.1)
        height_label_3_2 = MathTex("h_2").scale(0.5).next_to(height_brace_3_2, RIGHT)
        height_brace_3_3 = Brace(area_3[2], RIGHT, buff=0.1)
        height_label_3_3 = MathTex("h_3").scale(0.5).next_to(height_brace_3_3, RIGHT)

        #Explanation
        area_3_text_1 = MathTex("\\Delta x", "\\times", "h_1", "\\\\",
                            "+", "\\Delta x", "\\times", "h_2", "\\\\",
                            "+", "\\Delta x", "\\times", "h_3").scale(0.75).next_to(area_1_text, RIGHT)
        area_3_text_2 = MathTex("1", "\\times", "1", "\\\\",
                            "+", "1", "\\times", "2", "\\\\",
                            "+", "1", "\\times", "5").scale(0.75).next_to(area_1_text, RIGHT)
        area_3_text_3 = MathTex("1", "\\\\",
                            "+", "2", "\\\\",
                            "+", "5").scale(0.75).next_to(area_1_text, RIGHT)
        area_3_text_4 = MathTex("8").scale(0.75).next_to(area_1_text, RIGHT)
        no_of_tris_3 = MathTex("\\text{Number of rectangles: }", 3).scale(0.8).next_to(area_1_text, UP, buff = 1.5)
        

        self.play(ReplacementTransform(area_2, area_3), ReplacementTransform(no_of_tris_2, no_of_tris_3))
        self.play(Write(width_brace_3_1), Write(width_brace_3_2), Write(width_brace_3_3),
                Write(width_label_3_1), Write(width_label_3_2), Write(width_label_3_3),
                Write(height_brace_3_1), Write(height_brace_3_2), Write(height_brace_3_3),
                Write(height_label_3_1), Write(height_label_3_2), Write(height_label_3_3))
        self.play(area_3_copy.animate.move_to(RIGHT*5).scale(0.4))
        self.wait()
        self.play(ReplacementTransform(area_3_copy, area_3_text_1),
                FadeOut(width_brace_3_1), FadeOut(width_brace_3_2), FadeOut(width_brace_3_3),
                FadeOut(width_label_3_1), FadeOut(width_label_3_2), FadeOut(width_label_3_3),
                FadeOut(height_brace_3_1), FadeOut(height_brace_3_2), FadeOut(height_brace_3_3),
                FadeOut(height_label_3_1), FadeOut(height_label_3_2), FadeOut(height_label_3_3))
        self.wait()
        self.play(ReplacementTransform(area_3_text_1, area_3_text_2))
        self.wait()
        self.play(ReplacementTransform(area_3_text_2, area_3_text_3))
        self.wait()
        self.play(ReplacementTransform(area_3_text_3, area_3_text_4))
        self.wait()
        self.play(Flash(area_3_text_4, flash_radius=0.2))
        self.wait(0.5)
        self.play(FadeOut(area_3_text_4), FadeOut(area_1_text), FadeOut(text_preview_1), FadeOut(text_preview_2), FadeOut(area_3),
                FadeOut(no_of_tris_3))
    
    def tableValues(self):
        """ Making a table of values """
        num_cells = 28
        cells = VGroup()
        range_num_cells = range(num_cells)
        for i in range_num_cells:
            cell = Rectangle(height = 0.35, width = 0.7)
            cells.add(cell)
        
        cells.arrange_in_grid(buff = 0, cols = 2)
        cells.move_to(RIGHT*3.5)
        self.play(Write(cells), run_time=1.5)

        """ Title """
        table_title_1 = MathTex("\\text{As the number of rectangles increases,").scale(0.5).next_to(cells, UP, buff = 0.5)
        table_title_2 = MathTex("\\text{the approximation of area improves").scale(0.5).next_to(table_title_1, DOWN, buff = 0.125)

        self.play(Write(table_title_1), Write(table_title_2))

        """ Cell headers and left column values """
        col_1_head = MathTex("n").scale(0.5).move_to(cells[0].get_center())
        col_2_head = MathTex("\\text{Area}").scale(0.5).move_to(cells[1].get_center())

        n1 = MathTex("1").scale(0.5).move_to(cells[2].get_center())
        n2 = MathTex("2").scale(0.5).move_to(cells[4].get_center())
        n3 = MathTex("3").scale(0.5).move_to(cells[6].get_center())
        n4 = MathTex("4").scale(0.5).move_to(cells[8].get_center())
        n5 = MathTex("5").scale(0.5).move_to(cells[10].get_center())
        n6 = MathTex("6").scale(0.5).move_to(cells[12].get_center())
        n7 = MathTex("7").scale(0.5).move_to(cells[14].get_center())
        n8 = MathTex("8").scale(0.5).move_to(cells[16].get_center())
        n9 = MathTex("9").scale(0.5).move_to(cells[18].get_center())
        n10 = MathTex("10").scale(0.5).move_to(cells[20].get_center())
        n11 = MathTex("11").scale(0.5).move_to(cells[22].get_center())

        self.play(Write(col_1_head), Write(col_2_head))
        self.play(Write(n1), Write(n2), Write(n3), Write(n4), Write(n5), Write(n6),
                Write(n7), Write(n8), Write(n9), Write(n10), Write(n11))
        
        """ Area Values and rectangles """
        area1 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/1, input_sample_type="left", stroke_width=0)
        a1 = MathTex("3.00").scale(0.5).move_to(cells[3].get_center())

        area2 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/2, input_sample_type="left", stroke_width=0)
        a2 = MathTex("6.38").scale(0.5).move_to(cells[5].get_center())

        area3 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/3, input_sample_type="left", stroke_width=0)
        a3 = MathTex("8.00").scale(0.5).move_to(cells[7].get_center())

        area4 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/4, input_sample_type="left", stroke_width=0)
        a4 = MathTex("8.91").scale(0.5).move_to(cells[9].get_center())

        area5 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/5, input_sample_type="left", stroke_width=0)
        a5 = MathTex("9.48").scale(0.5).move_to(cells[11].get_center())

        area6 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/6, input_sample_type="left", stroke_width=0)
        a6 = MathTex("9.88").scale(0.5).move_to(cells[13].get_center())

        area7 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/7, input_sample_type="left", stroke_width=0)
        a7 = MathTex("10.16").scale(0.5).move_to(cells[15].get_center())

        area8 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/8, input_sample_type="left", stroke_width=0)
        a8 = MathTex("10.38").scale(0.5).move_to(cells[17].get_center())

        area9 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/9, input_sample_type="left", stroke_width=0)
        a9 = MathTex("10.56").scale(0.5).move_to(cells[19].get_center())

        area10 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/10, input_sample_type="left", stroke_width=0)
        a10 = MathTex("10.69").scale(0.5).move_to(cells[21].get_center())

        area11 = self.get_riemann_rectangles(graph_main, 0, 3, dx=(upper-lower)/11, input_sample_type="left", stroke_width=0)
        a11 = MathTex("10.81").scale(0.5).move_to(cells[23].get_center())

        self.play(Write(area1), Write(a1))
        self.wait()
        self.play(ReplacementTransform(area1, area2), Write(a2))
        self.wait()
        self.play(ReplacementTransform(area2, area3), Write(a3))
        self.wait()
        self.play(ReplacementTransform(area3, area4), Write(a4))
        self.wait()
        self.play(ReplacementTransform(area4, area5), Write(a5))
        self.wait()
        self.play(ReplacementTransform(area5, area6), Write(a6))
        self.wait()
        self.play(ReplacementTransform(area6, area7), Write(a7))
        self.wait()
        self.play(ReplacementTransform(area7, area8), Write(a8))
        self.wait()
        self.play(ReplacementTransform(area8, area9), Write(a9))
        self.wait()
        self.play(ReplacementTransform(area9, area10), Write(a10))
        self.wait()
        self.play(ReplacementTransform(area10, area11), Write(a11))
        self.wait()

        """ Last two rows """
        ndots = MathTex("\\vdots").scale(0.5).move_to(cells[24].get_center())
        adots = MathTex("\\vdots").scale(0.5).move_to(cells[25].get_center())
        
        global areainf
        areainf = self.get_area(graph_main, lower, upper)
        areainf.set_color_by_gradient([BLUE_B, GREEN_B])
        ninf = MathTex("\\infty").scale(0.5).move_to(cells[26].get_center())
        ainf = MathTex("12.00").scale(0.5).move_to(cells[27].get_center())
        
        self.play(Write(ndots), Write(adots))
        self.wait(0.5)
        self.play(ReplacementTransform(area11, areainf), Write(ninf), Write(ainf))
