import customtkinter as ctk

from tkinter import messagebox

from config import (
    APP_NAME,
    VERSION
)


from engine import (
    load_images,
    natural_sort,
    create_pairs,
    create_collage,
    export_image
)



class FashionStudioApp:


    def __init__(self):


        self.root = ctk.CTk()


        self.root.title(
            f"{APP_NAME} {VERSION}"
        )


        self.root.geometry(
            "900x600"
        )


        self.create_ui()



    def create_ui(self):


        title = ctk.CTkLabel(

            self.root,

            text="Fashion Studio AI Edition",

            font=(
                "Arial",
                32
            )

        )


        title.pack(
            pady=40
        )



        self.status = ctk.CTkLabel(

            self.root,

            text="等待任务",

            font=(
                "Arial",
                18
            )

        )


        self.status.pack(
            pady=20
        )



        self.start_button = ctk.CTkButton(

            self.root,

            text="开始生成",

            width=200,

            height=50,

            command=self.generate

        )


        self.start_button.pack(
            pady=40
        )



    def update_status(
            self,
            text
    ):

        self.status.configure(
            text=text
        )

        self.root.update()



    def generate(self):


        try:


            self.update_status(
                "读取图片..."
            )


            images = load_images()



            if len(images) < 2:


                messagebox.showwarning(

                    "提示",

                    "input文件夹至少需要2张图片"

                )

                return



            self.update_status(
                "图片排序..."
            )


            images = natural_sort(
                images
            )



            self.update_status(
                "创建组合..."
            )


            pairs = create_pairs(
                images
            )



            count = 1


            for left,right in pairs:


                self.update_status(

                    f"生成第 {count} 张"

                )


                collage = create_collage(

                    left,

                    right

                )


                export_image(

                    collage,

                    count

                )


                count += 1



            self.update_status(

                "完成"

            )


            messagebox.showinfo(

                "完成",

                f"成功生成 {count-1} 张图片"

            )



        except Exception as e:


            messagebox.showerror(

                "错误",

                str(e)

            )



    def run(self):


        self.root.mainloop()