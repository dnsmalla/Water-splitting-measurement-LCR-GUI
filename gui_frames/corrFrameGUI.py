from tkinter import *
from utils import setCorrectionParameters,setSignalLevelAndFrequency
from tkinter import ttk
		
class CorrFrame(Frame):

    def __init__(self, master,inst_handle_1):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE # tkinter relief attribute.
        self.grid() # grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.Widgets()
        self.inst_handle_1=inst_handle_1 # itializing instant handling
		
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
        self.ac_volt=DoubleVar(self)
        self.freq=DoubleVar(self)
        self.c_len=IntVar(self)
        self.c_len.set(1)   # to set cable length to 1 m
        self.ac_volt.set(0.001) # to set signal to 1 milivolt
        self.freq.set(1000) # to set frequency  to 1 kHz
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

        self.c_lenL=ttk.Label(main_frame,text='Cable len:',padding=0)
        self.c_lenL.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.c_lenV=Entry(main_frame, textvariable=self.c_len, bg='white')
        self.c_lenV.grid(row=2, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S) 


        self.signal_freqL=ttk.Label(main_frame,text='Freq(Hz)',padding=0)
        self.signal_freqL.grid(row=3, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.signal_freqV=Entry(main_frame, textvariable=self.freq, bg='white')
        self.signal_freqV.grid(row=3, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
					   
        self.ac_voltageL=ttk.Label(main_frame,text='Sig.Volt',padding=0)
        self.ac_voltageL.grid(row=4, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.ac_voltageV=Entry(main_frame, textvariable=self.ac_volt, bg='white')
        self.ac_voltageV.grid(row=4, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
   
        

        self.corr_Button=ttk.Button(main_frame,text='Correct', command=self.runCorrections)
        self.corr_Button.grid(row=6, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
    
    def updateInstHandle(self,handle_1):
        """ 
        to update the resuorce handle_1 LCR 
        
        """
        self.inst_handle_1=handle_1
		
    def runCorrections(self):
        """ 
        to set up setSignalLevelAndFrequency
        to set up setCorrectionParameters
        this  help to set the correction
        """
        print ("Correction.........")
        setSignalLevelAndFrequency(self.inst_handle_1,
                                self.freq.get(),
                                self.ac_volt.get())
        setCorrectionParameters(self.inst_handle_1,
        self.calc_method1V.get(),
        self.calc_method2V.get(),
        self.c_len.get(),) 
        print ("Done")
		
       