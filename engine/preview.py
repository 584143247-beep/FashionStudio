from PIL import Image
from pathlib import Path


def create_preview(image_pairs, save_path):

    previews = []

    for index, pair in enumerate(image_pairs[:5]):

        img1 = Image.open(pair[0])
        img2 = Image.open(pair[1])

        height = max(img1.height, img2.height)

        img1.thumbnail(
            (
                int(height * 0.75),
                height
            )
        )

        img2.thumbnail(
            (
                int(height * 0.75),
                height
            )
        )


        canvas = Image.new(
            "RGB",
            (
                img1.width + img2.width,
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


        preview_file = Path(save_path) / f"preview_{index+1}.jpg"

        canvas.save(
            preview_file,
            quality=95
        )

        previews.append(preview_file)


    return previews