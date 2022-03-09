from enum import Enum


class EventType(Enum):
    GENERATOR = 1
    PROCESSOR = 2
    DEFAULT = 3


class Event:
    def __init__(self, type: EventType, time, ind):
        self.type = type
        self.time = time
        self.ind = ind
