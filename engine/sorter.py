"""
Fashion Studio

图片自然排序模块

解决：

look1.jpg
look2.jpg
look10.jpg

排序错误问题
"""

import re



def natural_sort(files):


    def key(text):

        filename = text.lower()


        numbers = re.findall(
            r'\d+',
            filename
        )


        if numbers:

            return [
                int(numbers[0]),
                filename
            ]

        else:

            return [
                999999,
                filename
            ]


    return sorted(
        files,
        key=key
    )