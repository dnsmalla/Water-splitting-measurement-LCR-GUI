from tkinter import *
from utils import setSignalLevelAndFrequency,setMeasurementParameters
from tkinter import ttk
		
class CorrFrame(Frame):

    def __init__(self, master,inst_handle_1,app):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE # tkinter relief attribute.
        self.grid() # grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.parent=app
        self.Widgets()
        self.inst_handle_1=inst_handle_1 # itializing instant handling
        self.measure_type="c"
		
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
        self.clc_type1=IntVar(self)
        self.clc_type2=IntVar(self)

        self.reset=StringVar(self)
        self.inst_name=StringVar(self) # to show the insturment name
        
        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
		
		
        self.calc_method1L=ttk.Label(main_frame,text='Clc Typ1:',padding=0)
        self.calc_method1L.grid(row=0, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.calc_method1V= ttk.Combobox(main_frame, 
		values=["Cs","Z","C","CPRP","Cp","Ls","Lp"])
        self.calc_method1V.current(0)
        self.calc_method1V.grid(row=0, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

					   
        self.calc_method2L=ttk.Label(main_frame,text='Clc Typ2:',padding=0)
        self.calc_method2L.grid(row=1, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.calc_method2V= ttk.Combobox(main_frame, 
		values=["D","Rs","Rp","PHAS"])
        self.calc_method2V.current(0)
        self.calc_method2V.grid(row=1, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        #free space
        self.free_1=ttk.Label(main_frame,text='',padding=0)
        self.free_1.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        #measurement setting button
        self.corr_Button=ttk.Button(main_frame,text='Set Measurement', command=self.set_measurement)
        self.corr_Button.grid(row=3, column=1, rowspan=2, columnspan=1,
                       sticky=W + E + N + S)

    
    def updateInstHandle(self,handle_1):
        """ 
        to update the resuorce handle_1 LCR 
        
        """
        self.inst_handle_1=handle_1

    def set_measurement(self):
        """ 
        to set up setSignalLevelAndFrequency
        to set up setCorrectionParameters
        this  help to set the correction
        """
        print ("measurement setting.........")
        setMeasurementParameters(self.inst_handle_1,
        self.calc_method1V.get(),
        self.calc_method2V.get()) 
        if self.calc_method1V.get() in ["Cs", "C","CPRP","Cp"]: 
            self.measure_type="c"
        elif self.calc_method1V.get() in ["Z","Rs"]:
            self.measure_type="z" 
        else:
            self.measure_type="c"
        self.parent.update_cvmeasure()
        print(self.measure_type)
        print ("Done")
