# Copyright (C) 2009, 2010  Roman Zimbelmann <romanz@lavabit.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Console-based visual file manager.

Ranger is a file manager with an ncurses frontend written in Python.
It is designed to give you a broader overview of the file system by
displaying previews and backviews, dividing the screen into columns.

The keybindings are similar to those of other console programs like
vim, mutt or ncmpcpp so the usage will be intuitive and efficient.
"""

from os import path, environ
from ranger.ext.openstruct import OpenStruct
from sys import argv
from ranger.core.main import main

# Information
__license__ = 'GPL3'
__version__ = '1.3.0'
__author__ = __maintainer__ = 'Roman Zimbelmann'
__email__ = 'romanz@lavabit.com'

# Constants
USAGE = '%prog [options] [path/filename]'
RANGERDIR = path.dirname(__file__)
LOGFILE = '/tmp/errorlog'
if 'XDG_CONFIG_HOME' in environ and environ['XDG_CONFIG_HOME']:
	DEFAULT_CONFDIR = environ['XDG_CONFIG_HOME'] + '/ranger'
else:
	DEFAULT_CONFDIR = '~/.config/ranger'
DEBUG = ('-d' in argv or '--debug' in argv) and ('--' not in argv or
	(('-d' in argv and argv.index('-d') < argv.index('--')) or
	('--debug' in argv and argv.index('--debug') < argv.index('--'))))

# Get some valid arguments before actually parsing them in main()
#arg = OpenStruct(debug=DEBUG, clean=False, confdir=DEFAULT_CONFDIR,
#		mode=0, flags='', targets=[])


# Clean up
del environ, OpenStruct, argv
