from pathlib import Path


# 支持的图片格式
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}



def load_images_from_folder(folder_path):
    """
    读取指定文件夹中的全部图片

    注意：
    不进行排序
    保留文件系统读取顺序

    参数:
        folder_path:
            图片文件夹路径

    返回:
        图片路径列表
    """

    folder = Path(folder_path)


    if not folder.exists():

        raise FileNotFoundError(
            f"文件夹不存在: {folder_path}"
        )


    if not folder.is_dir():

        raise ValueError(
            "选择的路径不是文件夹"
        )


    images = []


    # 按文件夹当前读取顺序获取图片
    for file in folder.iterdir():

        if file.is_file():

            if file.suffix.lower() in IMAGE_EXTENSIONS:

                images.append(
                    str(file)
                )


    return images



def get_image_count(folder_path):

    """
    获取图片数量
    """

    images = load_images_from_folder(
        folder_path
    )

    return len(images)
