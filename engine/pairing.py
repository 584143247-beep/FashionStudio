"""
Fashion Studio

图片配对模块

例如：

look1
look2

↓

001


look3
look4

↓

002
"""


def create_pairs(images):


    pairs = []


    total = len(images)


    index = 0


    while index < total - 1:


        pair = (

            images[index],

            images[index + 1]

        )


        pairs.append(pair)


        index += 2



    return pairs