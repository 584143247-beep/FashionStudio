from PIL import Image
from pathlib import Path


TARGET_RATIO = 3/4



def resize_keep_ratio(img):

    width,height = img.size

    target_height = height

    target_width = int(
        target_height * TARGET_RATIO
    )


    if width < target_width:

        scale = target_width / width

        img = img.resize(
            (
                int(width*scale),
                int(height*scale)
            )
        )

    return img



def make_collage(
        img1_path,
        img2_path,
        output_path
):

    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")


    img1 = resize_keep_ratio(img1)
    img2 = resize_keep_ratio(img2)


    height=max(
        img1.height,
        img2.height
    )


    canvas=Image.new(
        "RGB",
        (
            img1.width+img2.width,
            height
        ),
        "white"
    )


    canvas.paste(
        img1,
        (0,0)
    )

    canvas.paste(
        img2,
        (
            img1.width,
            0
        )
    )


    canvas.save(
        output_path,
        quality=95
    )
