from pathlib import Path
from PIL import Image


def create_preview(pair):

    img1,img2 = pair


    img1 = Image.open(img1)
    img2 = Image.open(img2)



    width = img1.width + img2.width
    height = max(
        img1.height,
        img2.height
    )


    preview = Image.new(
        "RGB",
        (width,height),
        "white"
    )


    preview.paste(
        img1,
        (0,0)
    )


    preview.paste(
        img2,
        (img1.width,0)
    )


    output = Path("preview_001.jpg")


    preview.save(
        output,
        quality=95
    )


    return output
