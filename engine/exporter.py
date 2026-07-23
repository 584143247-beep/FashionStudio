"""
Fashion Studio

Export Engine

负责：
保存生成结果
"""


import os


from config import (
    OUTPUT_FOLDER,
    JPEG_QUALITY
)



def export_image(
        image,
        number
):


    if not os.path.exists(
        OUTPUT_FOLDER
    ):

        os.makedirs(
            OUTPUT_FOLDER
        )



    filename = (
        f"{number:03d}.jpg"
    )


    path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )


    image.save(
        path,
        quality=JPEG_QUALITY
    )


    return path