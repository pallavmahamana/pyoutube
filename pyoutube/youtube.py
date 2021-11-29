# -*- coding: utf-8 -*-

# Pyoutube: Curses based Youtube Music Player
# http://www.github.com/pallavmahamana/pyoutube
# Pallav Mahamana

import curses
import curses.ascii
import os
import random
import logging

from datetime import datetime
from time import ctime, sleep
from .common import *
from .window_stack import Window_Stack
from platform import system

from . import player







class Pyoutube(object):
	ws = Window_stack()