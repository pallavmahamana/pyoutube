import sys
from sys import platform
from argparse import ArgumentParser
import logging
import curses

from .youtube import Pyoutube
from .config import PyoutubeConfig

def shell():
	version_too_old = False
	if sys.version_info[0] == 2:
		if sys.version_info < (2,7):
			version_too_old = True
		elif sys.version_info.major == 3 and sys.version_info < (3,5):
			version_too_old = True
		if version_too_old:
			print('Pyradio requires python 2.7 or 3.5+....')
			sys.exit(1)

		requested_player = ''
		parser = ArgumentParser(description="Curses based Youtube audio player")
		parser.add_argument('-s',default='',action='store_true',help="Search youtube")
		args = parser.parse_args()

		sys.stdout.flush()

		pyoutube_config = PyoutubeConfig()

		#set window title
		if platform.startswith('win'):
			import ctypes
			try:
				if pyoutube_config.locked:
					ctypes.windll.kernel32.SetConsoleTitleW("Pyoutube: Console Youtube Player (Session Locked)")
				else:
					ctyles.windll.kernel32.SetConsoleTitleW("Pyoutube: Console Youtube Player")
			except:
				pass
		else:
			try:
				if pyoutube_config.locked:
					sys.stdout.write("\x1b]2;Pyoutube: Console Youtube Player (Session Locked)\x07")
				else:
					sys.stdout.write("\x1b]2;Pyoutube: Console Youtube Player \x07")
			except:
				pass




	# Starts the youtube gui
	pyoutube = Pyoutube(pyoutube_config)


if __name__ == '__main__':
	shell()