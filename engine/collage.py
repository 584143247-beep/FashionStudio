"""
Fashion Studio

Collage Engine

负责：
图片拼接
3:4画布生成
"""


from PIL import Image

from config import (
    OUTPUT_WIDTH,
    OUTPUT_HEIGHT
)



def resize_image(
        image,
        target_height
):

    """
    按高度等比例缩放
    """

    ratio = target_height / image.height


    new_width = int(
        image.width * ratio
    )


    return image.resize(
        (
            new_width,
            target_height
        )
    )



def create_collage(
        left_image_path,
        right_image_path
):

    """
    创建左右拼图
    """


    left = Image.open(
        left_image_path
    ).convert(
        "RGB"
    )


    right = Image.open(
        right_image_path
    ).convert(
        "RGB"
    )


    # 统一高度

    left = resize_image(
        left,
        OUTPUT_HEIGHT
    )


    right = resize_image(
        right,
        OUTPUT_HEIGHT
    )



    canvas = Image.new(
        "RGB",
        (
            OUTPUT_WIDTH,
            OUTPUT_HEIGHT
        ),
        "white"
    )


    # 左图位置

    canvas.paste(
        left,
        (
            0,
            0
        )
    )


    # 右图位置

    right_x = (
        OUTPUT_WIDTH
        -
        right.width
    )


    canvas.paste(
        right,
        (
            right_x,
            0
        )
    )


    return canvas