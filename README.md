# Albumentations Experimental

Albumentations Experimental provides experimental and cutting edge augmentation techniques on top of the [Albumentations](https://github.com/albumentations-team/albumentations) library.

## Why a separate library

Albumentations provides stable and well-tested interfaces for performing augmentations. We don't want to pollute the library with features that may be prone to rapid changes in interfaces and behavior since they could break users' pipelines. But we also want to implement new, experimental features and see whether they will be useful.

So we created Albumentations Experimental, a library that will help us to iterate faster and remove the need for striving for backward compatibility and rigorous testing.

Beware, that each new version of Albumentations Experimental may contain backward-incompatible changes both in interfaces and behavior.

When features in Albumentations Experimental are mature enough, we will port them to the main library with all our usual policies such as rigorous testing, extensive documentation, and stable behavior.

## Installation
Albumentations Experimental requires Python 3.5 or higher.

### Install the latest stable version from PyPI

```Bash
pip install -U albumentations_experimental
```

### Install the latest version from the master's branch on GitHub
```Bash
pip install -U git+https://github.com/albumentations-team/albumentations-experimental
```

## Usage

Import augmentations from the library:

```python
from albumentations_experimental import FlipSymmetricKeypoints
```

## Documentation

Documentation is available at [https://albumentations.ai/docs/experimental/overview/](https://albumentations.ai/docs/experimental/overview/)

## List of augmentations and their supported targets

### Spatial-level transforms

| Transform                                                                                                                                                                                                     | Image | Masks | BBoxes | Keypoints |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---: | :---: | :----: | :-------: |
| [FlipSymmetricKeypoints](https://albumentations.ai/docs/experimental/api_reference/augmentations/transforms/#albumentations_experimental.augmentations.transforms.FlipSymmetricKeypoints)                     | ✓     | ✓     | ✓      | ✓         |
| [HorizontalFlipSymmetricKeypoints](https://albumentations.ai/docs/experimental/api_reference/augmentations/transforms/#albumentations_experimental.augmentations.transforms.HorizontalFlipSymmetricKeypoints) | ✓     | ✓     | ✓      | ✓         |
| [TransposeSymmetricKeypoints](https://albumentations.ai/docs/experimental/api_reference/augmentations/transforms/#albumentations_experimental.augmentations.transforms.TransposeSymmetricKeypoints)           | ✓     | ✓     | ✓      | ✓         |
| [VerticalFlipSymmetricKeypoints](https://albumentations.ai/docs/experimental/api_reference/augmentations/transforms/#albumentations_experimental.augmentations.transforms.VerticalFlipSymmetricKeypoints)     | ✓     | ✓     | ✓      | ✓         |
