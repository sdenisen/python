import time
from HomeExplorerEngine.WSController.engine_controller import EngineController

__author__ = 'sdeni'


ec = EngineController()

ec.goForward()
time.sleep(5)
ec.stopAction()
time.sleep(5)
ec.goBackward()
time.sleep(5)


ec.stopAction()
time.sleep(1)
print ("stop - all - motors")
ec.cleanup()
