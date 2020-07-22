def swap_symmetric(keypoints, symmetric):
    if not len(symmetric):
        return keypoints

    keypoints = list(keypoints)

    for i in range(len(keypoints)):
        j = symmetric.get(i, None)
        if j is not None:
            keypoints[i], keypoints[j] = keypoints[j], keypoints[i]

    return keypoints
