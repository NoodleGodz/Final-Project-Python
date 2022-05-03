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
builtins.is_edit_mode = False
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
	    "basis of your own internal model instead.",
    "Practice makes perfect.\n" +
        "~ Unknown ~",
    "You only live once, but if you do it right, once is enough.\n"
        "~ Mae West ~",
    "Insanity is doing the same thing, over and over again, but expecting different results.\n"
        "~ Narcotics Anonymous ~",
    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\n"
        "~ Albert Einstein ~",
    "It does not do to dwell on dreams and forget to live.\n"
        "~ J.K. Rowling, Harry Potter and the Sorcerer's Stone ~",
    "Good friends, good books, and a sleepy conscience: this is the ideal life.\n"
        "~ Mark Twain ~",
    "Life is what happens to us while we are making other plans.\n"
        "~ Allen Saunders ~",
    "Everything you can imagine is real.\n"
        "~ Pablo Picasso ~",
    "Sometimes the questions are complicated and the answers are simple.\n"
        "~ Dr. Seuss ~",
    "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "~ Woody Allen ~",
    "Life isn't about finding yourself. Life is about creating yourself.\n"
        "~ George Bernard Shaw ~",
    "You should learn from your competitor, but never copy. Copy and you die.\n"
        "~ Jack Ma ~",
    "But better to get hurt by the truth than comforted with a lie.\n"
        "~ Khaled Hosseini ~",
    "We are all in the gutter, but some of us are looking at the stars.\n"
        "~ Oscar Wilde ~",
    "This too, shall pass.\n"
        "~ Anonymous ~",
    "Marriage is a three ring circus: engagement ring, wedding ring, and suffering.\n"
		"~ Roger Price ~",
    "Any time things appear to be going better, you have overlooked something.\n"
        "~ Anonymous ~",
    "I have many CHARTS and DIAGRAMS..\n"
        "~ Anonymous ~"
]