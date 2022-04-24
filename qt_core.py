# QT CORE
# Change for PySide Or PyQt
# ///////////////////////// WARNING: ////////////////////////////
# Remember that changing to PyQt too many modules will have 
# problems because some classes have different names like: 
# Property (pyqtProperty), Slot (pyqtSlot), Signal (pyqtSignal)
# among others.
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
import builtins

# GLOBAL VARIABLES
builtins.is_logged = False
builtins.motds = [
    "The whole point of criticism is that you are asking the other guys to do better." +
        " If you never comeback to see how they did, then it's plain old bad-mouthing.\n" +
        "~ Ibuki Suika, Lotus Eaters' Sobering, ch. 15 ~",
    "I will KILL you!\n" +
        "~ sontg ~",
]

def checkLogin(username, password):
    if username and password:
        return True
    else:
        return False

