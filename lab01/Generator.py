from typing import Optional, Union
from Distributions import *


class Generator:
    def __init__(self, generator: Optional[Union[ExponentGenerator, WeibullGenerator]]):
        self.generator = generator

    def nextTime(self, curTime=0):
        return curTime + self.generator.getTime()
