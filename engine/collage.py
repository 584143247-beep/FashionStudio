from PIL import Image
from pathlib import Path


# 最终小红书比例
OUTPUT_WIDTH = 1080
OUTPUT_HEIGHT = 1440


def resize_cover(img, target_w, target_h):
    """
    图片自动放大裁切
    保持比例填满区域
    """

    w, h = img.size

    scale = max(
        target_w / w,
        target_h / h
    )

    new_size = (
        int(w * scale),
        int(h * scale)
    )

    img = img.resize(
        new_size,
        Image.LANCZOS
    )

    left = (img.width - target_w) // 2
    top = (img.height - target_h) // 2

    img = img.crop(
        (
            left,
            top,
            left + target_w,
            top + target_h
        )
    )

    return img



def create_horizontal_collage(
        img1_path,
        img2_path,
        output_path
):

    """
    左右拼图核心

    look1 | look2

    输出3:4
    """

    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")


    # 左右区域尺寸

    half_width = OUTPUT_WIDTH // 2


    img1 = resize_cover(
        img1,
        half_width,
        OUTPUT_HEIGHT
    )

    img2 = resize_cover(
        img2,
        half_width,
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


    # 左右排列

    canvas.paste(
        img1,
        (0,0)
    )


    canvas.paste(
        img2,
        (half_width,0)
    )


    canvas.save(
        output_path,
        quality=95
    )


    return output_path



def batch_generate(
        pairs,
        output_folder
):

    """
    批量生成

    pairs:

    [
      (look1,look2),
      (look3,look4)
    ]

    """

    output_folder = Path(output_folder)

    output_folder.mkdir(
        exist_ok=True
    )


    results=[]


    for index,(a,b) in enumerate(
        pairs,
        start=1
    ):


        output_file = (
            output_folder /
            f"{index:03}.jpg"
        )


        create_horizontal_collage(
            a,
            b,
            output_file
        )


        results.append(
            output_file
        )


    return results
