import time
import logging

from detection import ObjectDetector
from robotarm import Robotarm
from conveyorbelt import ConveyorBeltControl as cc
from schranke import Schranke
from api_usage import API

robotarm = Robotarm()
object_detector = ObjectDetector()
cc = cc()
schranke = Schranke()

#first block

cc.block(1, 4, 5, 6)
cc.start_all()

for i in range (1, 4):
    cc.wait_until_detected(5)

    robotarm.pick_up_block_n(i)

    cc.unblock(5)
    cc.sleep(1)
    cc.block(5)

    cc.wait_until_detected(4)

    #detect object
    schranke.close()
    #detected

    cc.unblock(4)
    cc.sleep(1)
    cc.block(4)

    cc.wait_until_detected(3)






