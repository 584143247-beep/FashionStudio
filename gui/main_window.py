import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

from engine.image_loader import load_images
from engine.pairing import pair_images
from engine.preview import create_preview
from engine.collage import make_collage
from engine.exporter import create_output_folder


class FashionStudioApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "Style Pic 拼图助手 V2.0"
        )

        self.geometry(
            "700x600"
        )


        self.folder = None

        self.images = []

        self.pairs = []


        # 标题

        self.title_label = ctk.CTkLabel(
            self,
            text="Style Pic 拼图助手 V2.0",
            font=("微软雅黑",26)
        )

        self.title_label.pack(
            pady=25
        )


        # 选择文件夹

        self.select_button = ctk.CTkButton(
            self,
            text="选择图片文件夹",
            command=self.select_folder
        )

        self.select_button.pack(
            pady=10
        )


        self.info_label = ctk.CTkLabel(
            self,
            text="等待选择文件夹"
        )

        self.info_label.pack(
            pady=10
        )


        # 预览按钮

        self.preview_button = ctk.CTkButton(
            self,
            text="生成预览",
            command=self.preview
        )

        self.preview_button.pack(
            pady=10
        )


        self.preview_label = ctk.CTkLabel(
            self,
            text="预览区域"
        )

        self.preview_label.pack(
            pady=20
        )


        # 生成按钮

        self.generate_button = ctk.CTkButton(
            self,
            text="开始生成3:4拼图",
            command=self.generate
        )

        self.generate_button.pack(
            pady=10
        )



    def select_folder(self):

        folder = filedialog.askdirectory()


        if folder:

            self.folder = Path(folder)


            self.images = load_images(
                self.folder
            )


            self.pairs = pair_images(
                self.images
            )


            self.info_label.configure(
                text=
                f"已读取图片：{len(self.images)}张\n"
                f"预计生成：{len(self.pairs)}张拼图"
            )



    def preview(self):

        if not self.pairs:

            self.preview_label.configure(
                text="请先选择图片文件夹"
            )

            return



        preview_file = create_preview(
            self.pairs[0]
        )


        self.preview_label.configure(
            text=
            f"预览生成完成\n{preview_file}"
        )



    def generate(self):

        if not self.pairs:

            self.preview_label.configure(
                text="没有可生成图片"
            )

            return



        output_folder = create_output_folder(
            self.folder
        )


        count = 1


        for pair in self.pairs:


            output_file = (
                output_folder /
                f"{count:03d}.jpg"
            )


            make_collage(
                pair[0],
                pair[1],
                output_file
            )


            count += 1



        self.preview_label.configure(
            text=
            "生成完成！\n"
            f"文件位置：{output_folder}"
        )
