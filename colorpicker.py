"""
File:	colorpicker.py
Date:	03.28.19
Name: 	Dan

- Lets user pick a color and gives rgb values
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
	def __init__(self):
		"""Displays the results of picking a color"""
		EasyFrame.__init__(self, title = "Color Chooser Demo")
			
		# Labels and output fields
		self.addLabel("R", row = 0, column = 0)
		self.addLabel("G", row = 1, column = 0)
		self.addLabel("B", row = 2, column = 0)
		self.addLabel("Color", row = 3, column = 0)
			
		self.r = self.addIntegerField(value = 0, column = 1, row = 0)
		self.g = self.addIntegerField(value = 0, column = 1, row = 1)
		self.b = self.addIntegerField(value = 0, column = 1, row = 2)
		self.hex = self.addTextField(text = "#000000", column = 1, row = 3, width = 10)
			
		# Canvas with an initial black background
		self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")
			
		# Command button
		self.addButton(text = "Choose color", row = 4, column = 0, columnspan = 3, command = self. chooseColor)
			
	def chooseColor(self):
		"""Pops up a color chooser from the os and outputs the results"""
		colorTuple = tkinter.colorchooser.askcolor()
		if not colorTuple[0]:
			return
		((r, g, b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString
		
def main():
	ColorPicker().mainloop()
	
main()