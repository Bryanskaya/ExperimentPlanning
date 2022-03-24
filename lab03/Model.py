from Processor import *
from Event import *

from queue import Queue


class Model:
    def __init__(self, genArr: [Generator], procArr: [Processor]):
        self.genArr = genArr
        self.procArr = procArr
        self.eventArr = []
        self.buf = Queue()
        self.processed = 0
        self.sizeQMax = 0
        self.timeWait = []
        self.timeProc = {}

    def calcWorkingTime(self, curTime):
        s = 0
        for elem in self.timeProc.keys():
            if elem <= curTime:
                s += self.timeProc[elem]
        return s

    def doModeling(self, taskNum, timeModeling) -> dict:
        curEvent = Event(EventType.DEFAULT, 0, -1)

        for i in range(len(self.genArr)):
            self.eventArr.append(Event(EventType.GENERATOR, self.genArr[i].nextTime(), i))

        while (taskNum is None or self.processed < taskNum) and \
            (timeModeling is None or curEvent.time < timeModeling):
            self.eventArr = sorted(self.eventArr, key=lambda x: x.time)

            curEvent = self.eventArr.pop(0)

            if curEvent.type == EventType.GENERATOR:
                self.RunGenerator(curEvent)
            else:
                self.RunProcessor(curEvent)

        return {'endTime': curEvent.time,
                'sizeQMax': self.sizeQMax,
                'avgWait': sum(self.timeWait) / len(self.timeWait),
                'timeLoad': self.calcWorkingTime(curEvent.time) / curEvent.time / len(self.procArr)}

    def RunGenerator(self, req: Event):
        self.buf.put(req.time)
        if self.buf.qsize() > self.sizeQMax:    self.sizeQMax = self.buf.qsize()

        for i in range(len(self.procArr)):
            if self.procArr[i].IsFree():
                self.processed -= 1
                self.eventArr.append(Event(EventType.PROCESSOR, req.time, i))
                break

        self.eventArr.append(Event(EventType.GENERATOR, self.genArr[req.ind].nextTime(req.time), req.ind))

    def RunProcessor(self, req: Event):
        self.processed += 1
        self.procArr[req.ind].SetFree()

        if self.buf.empty(): return

        val = self.buf.get()
        self.timeWait.append(req.time - val)

        self.procArr[req.ind].SetBusy()
        self.eventArr.append(Event(EventType.PROCESSOR, self.procArr[req.ind].nextTime(req.time), req.ind))

        self.timeProc[self.eventArr[len(self.eventArr) - 1].time] = self.eventArr[len(self.eventArr) - 1].time - req.time
