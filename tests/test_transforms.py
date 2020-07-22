import pytest
import numpy as np
import albumentations as A
import albumentations_experimental as AE


@pytest.mark.parametrize(
    ["augmentation_cls", "params", "keypoints", "result_keypoints"],
    [
        [
            AE.HorizontalFlipSymmetricKeypoints,
            {"symmetric_keypoints": {0: 1, 3: 4}},
            [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
            [[98, 0], [99, 0], [97, 0], [95, 0], [96, 0]],
        ],
        [
            AE.VerticalFlipSymmetricKeypoints,
            {"symmetric_keypoints": {0: 1, 4: 2}},
            [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
            [[0, 98], [0, 99], [0, 95], [0, 96], [0, 97]],
        ],
        [
            AE.TransposeSymmetricKeypoints,
            {"symmetric_keypoints": {0: 1, 4: 3}},
            [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],
            [[3, 2], [1, 0], [5, 4], [9, 8], [7, 6]],
        ],
    ],
)
def test_symmetric(augmentation_cls, params, keypoints, result_keypoints):
    img = np.zeros([100, 100, 3], dtype=np.uint8)
    aug = A.Compose([augmentation_cls(**params, p=1)], keypoint_params=A.KeypointParams("xy"))

    res = aug(image=img, keypoints=keypoints)

    assert np.allclose(result_keypoints, res["keypoints"])
