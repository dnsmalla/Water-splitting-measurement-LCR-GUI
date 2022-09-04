from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
		
class CompareFile(Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE # tkinter relief attribute.
        self.grid() # grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.Widgets()

    def select_file(self):
        filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
        )
        f_ = fd.askopenfilenames(filetypes=filetypes,initialdir="./Data")
        # read the text file and show its content on the Text
        print("this is file name",str(f_))
        f_name=str(f_)[47:-3]
        self.file_list.append(str(f_name))
        self.text_.insert(END,"\n"+str(f_name))

    def disable_but(self):
        self.file_select_Button["state"] = DISABLED
        self.text_["state"] = DISABLED

        

		
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
        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        self.f_types=StringVar(self)
        self.file_list=[]
        self.f_types.set('*csv')
        self.calc_method2L=ttk.Label(main_frame,text='File type',padding=0)
        self.calc_method2L.grid(row=0, column=0, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
        self.file_types=Entry(main_frame, textvariable=self.f_types, bg='white')
        self.file_types.grid(row=0, column=1, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
        self.file_types["state"] = DISABLED
        self.text_ = Text(main_frame, width=40, height=8)
        self.text_.grid(row=2, column=0, rowspan=2, columnspan=2,sticky=W + E + N + S)
         #free space
        self.free_3=ttk.Label(main_frame,text='',padding=0)
        self.free_3.grid(row=5, column=0, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)

        self.file_select_Button=ttk.Button(main_frame,text='File select', command=self.select_file)
        self.file_select_Button.grid(row=6, column=1, rowspan=1, columnspan=1,
                       sticky=W +E + N + S)
        
