#    ConDNAdo - Conversor de archivos de secuencias de ADN
#    Copyright (C) 2011  Horacio G. de Oro <hgdeoro@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import Tkinter, Tkconstants, tkFileDialog

from Bio import SeqIO

class TkFileDialog(Tkinter.Frame):

  def __init__(self, root):

    Tkinter.Frame.__init__(self, root)

    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    # define buttons
    Tkinter.Button(self, text='Seleccion archivo de origen', command=self.askopenfile).pack(**button_opt)
    #Tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
    #Tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
    Tkinter.Button(self, text='Seleccion archivo destino', command=self.asksaveasfilename).pack(**button_opt)
    #Tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)

    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '' # couldn't figure out how this works
    options['filetypes'] = [('all files', '.*'),]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = ''
    options['parent'] = root
    options['title'] = 'Seleccion de archivo...'

    # This is only available on the Macintosh, and only when Navigation Services are installed.
    #options['message'] = 'message'

    # if you use the multiple file version of the module functions this option is set automatically.
    #options['multiple'] = 1

  def askopenfile(self):

    """Returns an opened file in read mode."""

    return tkFileDialog.askopenfile(mode='r', **self.file_opt)

    #  def askopenfilename(self):
    #
    #    """Returns an opened file in read mode.
    #    This time the dialog just returns a filename and the file is opened by your own code.
    #    """
    #
    #    # get filename
    #    filename = tkFileDialog.askopenfilename(**self.file_opt)
    #
    #    # open file on your own
    #    if filename:
    #      return open(filename, 'r')

    #  def asksaveasfile(self):
    #
    #    """Returns an opened file in write mode."""
    #
    #    return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

  def asksaveasfilename(self):

    """Returns an opened file in write mode.
    This time the dialog just returns a filename and the file is opened by your own code.
    """

    # get filename
    filename = tkFileDialog.asksaveasfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'w')

    #  def askdirectory(self):
    #
    #    """Returns a selected directoryname."""
    #
    #    return tkFileDialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialog(root).pack()
  root.mainloop()
