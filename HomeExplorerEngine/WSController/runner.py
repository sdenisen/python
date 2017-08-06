import time
from WSController import engine_controller

__author__ = 'sdeni'


ec = engine_controller()

ec.goForward()
time.sleep(5)
ec.stop()
time.sleep(5)
ec.goBackward()
time.sleep(5)


ec.stop()
time.sleep(1)
print ("stop - all - motors")
ec.cleanup()
