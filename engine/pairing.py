"""
Fashion Studio
Build002
Image Pairing Module

功能：
1. 按文件夹原始顺序读取图片
2. Look1 + Look2
3. Look3 + Look4
4. 自动两两配对
5. 删除图片后自动重新连续配对
"""

from pathlib import Path


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


def get_image_pairs(image_list):
    """
    将图片按照两个一组进行配对

    示例：
    [
        look1,
        look2,
        look3,
        look4
    ]

    返回：
    [
        (look1, look2),
        (look3, look4)
    ]
    """

    pairs = []

    index = 0

    while index < len(image_list) - 1:
        pairs.append(
            (
                image_list[index],
                image_list[index + 1]
            )
        )

        index += 2

    return pairs



def load_folder_images(folder_path):
    """
    读取指定文件夹图片

    注意：
    不进行重新排序

    保留系统文件夹中的排列顺序
    """

    folder = Path(folder_path)

    images = []

    for file in folder.iterdir():

        if file.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(file)

    return images



def create_pairs_from_folder(folder_path):

    images = load_folder_images(folder_path)

    pairs = get_image_pairs(images)

    return pairs



if __name__ == "__main__":

    test_folder = "input"

    pairs = create_pairs_from_folder(test_folder)

    print(
        "发现图片数量:",
        len(pairs) * 2
    )

    print(
        "生成组合:",
        len(pairs)
    )


    for index, pair in enumerate(pairs, start=1):

        print(
            f"{index:03d}:",
            pair[0].name,
            "+",
            pair[1].name
        )
