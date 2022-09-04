from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
		
class CompareSetting(Frame):

    def __init__(self, master,file_,parent):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE # tkinter relief attribute.
        self.grid() # grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.file_obj=file_
        self.f_no=int(len(file_.file_list))
        self.f_list=file_.file_list
        self.parent=parent
        self.Widgets()

    def compare_plot(self):
        self.f_no.set(str(len(self.f_list)))
        #self.parent.update_()
        self.parent.plot_compare(self.f_list)
        self.file_obj.disable_but()
        self.file_select_Button["state"] = DISABLED
        self.parent.update_status('Compare Done')
        self.file_nos["state"] = DISABLED

		
    def Widgets(self):
        """ 
        main window of the GUI 
        containt:- 
        - calc_method1 
        - calc_method2
        - cable_length
        - signal_frequency
        - signal_voltage
        - and correction button

        """
        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=12)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        self.f_no=StringVar(self)
        self.f_types=StringVar(self)

        self.file_select=ttk.Label(main_frame,text='File selected',padding=0)
        self.file_select.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
        self.file_nos=Entry(main_frame, textvariable=self.f_no, bg='white')
        self.file_nos.grid(row=2, column=1, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
       
         #free space
        self.free_3=ttk.Label(main_frame,text='',padding=0)
        self.free_3.grid(row=3, column=0, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)

        self.file_select_Button=ttk.Button(main_frame,text='Compare plot', command=self.compare_plot)
        self.file_select_Button.grid(row=5, column=1, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
        
