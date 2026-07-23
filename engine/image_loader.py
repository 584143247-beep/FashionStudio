"""
Fashion Studio
Image Loader

负责：
读取输入文件夹中的图片
"""

import os

from config import (
    INPUT_FOLDER,
    SUPPORTED_IMAGE
)


def load_images(folder=INPUT_FOLDER):
    """
    获取文件夹内所有图片
    """

    images = []


    if not os.path.exists(folder):

        return images


    for filename in os.listdir(folder):

        ext = os.path.splitext(filename)[1].lower()


        if ext in SUPPORTED_IMAGE:

            images.append(
                os.path.join(
                    folder,
                    filename
                )
            )


    return images