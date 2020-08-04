import logging

from abc import ABC

logger = logging.getLogger()


class Output(ABC):
    def __init__(self, output_path, force=False):
        self.output_path = output_path
        self.force = force

    def prepare(self):
        pass

    def compute(self, classified):
        pass
