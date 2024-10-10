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
schranke = Schranke(18)

#first block
now = True
schranke.open()
try:
    cc.block(1, 4, 5, 6)
    cc.move_all()

    for i in range (1, 4):
        cc.wait_until_detected(5)

        robotarm.pick_up_block_n(i)

        cc.unblock(5)
        time.sleep(1)
        cc.block(5)

        cc.wait_until_detected(4)

        #detect object
        if now :
            schranke.close()
        else:
            schranke.open()
        now = not now
        #detected

        cc.unblock(4)
        time.sleep(1)
        cc.block(4)

        cc.wait_until_detected(3)
finally:
    
    cc.wait_until_detected(2)
    cc.stop_all()
    cc.block(6, 5, 4)





