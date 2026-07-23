def pair_images(images):

    """
    两两配对

    look1 + look2
    look3 + look4
    """

    pairs = []

    index = 0


    while index < len(images):

        if index + 1 < len(images):

            pairs.append(
                (
                    images[index],
                    images[index+1]
                )
            )

        index += 2


    return pairs
