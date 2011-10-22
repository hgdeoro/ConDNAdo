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

import logging
import time

from multiprocessing import Process, Queue
from Queue import Empty

import Tkinter, Tkconstants, tkFileDialog, tkMessageBox

from Bio import SeqIO

def convertir_archivos(input_filename, input_format, output_filename, output_format, conv_process_queue):
    try:
        logging.info("Iniciando conversion...")
        count = SeqIO.convert(input_filename, input_format, output_filename, output_format)
        logging.info("Conversion finalizada!")
        conv_process_queue.put("OK")
    except Exception, e:
        logging.error("Excepcion detectada al intentar conversion")
        conv_process_queue.put("ERROR: %s" % str(e))

class TkFileDialog(Tkinter.Frame):

    def __init__(self, root):
        
        Tkinter.Frame.__init__(self, root)
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
        
        Tkinter.Label(self, text="Formato de entrada").pack(**button_opt)
        self.input_format_widget = Tkinter.Text(self, height=1)
        self.input_format_widget.pack(**button_opt)
        
        Tkinter.Button(self, text='Seleccion archivo de origen', command=self.select_input_file).pack(**button_opt)
        
        Tkinter.Label(self, text="Formato de salida").pack(**button_opt)
        
        self.output_format_widget = Tkinter.Text(self, height=1)
        self.output_format_widget.pack(**button_opt)
        
        Tkinter.Button(self, text='Seleccion archivo destino', command=self.select_output_file).pack(**button_opt)
        
        Tkinter.Button(self, text="Convertir", command=self.convertir).pack(**button_opt)
        
        self.status_widget = Tkinter.Text(self, height=10, state=Tkinter.DISABLED)
        self.status_widget.pack(**button_opt)
        
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
        if not text:
            input_format = self.get_input_format()
            output_format = self.get_output_format()
            widget_text = \
"""Archivo de entrada: %s
Formato de entrada: %s
Archivo de salida: %s
Formato de salida: %s
""" % (self.input_filename, input_format, self.output_filename, output_format)
        widget_text = ""
        if text:
            widget_text += "\n\n"
            widget_text += text
        self.status_widget.config(state=Tkinter.NORMAL)
        self.status_widget.delete(1.0, Tkinter.END)
        self.status_widget.insert(Tkinter.END, widget_text)
        self.status_widget.config(state=Tkinter.DISABLED)

    def select_input_file(self):
        self.input_filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.render_status()

    def select_output_file(self):
        self.output_filename = tkFileDialog.asksaveasfilename(**self.file_opt)
        self.render_status()
    
    def get_input_format(self):
        input_format = self.input_format_widget.get(1.0, Tkinter.END)
        return input_format.splitlines()[0].strip()

    def get_output_format(self):
        output_format = self.output_format_widget.get(1.0, Tkinter.END)
        return output_format.splitlines()[0].strip()
    
    def convertir(self):
        if not self.input_filename or not self.output_filename:
            tkMessageBox.showerror("Conversion", "Falta seleccionar el archivo de entrada o salida")
            return
        
        input_format = self.get_input_format()
        output_format = self.get_output_format()
        if not input_format or not output_format:
            tkMessageBox.showerror("Conversion", "Falta seleccionar el formato de entrada o salida")
            return

        self.render_status("Iniciando conversion...")
        
        conv_process_queue = Queue()
        
        
        conv_process = Process(target=convertir_archivos, args=(self.input_filename, input_format,
            self.output_filename, output_format, conv_process_queue, ))
        conv_process.daemon = True
        conv_process.start()
        
        logging.info("ConversorProcess start()'eado")
        
        self.render_status("Conversion en proceso...")
        
        while True:
            logging.debug("En bucle...")
            try:
                ret = conv_process_queue.get(False)
                logging.info("Saliendo de bucle...")
                break
            except Empty:
                self.update_idletasks()
                time.sleep(0.5) # 0.5 seg.
        
        logging.info("Haciendo join()")
        conv_process.join()
        
        logging.info("join() OK")
        self.render_status("PROCESO FINALIZADO\n\nResultado: %r" % ret)
        
        #        if conv_process.ext:
        #            self.render_status("Error detectado al intentar conversion")
        #        else:
        #            self.render_status("TERMINADO! Se convirtieron %d registros" % conv_process.count)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    root = Tkinter.Tk()
    TkFileDialog(root).pack()
    root.mainloop()
