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
        
        Tkinter.Label(self, text="Formato de entrada").pack(**button_opt)
        Tkinter.Text(self, height=1).pack(**button_opt)
        Tkinter.Button(self, text='Seleccion archivo de origen', command=self.select_input_file).pack(**button_opt)
        
        Tkinter.Label(self, text="Formato de salida").pack(**button_opt)
        Tkinter.Text(self, height=1).pack(**button_opt)
        Tkinter.Button(self, text='Seleccion archivo destino', command=self.select_output_file).pack(**button_opt)
        
        Tkinter.Button(self, text="Convertir", command=self.convertir).pack(**button_opt)
        
        self.status = Tkinter.Text(self, height=10, state=Tkinter.DISABLED).pack(**button_opt)
        
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '' # couldn't figure out how this works
        options['filetypes'] = [('all files', '.*'), ]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = ''
        options['parent'] = root
        options['title'] = 'Seleccion de archivo...'
        
        self.output_filename = None
        self.input_filename = None

    def render_status(self, text=""):
        self.status.config(state=Tkinter.NORMAL)
        self.status.delete(1.0, Tkinter.END)
        self.status.insert(Tkinter.END, text)
        self.status.config(state=Tkinter.DISABLED)

    def select_input_file(self):
        self.input_filename = tkFileDialog.askopenfile(mode='r', **self.file_opt)
        self.render_status()

    def select_output_file(self):
        self.output_filename = tkFileDialog.asksaveasfilename(**self.file_opt)
        self.render_status()

    def convertir(self):
        self.render_status("Convertido OK")

if __name__ == '__main__':
    root = Tkinter.Tk()
    TkFileDialog(root).pack()
    root.mainloop()
    
