# GUI Application automation and testing library
# Copyright (C) 2006 Mark Mc Mahon
#
# This library is free software; you can redistribute it and/or 
# modify it under the terms of the GNU Lesser General Public License 
# as published by the Free Software Foundation; either version 2.1 
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public 
# License along with this library; if not, write to the 
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330, 
#    Boston, MA 02111-1307 USA 

#import os
import time

from pywinauto import application

from pywinauto import tests



def WindowsMedia():
	
	app = application.Application()

	app._connect(path = ur"C:\Program Files\Windows Media Player\wmplayer.exe")
	
	app.WindowsMediaPlayer.MenuSelect("View->GoTo->Library")
	app.WindowsMediaPlayer.MenuSelect("View->Choose Columns")
	
	for ctrl in app.ChooseColumns.Children:
		print ctrl.Class
	
	
	print "Is it checked already:", app.ChooseColumsn.ListView.IsChecked(1)
	
	# Check an Item in the listview
	app.ChooseColumns.ListView.Check(1)
	time.sleep(.5)
	print "Shold be checked now:", app.ChooseColumsn.ListView.IsChecked(1)

	# Uncheck it
	app.ChooseColumns.ListView.UnCheck(1)
	time.sleep(.5)
	print "Should not be checked now:", app.ChooseColumsn.ListView.IsChecked(1)

	# Check it again
	app.ChooseColumns.ListView.Check(1)
	time.sleep(.5)
	
	app.ChooseColumsn.Cancel.Click()


def Main():
	start = time.time()
	
	WindowsMedia()
	
	print "Total time taken:", time.time() - start

if __name__ == "__main__":
	Main()