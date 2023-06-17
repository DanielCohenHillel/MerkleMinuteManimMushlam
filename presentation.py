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


class Presentation(MovingCameraScene):
    def construct(self):
        # merkle_tree = MerkleTree(self, 1)
        # merkle_tree.create()
        dad_pos   = np.array([0, 2, 0])
        left_pos  = np.array([-3, -2, 0])
        right_pos = np.array([3, -2, 0])

        dad_dad_pos = np.array([3, 6, 0])
        dad_bro_pos = np.array([6, 2, 0])



        left = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, fill_opacity=1)
        left.move_to(left_pos)

        right = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, fill_opacity=1)
        right.move_to(right_pos)

        dad = RoundedRectangle(corner_radius=0.2, width=1.35, height=1.05, fill_opacity=1)
        dad.move_to(dad_pos)
        dad_left = dad.copy()

        dad_new = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, fill_opacity=1)
        dad_new.move_to(dad_pos)

        self.play(GrowFromCenter(left), GrowFromCenter(right))

        left_new = left.copy()
        right_new = right.copy()

        left_arrow = Arrow(left_pos, dad_pos, buff=0.85)
        right_arrow = Arrow(right_pos, dad_pos, buff=0.85)

        midpoint_precent = 0.9
        left_midpoint = left_pos + (dad_pos - left_pos) * midpoint_precent
        right_midpoint = right_pos + (dad_pos - right_pos) * midpoint_precent

        ag1 = AnimationGroup(left_new.animate.move_to(left_midpoint), right_new.animate.move_to(right_midpoint))
        ag2 = AnimationGroup(Transform(left_new, dad_left), Transform(right_new, dad))

        arrow_grow_ag = AnimationGroup(GrowArrow(left_arrow), GrowArrow(right_arrow), run_time=1.1)
        # ag3 = AnimationGroup(ag1, ag2)
        self.play(AnimationGroup(ag2, arrow_grow_ag, lag_ratio=0))
        # self.play(, rate_func=rate_functions.ease_out_sine, run_time=0.15)
        # self.play(left_new.animate.move_to(left_midpoint), right_new.animate.move_to(right_midpoint), rate_func=rate_functions.ease_in_sine, run_time=0.5)
        # self.play(Transform(left_new, dad_left), Transform(right_new, dad), rate_func=rate_functions.ease_out_sine, run_time=0.15)

        self.remove(dad_left)
        self.remove(left_new)
        self.remove(right_new)
        self.play(Transform(dad, dad_new), rate_func=rate_functions.ease_in_sine, run_time=0.2)
        self.play(Wiggle(dad_new))



        ### CAMERA CHANGE

        self.play(
            self.camera.frame.animate.move_to([4, 2, 0]).scale(1.5)
            )
        
        dad_dad = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, fill_opacity=1)
        dad_dad.move_to(dad_dad_pos)

        dad_bro = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, fill_opacity=1)
        dad_bro.move_to(dad_bro_pos)

        self.play(GrowFromCenter(dad_bro))

        dad_bro_new = dad_bro.copy()
        daddy_new = dad.copy()
        dad_dad_tmp = dad_dad.copy()

        dad_merge_ag = AnimationGroup(Transform(dad_bro_new, dad_dad), Transform(daddy_new, dad_dad_tmp))

        dad_left_arrow = Arrow(dad_pos, dad_dad_pos, buff=0.85)
        dad_right_arrow = Arrow(dad_bro_pos, dad_dad_pos, buff=0.85)
        dad_arrow_ag = AnimationGroup(GrowArrow(dad_left_arrow), GrowArrow(dad_right_arrow), run_time=1.1)


        self.play(AnimationGroup(dad_merge_ag, dad_arrow_ag, lag_ratio=0))

        self.play(Circumscribe(dad_dad))


        # self.play(Indicate(dad_new))

        # self.play(AnimationGroup(TransformFromCopy(left, dad), Transform(dad, dad_new)), lag_ratio=0.9)

        # self.play(TransformFromCopy(left, dad))
        # self.remove(dad_left)     
        # self.play(Indicate(dad))
        self.wait()


        # arrow_right = Arrow(start=[3, -2.7, 0], end=[0,-0.4,0])
        # arrow_left = Arrow(start=[-3, -2.7, 0], end=[0,-0.4,0])
        # arrow_right = Arrow(right, dad, buff=0)
        # arrow_left = Arrow(left, dad, buff=0)

        # self.play(TransformFromCopy(right, dad), TransformFromCopy(left, dad_left))
        # self.play(DrawBorderThenFill(arrow_right), DrawBorderThenFill(arrow_left))

        # # create text box

        # textbox = create_textbox(color=BLUE, string="Hello world")
        # self.add(textbox)

        # # move text box around
        # self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        # self.play(textbox.animate.shift(2*UP), run_time=3)
        # self.wait()

# def get_rect_left(rect):


class Buffers(MovingCameraScene):
    def merge_into_dad(self, left, right, text, font_size=DEFAULT_FONT_SIZE, dad_height=2, z_index=1, scaling=1, arrows_buff = 0.8): # -> dad, AnimationGroup
        left_pos = np.array(left.get_center())
        right_pos = np.array(right.get_center())
        dad_pos = (left_pos + right_pos)/2 + np.array([0, dad_height, 0])

        dad_text = MarkupText(text, color=GREY_E, font_size=font_size)
        dad_width_margin = 0.1
        dad_width = max(1, dad_text.width + dad_width_margin)

        dad = VGroup(
            RoundedRectangle(corner_radius=0.2, width=dad_width, height=1, fill_opacity=1, stroke_opacity=0),
            dad_text
        )
        dad.set_z_index(z_index)
        dad.move_to(dad_pos).scale(scaling)
        dad_tmp = dad.copy()

        left_arrow = Arrow(left.get_center(), dad_pos, buff=arrows_buff)
        right_arrow = Arrow(right.get_center(), dad_pos, buff=arrows_buff)
        left_arrow.set_z_index(z_index)
        right_arrow.set_z_index(z_index)

        merge_ag = AnimationGroup(TransformFromCopy(left, dad), TransformFromCopy(right, dad_tmp))
        arrows_ag = AnimationGroup(GrowArrow(left_arrow), GrowArrow(right_arrow))

        res_ag = AnimationGroup(AnimationGroup(merge_ag, arrows_ag), lag_ratio=0.25)
        res_ag = Succession(res_ag, FadeOut(dad_tmp, run_time=0.1))

        self.remove(dad_tmp)

        return dad, res_ag

    def create_buffer(self, texts, fill_color, stroke_color, text_color, title_text):
        roof_buf = 0.2
        left_buf = 0.1
        leaf_buf = 0.1
        leaf_width = 1
        leaves_buf_width = (leaf_width + leaf_buf) * len(texts) + leaf_buf
        buff_height = 1
        text_height_buf = 0.2
        leaves_buffer = RoundedRectangle(corner_radius=0.1, width=leaves_buf_width, height=buff_height + roof_buf, stroke_width=6, color=stroke_color)


        eff_leaf_width = leaf_width + leaf_buf
        leaves_arr = [
            VGroup(
                RoundedRectangle(corner_radius=0.2, width=leaf_width, height=buff_height, fill_opacity=1, stroke_opacity=0, color=fill_color),
                Text(text=texts[i], color=text_color),
                z_index=1
            )
            for i in range(int(leaves_buf_width // eff_leaf_width))
        ]
        for i, leaf in enumerate(leaves_arr):
            rect_left = -leaves_buf_width / 2
            leaf.move_to([rect_left + left_buf + leaf_width / 2 + i * eff_leaf_width, 0, 0])

        self.play(GrowFromCenter(leaves_buffer))

        title = Text(title_text, color=text_color, font_size=36)
        title.move_to([-leaves_buf_width/2 + title.width/2, -buff_height/2 - title.height/2 - text_height_buf, 0])

        self.play(AnimationGroup(*[GrowFromCenter(l)for l in leaves_arr], lag_ratio=0.15), Write(title))
        behind_leaves_arr = [
            leaf.copy().set_opacity(0.2).set_z_index(-1)
            for leaf in leaves_arr
        ]

        self.add(*behind_leaves_arr)

        leaves_vgroup = VGroup(*(leaves_arr + behind_leaves_arr + [leaves_buffer, title]))
        return leaves_vgroup, leaves_arr, behind_leaves_arr, leaves_buffer, title
        
    def explain(self, obj, text, color=RED, z_index=10, wait_time=1):
        old_z_index = obj.z_index
        obj.set_z_index(z_index)
        shade_background = Rectangle(width=1000, height=1000, fill_opacity=0.9, color=BLACK)
        shade_background.move_to([-50, 50, 0])
        shade_background.set_z_index(z_index-1)
        explain_text = Text(text, font_size=36, color=color)
        explain_text.next_to(obj)
        explain = VGroup(
            explain_text,
        ).set_z_index(z_index)
        self.play(FadeIn(shade_background), FadeIn(explain))
        self.wait(wait_time)
        self.play(FadeOut(shade_background), FadeOut(explain))
        obj.set_z_index(old_z_index)

    def explain_noanim(self, obj, text, color=RED, lag_ratio=2, center=False):
        obj.set_z_index(10)
        shade_background = Rectangle(width=1000, height=1000, fill_opacity=0.9, color=BLACK)
        shade_background.move_to([-50, 50, 0])
        shade_background.set_z_index(9)
        explain_text = Text(text, font_size=36, color=color)
        if center:
            explain_text.move_to(obj.get_center())
        else:
            explain_text.next_to(obj)
        explain = VGroup(
            explain_text,
        ).set_z_index(10)
        fadeins_ag = AnimationGroup(FadeIn(shade_background), FadeIn(explain))
        fadeouts_ag = AnimationGroup(FadeOut(shade_background), FadeOut(explain))

        return Succession(fadeins_ag, fadeouts_ag, lag_ratio=2.0)
    
    def end_credits(self, texts, color=WHITE, lag_ratio=7.0):
        shade_background = Rectangle(width=1000, height=1000, fill_opacity=0.9, color=BLACK)
        shade_background.move_to([-50, 50, 0])
        shade_background.set_z_index(9)
        credits_texts = []
        for text in texts:
            credits_texts.append(MarkupText(text, font_size=36, color=color))

        credits = VGroup(
            *credits_texts,
        ).arrange(DOWN).set_z_index(10)
        credits_ag = AnimationGroup(*[FadeIn(line) for line in credits], lag_ratio=0.75)
        fadeins_ag = AnimationGroup(FadeIn(shade_background), credits_ag)
        fadeouts_ag = AnimationGroup(FadeOut(shade_background), FadeOut(credits))

        return Succession(fadeins_ag, fadeouts_ag, lag_ratio=lag_ratio)
    
    def full_tree_construct(self):
        bufs_dist = 2.5

        leaves_texts = ['a', 'b']
        leaves_vgroup, _, _, _, _ = self.create_buffer(leaves_texts, GREEN_A, GREEN, GREEN_E, "leaves")
        self.play(leaves_vgroup.animate.move_to([-6 + leaves_vgroup.width/2,bufs_dist,0]).scale(0.8))

        proof_text = ['A', 'B']
        proof_vgroup, _, _, _, _ = self.create_buffer(proof_text, YELLOW_A, YELLOW, YELLOW_E, "proof")
        self.play(proof_vgroup.animate.move_to([-6 + proof_vgroup.width/2,0,0]).scale(0.8))

        struct_text = ['0', '0', '1']
        struct_vgroup, _, _, _, _ = self.create_buffer(struct_text, RED_A, RED, RED_E, "proof flags")
        self.play(struct_vgroup.animate.move_to([-6 + struct_vgroup.width/2,-bufs_dist,0]).scale(0.8))

        hashes_text = ['', '', '']
        hashes_vgroup, _, _, _, _ = self.create_buffer(hashes_text, GREY_D, GREY, GREY_C, "hashes")
        self.play(hashes_vgroup.animate.move_to([-6 + hashes_vgroup.width/2 + leaves_vgroup.width,bufs_dist,0]).scale(0.8))
        
        arrows_top_buf = 0.2
        leaves_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=GREEN)
        proof_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=YELLOW)
        bits_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=RED)

        arrows_start = np.array([-6 + 0.25, leaves_vgroup.height/2 + leaves_arrow.height/2 + arrows_top_buf, 0])
        bufs_dist_vec = np.array([0,bufs_dist,0])
        
        leaves_arrow.move_to(arrows_start + bufs_dist_vec)
        proof_arrow.move_to(arrows_start)
        bits_arrow.move_to(arrows_start - bufs_dist_vec)

        self.play(GrowArrow(leaves_arrow), GrowArrow(proof_arrow), GrowArrow(bits_arrow))
        leaves_hashes_xs = [i.get_center()[0] - i.width /2 for i in leaves_vgroup[:2]] + [i[0].get_center()[0] - i[0].width /2 for i in hashes_vgroup[:3]]
        
        # start creating the tree
        l2_left_left = leaves_vgroup[0]
        l2_left_right = proof_vgroup[0]

        def la_mtx(la, i):
            return la.animate.move_to([leaves_hashes_xs[i], la.get_center()[1], la.get_center()[2]])

        # self.play(l2_left_left.animate.move_to([0,-2,0]), leaves_arrow.animate.shift([1,0,0]))
        self.play(l2_left_left.animate.move_to([0,-2,0]), la_mtx(leaves_arrow, 1))
        
        # explain the bits before continueing
        self.explain(struct_vgroup[0], "Take from proof list")

        self.play(l2_left_right.animate.move_to([2,-2,0]), la_mtx(proof_arrow, 1), la_mtx(bits_arrow, 1))

        scaling=0.8
        arrows_buff = 0.5

        l1_left, l1_left_ag = self.merge_into_dad(l2_left_left, l2_left_right, "aA", scaling=scaling, arrows_buff=arrows_buff)
        self.play(l1_left_ag)
        hashes_0 = l1_left.copy().set_z_index(2)
        self.play(hashes_0.animate.move_to(hashes_vgroup[0]))

        l2_right_left = leaves_vgroup[1]
        l2_right_right = proof_vgroup[1]
        self.play(l2_right_left.animate.move_to([4,-2,0]), la_mtx(leaves_arrow, 2))

        self.explain(struct_vgroup[1], "Take from proof list")


        self.play(l2_right_right.animate.move_to([6,-2,0]), la_mtx(proof_arrow, 2), la_mtx(bits_arrow, 2))

        l1_right, l1_right_ag = self.merge_into_dad(l2_right_left, l2_right_right, "bB", scaling=scaling, arrows_buff=arrows_buff)
        self.play(l1_right_ag)
        hashes_1 = l1_right.copy().set_z_index(3)
        self.play(hashes_1.animate.move_to(hashes_vgroup[1]))

        self.explain(struct_vgroup[2], "Take from leaves/hashes list")

        dad, dad_ag = self.merge_into_dad(l1_left, l1_right, "aAbB", font_size=24, scaling=scaling, arrows_buff=arrows_buff)
        self.play(dad_ag, hashes_0.animate.set_opacity(0.2), hashes_1.animate.set_opacity(0.2), la_mtx(leaves_arrow, 4), la_mtx(bits_arrow, 3))
        hashes_2 = dad.copy().set_z_index(4)
        self.play(hashes_2.animate.move_to(hashes_vgroup[2]))
        self.explain(dad, "calculated root", wait_time=2)


    def three_tree_construct(self):
        scaling = 0.8
        arrows_buff = 0.5

        bufs_dist = 2.5

        leaves_texts = ['a', 'b']
        leaves_vgroup, _, _, _, _ = self.create_buffer(leaves_texts, GREEN_A, GREEN, GREEN_E, "leaves")
        self.play(leaves_vgroup.animate.move_to([-6 + leaves_vgroup.width/2,bufs_dist,0]).scale(0.8))

        proof_text = ['A']
        proof_vgroup, _, _, _, _ = self.create_buffer(proof_text, YELLOW_A, YELLOW, YELLOW_E, "proof")
        self.play(proof_vgroup.animate.move_to([-6 + proof_vgroup.width/2,0,0]).scale(0.8))

        struct_text = ['1', '0']
        struct_vgroup, _, _, _, _ = self.create_buffer(struct_text, RED_A, RED, RED_E, "proof flags")
        self.play(struct_vgroup.animate.move_to([-6 + struct_vgroup.width/2,-bufs_dist,0]).scale(0.8))

        hashes_text = ['', '']
        hashes_vgroup, _, hashes_arr, _, _ = self.create_buffer(hashes_text, GREY_D, GREY, GREY_C, "hashes")
        self.play(hashes_vgroup.animate.move_to([-6 + hashes_vgroup.width/2 + leaves_vgroup.width,bufs_dist,0]).scale(0.8))
        
        arrows_top_buf = 0.2
        leaves_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=GREEN)
        proof_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=YELLOW)
        bits_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=RED)

        arrows_start = np.array([-6 + 0.25, leaves_vgroup.height/2 + leaves_arrow.height/2 + arrows_top_buf, 0])
        bufs_dist_vec = np.array([0,bufs_dist,0])
        
        leaves_arrow.move_to(arrows_start + bufs_dist_vec)
        proof_arrow.move_to(arrows_start)
        bits_arrow.move_to(arrows_start - bufs_dist_vec)

        self.play(GrowArrow(leaves_arrow), GrowArrow(proof_arrow), GrowArrow(bits_arrow))

        self.play(hashes_arr[0].animate.set_opacity(0.4))
        leaves_hashes_xs = [i.get_center()[0] - i.width /2 for i in leaves_vgroup[:2]] + [i[0].get_center()[0] - i[0].width /2 for i in hashes_vgroup[:2]]
        
        # start creating the tree
        l2_left_left = leaves_vgroup[0]
        l2_left_right = leaves_vgroup[1]

        def la_mtx(la, i):
            return la.animate.move_to([leaves_hashes_xs[i], la.get_center()[1], la.get_center()[2]])

        self.play(l2_left_left.animate.move_to([0,-2,0]), la_mtx(leaves_arrow, 1))

        # explain the bits before continueing
        self.explain(struct_vgroup[0], "Take from leaves/hashes list")

        self.play(l2_left_right.animate.move_to([2,-2,0]), la_mtx(leaves_arrow, 2), la_mtx(bits_arrow, 1))

        l1_left, l1_left_ag = self.merge_into_dad(l2_left_left, l2_left_right, "ab", scaling=scaling, arrows_buff=arrows_buff)
        self.play(l1_left_ag)
        hashes_0 = l1_left.copy().set_z_index(2)
        self.play(hashes_0.animate.move_to(hashes_vgroup[0]))
        hashes_0_behind = hashes_0.copy().set_opacity(0.2).set_z_index(1)
        self.add(hashes_0_behind)
        self.wait(0.5)

        hashes_0.set_z_index(2)
        l1_left.set_z_index(1)
        self.play(hashes_0.animate.move_to(l1_left.get_center()), la_mtx(leaves_arrow, 3))


        self.explain(struct_vgroup[1], "Take from proof list")

        l1_right = proof_vgroup[0]
        l1_right.set_z_index(3)
        self.play(l1_right.animate.move_to([4,0,0]), la_mtx(proof_arrow, 1), la_mtx(bits_arrow, 2))

        root, root_ag = self.merge_into_dad(l1_left, l1_right, "abA", font_size=30, scaling=scaling, arrows_buff=arrows_buff)
        self.play(root_ag)

        hashes_1 = root.copy().set_z_index(4)
        self.play(hashes_1.animate.move_to(hashes_vgroup[1]))


    def malicious_tree_construct(self):
        scaling = 0.8
        arrows_buff = 0.5

        bufs_dist = 2.5

        leaves_texts = ['a']
        leaves_vgroup, _, _, _, _ = self.create_buffer(leaves_texts, GREEN_A, GREEN, GREEN_E, "leaves")
        self.play(leaves_vgroup.animate.move_to([-6 + leaves_vgroup.width/2,bufs_dist,0]).scale(0.8))

        proof_text = ['A', 'B']
        proof_vgroup, _, _, _, _ = self.create_buffer(proof_text, YELLOW_A, YELLOW, YELLOW_E, "proof")
        self.play(proof_vgroup.animate.move_to([-6 + proof_vgroup.width/2,0,0]).scale(0.8))

        struct_text = ['1', '0']
        struct_vgroup, _, _, _, _ = self.create_buffer(struct_text, RED_A, RED, RED_E, "proof flags")
        self.play(struct_vgroup.animate.move_to([-6 + struct_vgroup.width/2,-bufs_dist,0]).scale(0.8))

        hashes_text = ['0', '0']
        hashes_vgroup, _, hashes_arr, _, _ = self.create_buffer(hashes_text, GREY_D, GREY, GREY_C, "hashes")
        self.play(hashes_vgroup.animate.move_to([-6 + hashes_vgroup.width/2 + leaves_vgroup.width,bufs_dist,0]).scale(0.8))
        
        arrows_top_buf = 0.2
        leaves_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=GREEN)
        proof_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=YELLOW)
        bits_arrow = Arrow([0,1,0], [0,0,0], max_stroke_width_to_length_ratio=10, color=RED)

        arrows_start = np.array([-6 + 0.25, leaves_vgroup.height/2 + leaves_arrow.height/2 + arrows_top_buf, 0])
        bufs_dist_vec = np.array([0,bufs_dist,0])
        
        leaves_arrow.move_to(arrows_start + bufs_dist_vec)
        proof_arrow.move_to(arrows_start)
        bits_arrow.move_to(arrows_start - bufs_dist_vec)

        self.play(GrowArrow(leaves_arrow), GrowArrow(proof_arrow), GrowArrow(bits_arrow))

        leaves_hashes_xs = [i.get_center()[0] - i.width /2 for i in leaves_vgroup[:1]] + [i[0].get_center()[0] - i[0].width /2 for i in hashes_vgroup[:2]]
        
        # start creating the tree
        l2_left_left = leaves_vgroup[0]
        l2_left_right = hashes_vgroup[0]

        def la_mtx(la, i, shift=0):
            return la.animate.move_to([leaves_hashes_xs[i] + shift, la.get_center()[1], la.get_center()[2]])

        self.play(l2_left_left.animate.move_to([0,-2,0]), la_mtx(leaves_arrow, 1))

        # explain the bits before continueing
        self.explain(struct_vgroup[0], "Take from leaves/hashes list")

        self.explain(hashes_vgroup[0], "This is UNINITIALIZED!")

        self.play(l2_left_right.animate.move_to([2,-2,0]), la_mtx(leaves_arrow, 2), la_mtx(bits_arrow, 1))

        l1_left, l1_left_ag = self.merge_into_dad(l2_left_left, l2_left_right, "a0", scaling=scaling, arrows_buff=arrows_buff)
        self.play(l1_left_ag)

        hashes_0 = l1_left.copy().set_z_index(2)
        self.play(hashes_0.animate.move_to(hashes_vgroup[2+0]))
        hashes_0_behind = hashes_0.copy().set_opacity(0.2).set_z_index(1)
        self.add(hashes_0_behind)
        self.remove(hashes_vgroup[2+0])
        self.wait(0.5)


        hashes_1 = hashes_vgroup[1]
        self.explain(hashes_1, "This is UNINITIALIZED!")
        hashes_1.set_z_index(2)
        l1_left.set_z_index(1)

        hashes_1.set_z_index(2)

        self.play(hashes_1.animate.move_to(np.array(l1_left.get_center()) + np.array([-0.7, 1,0])) , leaves_arrow.animate.shift([1,0,0]))


        self.explain(struct_vgroup[1], "Take from proof list")

        l1_right = proof_vgroup[0]
        l1_right.set_z_index(3)
        self.play(l1_right.animate.move_to(np.array(hashes_1.get_center()) + np.array([2, 0,0])), la_mtx(proof_arrow, 1), la_mtx(bits_arrow, 2))

        root, root_ag = self.merge_into_dad(hashes_1, l1_right, "0A", scaling=scaling, arrows_buff=arrows_buff)
        self.play(root_ag)

        hashes_1 = root.copy().set_z_index(4)
        self.play(hashes_1.animate.move_to(hashes_vgroup[2+1]))

        self.play(Indicate(root[0]))
        self.explain(root, "calculated root", z_index=20, wait_time=1)

        end_credits_ag = self.end_credits(["The calculated root does not depend on the input leaves!", "If there's ever a child of the root is 0,", f"an attacker could <span fgcolor=\"{RED}\">validate malicious leaves!</span>"])
        self.play(end_credits_ag)


    def build_tree(self):
        fastpace_run_time = 0.4

        leaves_info = [('a', BLUE_E), ('b', RED_E), ('c', GREEN_E), ('d', YELLOW_E)]
        leaves = [
            VGroup(
                RoundedRectangle(corner_radius=0.2, width=1, height=1, fill_opacity=1, stroke_opacity=0),
                Text(leaf_text, color=leaf_color)
            )
            for leaf_text, leaf_color in leaves_info
            ]
        leaves_y = -1.5
        leaves[0].move_to([-1.5, leaves_y, 0])
        leaves[1].move_to([1.5, leaves_y, 0])
        leaves[2].move_to([4.5, leaves_y, 0])
        leaves[3].move_to([7.5, leaves_y, 0])
        self.play(GrowFromCenter(leaves[0]), GrowFromCenter(leaves[1]), run_time=fastpace_run_time)

        l1_left_text = f'H(<span fgcolor="{leaves_info[0][1]}">a</span>,<span fgcolor="{leaves_info[1][1]}">b</span>)'
        l1_left, l1_left_ag = self.merge_into_dad(leaves[0], leaves[1], l1_left_text, font_size=30, dad_height=2.5)
        self.play(l1_left_ag, run_time=fastpace_run_time)

        self.play(
            self.camera.frame.animate.move_to([3, 1.5, 0]).scale(1.2), run_time=fastpace_run_time
            )
        
        self.play(GrowFromCenter(leaves[2]), GrowFromCenter(leaves[3]), run_time=fastpace_run_time)

        l1_right_text = f'H(<span fgcolor="{leaves_info[2][1]}">c</span>,<span fgcolor="{leaves_info[3][1]}">d</span>)'
        l1_right, l1_right_ag = self.merge_into_dad(leaves[2], leaves[3], l1_right_text, font_size=30, dad_height=2.5)
        self.play(l1_right_ag, run_time=fastpace_run_time)

        root_text = f'H({l1_left_text},{l1_right_text})'
        root, root_ag = self.merge_into_dad(l1_left, l1_right, root_text, font_size=30, dad_height=2.5)
        self.play(root_ag, run_time=fastpace_run_time)

        # leaves[2][0].set_z_index(0) # square
        # leaves[2][1].set_z_index(0) # text
        # self.play(leaves[2][0].animate.set_color(GREEN_A), run_time=0.3)
        explain_leaf_ag = self.explain_noanim(leaves[2], "Leaf to verify", GREEN)
        self.play(explain_leaf_ag, leaves[2][0].animate.set_color(GREEN_A))
        leaves[2].set_z_index(3)

        l1_left.set_z_index(5)
        explain_proof_ag = self.explain_noanim(VGroup(leaves[3], l1_left), "The proof", YELLOW, center=True)
        self.play(explain_proof_ag, leaves[3][0].animate.set_color(YELLOW_A), l1_left[0].animate.set_color(YELLOW_A))

        all_needed_nodes = VGroup(leaves[2], leaves[3], l1_left)

        # explain_all_needed_ag = self.explain_noanim(all_needed_nodes, "all you need to send to verify the leaf", WHITE, center=True)
        # self.play(explain_all_needed_ag)
        explain_text = Text("everything you need to verify the leaf", font_size=36, color=WHITE)
        explain_text.move_to(all_needed_nodes.get_center())
        all_needed_explain = VGroup(
            explain_text,
        ).set_z_index(10)

        all_needed_nodes.set_z_index(10)
        shade_background = Rectangle(width=1000, height=1000, fill_opacity=0.93, color=BLACK)
        shade_background.move_to([-50, 50, 0])
        shade_background.set_z_index(9)
        self.play(FadeIn(shade_background), FadeIn(all_needed_explain))
        self.wait(1)
        self.play(FadeOut(all_needed_explain))


        # do proof
        l1_right_text = f'H(<span fgcolor="{leaves_info[2][1]}">c</span>,<span fgcolor="{leaves_info[3][1]}">d</span>)'
        l1_right, l1_right_ag = self.merge_into_dad(leaves[2], leaves[3], l1_right_text, font_size=30, dad_height=2.5, z_index=10)
        self.play(l1_right_ag)

        root_text = f'H({l1_left_text},{l1_right_text})'
        root, root_ag = self.merge_into_dad(l1_left, l1_right, root_text, font_size=30, dad_height=2.5, z_index=10)
        self.play(root_ag)

        self.play(Indicate(root[0]))
        self.explain(root, "calculated root", z_index=20, wait_time=2)

    def construct(self):
        # self.full_tree_construct()
        # self.three_tree_construct()
        # self.build_tree()
        self.malicious_tree_construct()



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
