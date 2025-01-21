from typing import List

import numpy as np
from torch.utils.data import Dataset as BaseDataset

from blueness import module
from blue_objects import file
from roofai.dataset.classes import DatasetTarget

from palisades import NAME
from palisades.logger import logger

NAME = module.name(__file__, NAME)


class GeoDataset(BaseDataset):
    def __init__(
        self,
        filename: str,
        augmentation=None,
        preprocessing=None,
        count=-1,
        chip_overlap: float = 0.5,
    ):
        self.chip_height = DatasetTarget.TORCH.chip_height
        self.chip_width = DatasetTarget.TORCH.chip_width
        self.chip_overlap = chip_overlap

        success, self.matrix, _ = file.load_geoimage(
            filename,
            log=True,
        )
        assert success
        self.matrix = np.transpose(self.matrix, (1, 2, 0))

        self.ids: List[str] = []
        for y in range(
            0,
            self.matrix.shape[0] - self.chip_height,
            int(chip_overlap * self.chip_height),
        ):
            for x in range(
                0,
                self.matrix.shape[1] - self.chip_width,
                int(chip_overlap * self.chip_width),
            ):
                self.ids += [f"{y:05d}-{x:05d}"]

        if count != -1:
            self.ids = self.ids[:count]

        self.augmentation = augmentation
        self.preprocessing = preprocessing

        logger.info(
            "{}.GeoDataset({}): {}x{}: {:,} chip(s).".format(
                NAME,
                file.name_and_extension(filename),
                self.chip_height,
                self.chip_width,
                len(self.ids),
            )
        )

    def __getitem__(self, i):
        item_id = self.ids[i]  # expecting f"{y:05d}-{x:05d}"

        pieces = item_id.split("-")
        assert len(pieces) == 2
        y = int(pieces[0])
        x = int(pieces[1])

        image = self.matrix[
            y : y + self.chip_height,
            x : x + self.chip_width,
        ]

        mask = np.zeros(image.shape, dtype=np.uint8)

        if self.augmentation:
            sample = self.augmentation(image=image, mask=mask)
            image, mask = sample["image"], sample["mask"]

        if self.preprocessing:
            sample = self.preprocessing(image=image, mask=mask)
            image, mask = sample["image"], sample["mask"]

        return image, mask

    def __len__(self):
        return len(self.ids)
