def create_symmetric_keypoints(values):
    values = dict(values)

    _set = set()
    for key, item in values.items():
        _set.add(key)
        _set.add(item)
    count = len(_set)

    if not all([(i in _set) for i in range(count)]):
        raise ValueError(
            "Values in symmetric_keypoints must be in range(len(unique(symmetric_keypoints))) without skips."
        )

    return values, count


def swap_symmetric(keypoints, symmetric, symmetric_count):
    if not len(symmetric) or not len(keypoints):
        return keypoints

    keypoints = list(keypoints)
    if len(keypoints) % symmetric_count != 0:
        raise RuntimeError(
            "Kyepoints length must be divisible to symmetric count. Kepoints length = {} symmetric count = {}".format(
                len(keypoints), symmetric_count
            )
        )

    for x1 in range(len(keypoints)):
        i = x1 % symmetric_count
        j = x1 // symmetric_count
        x2 = symmetric.get(i, None)

        if x2 is not None:
            x2 += j * symmetric_count
            keypoints[x1], keypoints[x2] = keypoints[x2], keypoints[x1]

    return keypoints
