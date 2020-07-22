from albumentations import HorizontalFlip, VerticalFlip, Flip, Transpose
from albumentations_experimental.augmentations.keypoint_utils import swap_symmetric

__all__ = [
    "HorizontalFlipSymmetricKeypoints",
    "VerticalFlipSymmetricKeypoints",
    "FlipSymmetricKeypoints",
    "TransposeSymmetricKeypoints",
]


class HorizontalFlipSymmetricKeypoints(HorizontalFlip):
    """Flip the input horizontally around the y-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.
        symmetric_keypoints (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if horizontal flip swaps their semantics, e.g. left arm - right arm.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """

    def __init__(self, symmetric_keypoints, *args, **kwargs):
        super(HorizontalFlipSymmetricKeypoints, self).__init__(*args, **kwargs)
        if isinstance(symmetric_keypoints, dict):
            self.symmetric_keypoints = symmetric_keypoints
        else:
            self.symmetric_keypoints = {i: j for i, j in symmetric_keypoints}

    def apply_to_keypoints(self, keypoints, **params):
        keypoints = super().apply_to_keypoints(keypoints, **params)
        return swap_symmetric(keypoints, self.symmetric_keypoints)

    def get_transform_init_args_names(self):
        return super(HorizontalFlipSymmetricKeypoints, self).get_transform_init_args_names() + ("symmetric_keypoints",)


class VerticalFlipSymmetricKeypoints(VerticalFlip):
    """Flip the input vertically around the x-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.
        symmetric_keypoints (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if vertical flip swaps their semantics, e.g. top corner - bottom corner.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """

    def __init__(self, symmetric_keypoints, *args, **kwargs):
        super(VerticalFlipSymmetricKeypoints, self).__init__(*args, **kwargs)
        if isinstance(symmetric_keypoints, dict):
            self.symmetric_keypoints = symmetric_keypoints
        else:
            self.symmetric_keypoints = {i: j for i, j in symmetric_keypoints}

    def apply_to_keypoints(self, keypoints, **params):
        keypoints = super().apply_to_keypoints(keypoints, **params)
        return swap_symmetric(keypoints, self.symmetric_keypoints)

    def get_transform_init_args_names(self):
        return super(VerticalFlip, self).get_transform_init_args_names() + ("symmetric_keypoints",)


class FlipSymmetricKeypoints(Flip):
    """Flip the input horizontally around the y-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.
        symmetric_keypoints_horizontal (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if horizontal flip swaps their semantics, e.g. left arm - right arm.
        symmetric_keypoints_vertical (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if vertical flip swaps their semantics, e.g. top corner - bottom corner.
        symmetric_keypoints_both (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if vertical and horizontal flip swaps their semantics, e.g. top left corner - bottom right corner.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """

    def __init__(self, symmetric_keypoints_horizontal=(), symmetric_keypoints_vertical=(), symmetric_keypoints_both=(), *args, **kwargs):
        super(FlipSymmetricKeypoints, self).__init__(*args, **kwargs)

        if isinstance(symmetric_keypoints_horizontal, dict):
            self.symmetric_keypoints_horizontal = symmetric_keypoints_horizontal
        else:
            self.symmetric_keypoints_horizontal = {i: j for i, j in symmetric_keypoints_horizontal}

        if isinstance(symmetric_keypoints_vertical, dict):
            self.symmetric_keypoints_vertical = symmetric_keypoints_vertical
        else:
            self.symmetric_keypoints_vertical = {i: j for i, j in symmetric_keypoints_vertical}

        if isinstance(symmetric_keypoints_both, dict):
            self.symmetric_keypoints_both = symmetric_keypoints_both
        else:
            self.symmetric_keypoints_both = {i: j for i, j in symmetric_keypoints_both}

        if (len(symmetric_keypoints_vertical) or len(symmetric_keypoints_horizontal)) and not len(symmetric_keypoints_both):
                raise ValueError("symmetric_keypoints_both is empty. Undefined behaviour in case horizontal and vertical flip.")

    def apply_to_keypoints(self, keypoints, **params):
        keypoints = super().apply_to_keypoints(keypoints, **params)
        if params["d"] == 1:
            keypoints = swap_symmetric(keypoints, self.symmetric_keypoints_horizontal)
        elif params["d"] == 0:
            keypoints = swap_symmetric(keypoints, self.symmetric_keypoints_vertical)
        else:
            keypoints = swap_symmetric(keypoints, self.symmetric_keypoints_both)
        return keypoints

    def get_transform_init_args_names(self):
        return super(FlipSymmetricKeypoints, self).get_transform_init_args_names() + (
            "symmetric_keypoints_horizontal",
            "symmetric_keypoints_vertical",
            "symmetric_keypoints_both"
        )


class TransposeSymmetricKeypoints(Transpose):
    """Flip the input horizontally around the y-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.
        symmetric_keypoints (tuple, list, dict): tuple of pairs containing indices of symmetric keypoints.
            Keypoints are considered as symmetric if vertical and horizontal flip swaps their semantics, e.g. top left corner - bottom right corner.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """

    def __init__(self, symmetric_keypoints=(), *args, **kwargs):
        super(Transpose, self).__init__(*args, **kwargs)

        if isinstance(symmetric_keypoints, dict):
            self.symmetric_keypoints = symmetric_keypoints
        else:
            self.symmetric_keypoints = {i: j for i, j in symmetric_keypoints}

    def apply_to_keypoints(self, keypoints, **params):
        keypoints = super().apply_to_keypoints(keypoints, **params)
        keypoints = swap_symmetric(keypoints, self.symmetric_keypoints)
        return keypoints

    def get_transform_init_args_names(self):
        return super(Transpose, self).get_transform_init_args_names() + (
            "symmetric_keypoints",
        )


if __name__ == "__main__":
    import numpy as np
    from albumentations import Compose, KeypointParams

    aug = Compose(
        [VerticalFlipSymmetricKeypoints(symmetric_keypoints=[[0, 1], [2, 3]], p=1)],
        keypoint_params=KeypointParams("xy"),
    )

    img = np.zeros([101, 101, 3], dtype=np.uint8)
    keypoints = [[10, 0], [20, 0], [30, 0], [40, 0]]

    res = aug(image=img, keypoints=keypoints)
    print(res["keypoints"])
