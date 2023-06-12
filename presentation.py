# flake8: noqa: F403, F405
# type: ignore
import sys

if "manim" in sys.modules:
    print("DADA"*10)
    from manim import *

    MANIMGL = False
elif "manimlib" in sys.modules:
    print("DEBE"*10)
    from manimlib import *

    MANIMGL = True
else:
    raise ImportError("This script must be run with either `manim` or `manimgl`")

from manim_slides import Slide, ThreeDSlide


def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result

class MerkleTree:
    def __init__(self, scene, num_nodes=4):
        self.scene = scene
        self.num_nodes = num_nodes

    def create(self):
        self.nodes = [RoundedRectangle(corner_radius=0.5) for _ in range(self.num_nodes)]

        for node in self.nodes:
            self.scene.play(GrowFromCenter(node))


class Presentation(Slide):
    def construct(self):
        # merkle_tree = MerkleTree(self, 1)
        # merkle_tree.create()

        left = RoundedRectangle(corner_radius=0.2, width=1.5, height=1)
        left.move_to([-3, -3, 0])

        right = RoundedRectangle(corner_radius=0.2, width=1.5, height=1)
        right.move_to([3, -3, 0])

        dad_left = RoundedRectangle(corner_radius=0.2, width=1.5, height=1)
        dad_left.move_to([0,0,0])
        dad = RoundedRectangle(corner_radius=0.2, width=1.5, height=1)
        dad.move_to([0,0,0])

        # p = Dot()
        # self.play(GrowFromCenter(p))

        self.play(GrowFromCenter(left), GrowFromCenter(right))


        # arrow_right = Arrow(start=[3, -2.7, 0], end=[0,-0.4,0])
        # arrow_left = Arrow(start=[-3, -2.7, 0], end=[0,-0.4,0])
        arrow_right = Arrow(right, dad)
        arrow_left = Arrow(left, dad)

        self.play(TransformFromCopy(right, dad), TransformFromCopy(left, dad_left), GrowArrow(arrow_right), GrowArrow(arrow_left))
        # self.play(DrawBorderThenFill(arrow_right), DrawBorderThenFill(arrow_left))

        self.remove(dad_left)     

        self.play(Indicate(dad))
        
        self.wait()
        # # create text box

        # textbox = create_textbox(color=BLUE, string="Hello world")
        # self.add(textbox)

        # # move text box around
        # self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        # self.play(textbox.animate.shift(2*UP), run_time=3)
        # self.wait()


# class MultipleAnimationsInLastSlide(Slide):
#     """This is used to check against solution for issue #161."""
# 
#     def construct(self):
#         circle = Circle(color=BLUE)
#         dot = Dot()
# 
#         self.play(GrowFromCenter(circle))
#         self.play(FadeIn(dot))
#         self.next_slide()
# 
#         self.play(dot.animate.move_to(RIGHT))
#         self.play(dot.animate.move_to(UP))
#         self.play(dot.animate.move_to(LEFT))
#         self.play(dot.animate.move_to(DOWN))
# 
#         self.next_slide()
# 
# 
# class TestFileTooLong(Slide):
#     """This is used to check against solution for issue #123."""
# 
#     def construct(self):
#         import random
# 
#         circle = Circle(radius=3, color=BLUE)
#         dot = Dot()
#         self.play(GrowFromCenter(circle), run_time=0.1)
# 
#         for _ in range(30):
#             direction = (random.random() - 0.5) * LEFT + (random.random() - 0.5) * UP
#             self.play(dot.animate.move_to(direction), run_time=0.1)
#             self.play(dot.animate.move_to(ORIGIN), run_time=0.1)
# 
#         self.next_slide()
# 
# 
# class ConvertExample(Slide):
#     """WARNING: this example does not seem to work with ManimGL."""
# 
#     def tinywait(self):
#         self.wait(0.1)
# 
#     def construct(self):
#         title = VGroup(
#             Text("From Manim animations", t2c={"From": BLUE}),
#             Text("to slides presentation", t2c={"to": BLUE}),
#             Text("with Manim Slides", t2w={"[-12:]": BOLD}, t2c={"[-13:]": YELLOW}),
#         ).arrange(DOWN)
# 
#         step_1 = Text("1. In your scenes file, import Manim Slides")
#         step_2 = Text("2. Replace Scene with Slide")
#         step_3 = Text("3. In construct, add pauses where you need")
#         step_4 = Text("4. You can also create loops")
#         step_5 = Text("5. Render you scene with Manim")
#         step_6 = Text("6. Open your presentation with Manim Slides")
# 
#         for step in [step_1, step_2, step_3, step_4, step_5, step_6]:
#             step.scale(0.5).to_corner(UL)
# 
#         step = step_1
# 
#         self.play(FadeIn(title))
# 
#         self.next_slide()
# 
#         code = Code(
#             code="""from manim import *
# 
# 
# class Example(Scene):
#     def construct(self):
#         dot = Dot()
#         self.add(dot)
# 
#         self.play(Indicate(dot, scale_factor=2))
# 
#         square = Square()
#         self.play(Transform(dot, square))
# 
#         self.play(Rotate(square, angle=PI/2))
# """,
#             language="python",
#         )
# 
#         code_step_1 = Code(
#             code="""from manim import *
# from manim_slides import Slide
# 
# class Example(Scene):
#     def construct(self):
#         dot = Dot()
#         self.add(dot)
# 
#         self.play(Indicate(dot, scale_factor=2))
# 
#         square = Square()
#         self.play(Transform(dot, square))
# 
#         self.play(Rotate(square, angle=PI/2))
# """,
#             language="python",
#         )
# 
#         code_step_2 = Code(
#             code="""from manim import *
# from manim_slides import Slide
# 
# class Example(Slide):
#     def construct(self):
#         dot = Dot()
#         self.add(dot)
# 
#         self.play(Indicate(dot, scale_factor=2))
# 
#         square = Square()
#         self.play(Transform(dot, square))
# 
#         self.play(Rotate(square, angle=PI/2))
# """,
#             language="python",
#         )
# 
#         code_step_3 = Code(
#             code="""from manim import *
# from manim_slides import Slide
# 
# class Example(Slide):
#     def construct(self):
#         dot = Dot()
#         self.add(dot)
# 
#         self.play(Indicate(dot, scale_factor=2))
#         self.next_slide()
#         square = Square()
#         self.play(Transform(dot, square))
#         self.next_slide()
#         self.play(Rotate(square, angle=PI/2))
# """,
#             language="python",
#         )
# 
#         code_step_4 = Code(
#             code="""from manim import *
# from manim_slides import Slide
# 
# class Example(Slide):
#     def construct(self):
#         dot = Dot()
#         self.add(dot)
#         self.start_loop()
#         self.play(Indicate(dot, scale_factor=2))
#         self.end_loop()
#         square = Square()
#         self.play(Transform(dot, square))
#         self.next_slide()
#         self.play(Rotate(square, angle=PI/2))
# """,
#             language="python",
#         )
# 
#         code_step_5 = Code(
#             code="manim example.py Example",
#             language="console",
#         )
# 
#         code_step_6 = Code(
#             code="manim-slides Example",
#             language="console",
#         )
# 
#         or_text = Text("or generate HTML presentation").scale(0.5)
# 
#         code_step_7 = Code(
#             code="manim-slides convert Example slides.html --open",
#             language="console",
#         ).shift(DOWN)
# 
#         self.clear()
# 
#         self.play(FadeIn(code))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(FadeIn(step, shift=RIGHT))
#         self.play(Transform(code, code_step_1))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(Transform(step, step_2))
#         self.play(Transform(code, code_step_2))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(Transform(step, step_3))
#         self.play(Transform(code, code_step_3))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(Transform(step, step_4))
#         self.play(Transform(code, code_step_4))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(Transform(step, step_5))
#         self.play(Transform(code, code_step_5))
#         self.tinywait()
#         self.next_slide()
# 
#         self.play(Transform(step, step_6))
#         self.play(Transform(code, code_step_6))
#         self.play(code.animate.shift(UP), FadeIn(code_step_7), FadeIn(or_text))
#         self.tinywait()
#         self.next_slide()
# 
#         watch_text = Text("Watch result on next slides!").shift(2 * DOWN).scale(0.5)
# 
#         self.start_loop()
#         self.play(FadeIn(watch_text))
#         self.play(FadeOut(watch_text))
#         self.end_loop()
#         self.clear()
# 
#         dot = Dot()
#         self.add(dot)
#         self.start_loop()
#         self.play(Indicate(dot, scale_factor=2))
#         self.end_loop()
#         square = Square()
#         self.play(Transform(dot, square))
#         self.remove(dot)
#         self.add(square)
#         self.tinywait()
#         self.next_slide()
#         self.play(Rotate(square, angle=PI / 4))
#         self.tinywait()
#         self.next_slide()
# 
#         learn_more_text = (
#             VGroup(
#                 Text("Learn more about Manim Slides:"),
#                 Text("https://github.com/jeertmans/manim-slides", color=YELLOW),
#             )
#             .arrange(DOWN)
#             .scale(0.75)
#         )
# 
#         self.play(Transform(square, learn_more_text))
#         self.tinywait()
# 
# 
# # For ThreeDExample, things are different
# 
# if not MANIMGL:
#     # [manim-3d]
#     class ThreeDExample(ThreeDSlide):
#         def construct(self):
#             axes = ThreeDAxes()
#             circle = Circle(radius=3, color=BLUE)
#             dot = Dot(color=RED)
# 
#             self.add(axes)
# 
#             self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
# 
#             self.play(GrowFromCenter(circle))
#             self.begin_ambient_camera_rotation(rate=75 * DEGREES / 4)
# 
#             self.next_slide()
# 
#             self.start_loop()
#             self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
#             self.end_loop()
# 
#             self.stop_ambient_camera_rotation()
#             self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
# 
#             self.play(dot.animate.move_to(ORIGIN))
#             self.next_slide()
# 
#             self.play(dot.animate.move_to(RIGHT * 3))
#             self.next_slide()
# 
#             self.start_loop()
#             self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#             self.end_loop()
# 
#             self.play(dot.animate.move_to(ORIGIN))
# 
#     # [manim-3d]
# else:
#     # [manimgl-3d]
#     # WARNING: 3b1b's manim change how ThreeDScene work,
#     # this is why things have to be managed differently.
#     class ThreeDExample(Slide):
#         CONFIG = {
#             "camera_class": ThreeDCamera,
#         }
# 
#         def construct(self):
#             axes = ThreeDAxes()
#             circle = Circle(radius=3, color=BLUE)
#             dot = Dot(color=RED)
# 
#             self.add(axes)
# 
#             frame = self.camera.frame
#             frame.set_euler_angles(
#                 theta=30 * DEGREES,
#                 phi=75 * DEGREES,
#                 gamma=0,
#             )
# 
#             self.play(GrowFromCenter(circle))
#             updater = lambda m, dt: m.increment_theta((75 * DEGREES / 4) * dt)
#             frame.add_updater(updater)
# 
#             self.next_slide()
# 
#             self.start_loop()
#             self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
#             self.end_loop()
# 
#             frame.remove_updater(updater)
#             self.play(frame.animate.set_theta(30 * DEGREES))
#             self.play(dot.animate.move_to(ORIGIN))
#             self.next_slide()
# 
#             self.play(dot.animate.move_to(RIGHT * 3))
#             self.next_slide()
# 
#             self.start_loop()
#             self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#             self.end_loop()
# 
#             self.play(dot.animate.move_to(ORIGIN))
# 
#     # [manimgl-3d]
