from tkinter import *
from tkinter import ttk

		
class FileSaveFrame(Frame):
     
    def __init__(self, master,filename,app):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE# tkinter relief attribute.
        self.grid()# grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.parent=app
        self.filename=filename # intialize file name
        self.Widgets()
        
		
    def Widgets(self):
        """ 
        main window of the GUI 
        containt:- 
        - file_nameL 
        - corr_Button for plot clear

        """
        self.file_name=StringVar(self)
        update_filename = self.register(self.update_filename)
            
        main_frame= ttk.Frame(self, borderwidth=0, relief=GROOVE)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
		
        self.file_nameL=ttk.Label(main_frame,text='FileName/location')
        self.file_nameL.grid(row=0, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.file_nameV=ttk.Entry(main_frame, textvariable=self.file_name, 
                                width=62, 
                                validate='focusout',
                                validatecommand=update_filename)
        self.file_nameV.grid(row=0, column=1, rowspan=1, columnspan=5,
                       sticky=W + E + N + S)
        self.corr_Button=ttk.Button(main_frame,text='Clc Plt', command=self.clear_plot)
        self.corr_Button.grid(row=0, column=6, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
       
    def update_filename(self):
        """ 
        to update file name
        
        """
        self.filename=self.file_name.get()
        self.parent.updateFileName(self.filename)

    def clear_plot(self):
        """ 
        to clear plot
        
        """
        self.parent.clear_plot()
        
    def get_fileName(self):
        """ 
        to get file name
        
        """
        return self.filename