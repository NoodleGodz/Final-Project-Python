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
from PySide6.QtCharts import *
from Elec_Database import *
from Main_Menu import Main_Menu
import builtins
import datetime
import random

# GLOBAL VARIABLES
builtins.mm = Main_Menu()
builtins.is_logged = False
builtins.motds = [
    "The whole point of criticism is that you are asking the other guys to do better." +
        " If you never comeback to see how they did, then it's plain old bad-mouthing.\n" +
        "~ Ibuki Suika, Lotus Eaters' Sobering, ch. 15 ~",
    "I will KILL you!\n" +
        "~ sontg ~",
    "F-you, cuty designer!\n" + 
        "~ rashlight, The Sonoric Ones ~",
    "The instruments of science do not in themselves discover truth.  And there are " +
    "searchings that are not concluded by the coincidence of a pointer and a mark.\n" +
        "~ Fred Saberhagen, \"The Berserker Wars\" ~",
    "understand, v.:\n"+
	    "To reach a point, in your investigation of some subject, at which " +
	    "you cease to examine what is really present, and operate on the " + 
	    "basis of your own internal model instead."
]