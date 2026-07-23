"""
Fashion Studio V1.0 Beta

Build001 Test

测试：
1. 模块导入
2. 图片读取
3. 图片排序
4. 图片配对
"""


from engine import (
    load_images,
    natural_sort,
    create_pairs
)


from config import INPUT_FOLDER



def test_import():

    print("✅ Engine模块加载成功")



def test_images():


    print("\n正在扫描图片...")


    images = load_images()


    print(
        f"发现图片数量：{len(images)}"
    )


    if len(images) == 0:

        print(
            "⚠ input文件夹暂无图片"
        )

        return []


    return images



def test_sort(images):


    print(
        "\n排序测试..."
    )


    result = natural_sort(
        images
    )


    for item in result:

        print(
            item
        )


    return result



def test_pair(images):


    print(
        "\n配对测试..."
    )


    pairs = create_pairs(
        images
    )


    print(
        f"生成组合数量：{len(pairs)}"
    )


    for index,pair in enumerate(
        pairs,
        start=1
    ):

        print(
            f"{index}:"
        )

        print(
            pair[0]
        )

        print(
            pair[1]
        )


    return pairs




if __name__ == "__main__":


    print(
        "===================="
    )

    print(
        "Fashion Studio Build001 Test"
    )

    print(
        "===================="
    )



    test_import()


    images = test_images()



    if images:


        images = test_sort(
            images
        )


        test_pair(
            images
        )



    print(
        "\n测试结束"
    )