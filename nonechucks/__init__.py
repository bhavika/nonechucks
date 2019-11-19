import logging

import torch
import torch.utils.data


logger = logging.getLogger(__name__)


def _get_pytorch_version():
    version = torch.__version__

    # PyTorch versions are now named as 1.3.0+cpu or 1.3.1+cu92 for CUDA
    version = version.split('+')[0]

    major, minor, patch = [int(x) for x in version.split(".")]
    if major != 1:
        raise RuntimeError(
            "nonechucks only supports PyTorch major version 1 at the moment."
        )
    if minor > 2:
        logger.warn(
            "nonechucks may not work properly with this version of PyTorch ({}). "
            "It has only been tested on PyTorch versions 1.0, 1.1, and 1.2".format(
                version
            )
        )
    return major, minor


MAJOR, MINOR = _get_pytorch_version()

if MINOR > 1:
    SingleProcessDataLoaderIter = (
        torch.utils.data.dataloader._SingleProcessDataLoaderIter
    )
    MultiProcessingDataLoaderIter = (
        torch.utils.data.dataloader._MultiProcessingDataLoaderIter
    )
else:
    SingleProcessDataLoaderIter = torch.utils.data.dataloader._DataLoaderIter
    MultiProcessingDataLoaderIter = torch.utils.data.dataloader._DataLoaderIter


from nonechucks.dataset import SafeDataset
from nonechucks.sampler import SafeSampler
from nonechucks.dataloader import SafeDataLoader
