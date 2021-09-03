import warnings


def create_symmetric_keypoints(values):
    values = dict(values)

    _set = set()
    for key, item in values.items():
        _set.add(key)
        _set.add(item)
    count = len(_set)

    if max(_set) != count - 1:
        without_pair = []
        for i in range(count):
            if i not in _set:
                values[i] = i
                without_pair.append(i)
        warnings.warn("Found points without pairs in symmetric transform: " + str(without_pair))
        count += len(without_pair)

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
            keypoints[x1], keypoints[x2] = keypoints[x2][:4] + keypoints[x1][4:], keypoints[x1][:4] + keypoints[x2][4:]

    return keypoints
