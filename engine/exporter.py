from pathlib import Path
from PIL import Image


def export_images(images, output_folder):
    """
    保存最终拼图结果
    """

    output_path = Path(output_folder)

    output_path.mkdir(
        exist_ok=True
    )

    count = 1

    for img in images:

        filename = (
            f"{count:03d}.jpg"
        )

        save_path = (
            output_path /
            filename
        )

        img.save(
            save_path,
            quality=95
        )

        count += 1


def create_output_folder(folder):

    folder = Path(folder)

    output = (
        folder /
        "拼图输出"
    )

    output.mkdir(
        exist_ok=True
    )

    return output
