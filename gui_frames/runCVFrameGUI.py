from tkinter import *
from utils import setSignalLevelAndFrequency,runCVLoop,runIMPLoop
import numpy as np
from tkinter import ttk
from time import gmtime, strftime
		
class RunCVFrame(Frame):

    def __init__(self, master,inst_handle_1,inst_handle_2,app,typ_c):
        ttk.Frame.__init__(self, master)
        self.relief = GROOVE
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.types_c=typ_c
        self.Widgets()
        self.inst_handle_1=inst_handle_1
        self.inst_handle_2=inst_handle_2
        self.parent=app
        print(self.types_c)
        
    def Widgets(self):  
        if self.types_c== "c":
            self.dc_start=DoubleVar(self)
            self.dc_end=DoubleVar(self)
            self.dc_pts=DoubleVar(self)
            self.imp_rng=DoubleVar(self)
            self.aut_rng=IntVar(self)
            self.av_t=IntVar(self)
            self.time_pts=IntVar(self)
            self.time_pts.set(1)
            self.av_t.set(100)  
            self.dc_end.set(1)
            self.dc_pts.set(25)
            self.imp_rng.set(1000000000000)
            self.aut_rng.set(1)
            self.filename=None
            self.ac_volt=DoubleVar(self)
            self.freq=DoubleVar(self)
            self.c_len=IntVar(self)
            self.c_len.set(1)   # to set cable length to 1 m
            self.ac_volt.set(0.001) # to set signal to 1 milivolt
            self.freq.set(1000) # to set frequency  to 1 kHz
            
            main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
            main_frame.grid()
            main_frame.grid_columnconfigure(0, weight=1)
            main_frame.grid_rowconfigure(0, weight=1)
            

            self.dc_startL=ttk.Label(main_frame,text='Start (V):',padding=0)
            self.dc_startL.grid(row=0, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.dc_startV=Entry(main_frame, textvariable=self.dc_start, bg='white')
            self.dc_startV.grid(row=0, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            self.dc_endL=ttk.Label(main_frame,text='End (V):',padding=0)
            self.dc_endL.grid(row=1, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.dc_endV=Entry(main_frame, textvariable=self.dc_end, bg='white')
            self.dc_endV.grid(row=1, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            # dc points			   
            self.dc_ptL=ttk.Label(main_frame,text='DC points',padding=0)
            self.dc_ptL.grid(row=2, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.dc_ptV=Entry(main_frame, textvariable=self.dc_pts, bg='white')
            self.dc_ptV.grid(row=2, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            # timre			   
            self.dc_ptL=ttk.Label(main_frame,text='Time step',padding=0)
            self.dc_ptL.grid(row=3, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.dc_ptV=Entry(main_frame, textvariable=self.time_pts, bg='white')
            self.dc_ptV.grid(row=3, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            #average time			   
            self.av_tL=ttk.Label(main_frame,text='AV times',padding=0)
            self.av_tL.grid(row=4, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.av_tV=Entry(main_frame, textvariable=self.av_t, bg='white')
            self.av_tV.grid(row=4, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            #Impidance  Rng		   
            self.Imp_RngL=ttk.Label(main_frame,text='Imp Range',padding=0)
            self.Imp_RngL.grid(row=5, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.Imp_RngV=Entry(main_frame, textvariable=self.imp_rng, bg='white')
            self.Imp_RngV.grid(row=5, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            self.signal_freqL=ttk.Label(main_frame,text='Freq (Hz)',padding=0)
            self.signal_freqL.grid(row=6, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            self.signal_freqV=Entry(main_frame, textvariable=self.freq, bg='white')
            self.signal_freqV.grid(row=6, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
                        
            self.ac_voltageL=ttk.Label(main_frame,text='Sig.Volt',padding=0)
            self.ac_voltageL.grid(row=7, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            self.ac_voltageV=Entry(main_frame, textvariable=self.ac_volt, bg='white')
            self.ac_voltageV.grid(row=7, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
        
            self.run_Button=ttk.Button(main_frame,text='Run CV measure',command=self.runCVMeasurements)
            self.run_Button.grid(row=8, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

        elif self.types_c=="z":
            self.frq_start=DoubleVar(self)
            self.frq_end=DoubleVar(self)
            self.frq_pts=DoubleVar(self)
            self.imp_rng=DoubleVar(self)
            self.aut_rng=IntVar(self)
            self.av_t=IntVar(self)
            self.time_pts=IntVar(self)
            self.time_pts.set(1)
            self.av_t.set(100) 
            self.frq_start.set(10000)
            self.frq_end.set(0.1)
            self.frq_pts.set(25)
            self.imp_rng.set(1000000000000)
            self.aut_rng.set(1)
            self.filename=None
            self.ac_volt=DoubleVar(self)
            self.DC=DoubleVar(self)
            self.c_len=IntVar(self)
            self.c_len.set(1)   # to set cable length to 1 m
            self.ac_volt.set(0.001) # to set signal to 1 milivolt
            self.DC.set(0.1) # to set frequency  to 1 kHz
            
            main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
            main_frame.grid()
            main_frame.grid_columnconfigure(0, weight=1)
            main_frame.grid_rowconfigure(0, weight=1)
            

            self.frq_startL=ttk.Label(main_frame,text='Start Freq:',padding=0)
            self.frq_startL.grid(row=0, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.frq_startV=Entry(main_frame, textvariable=self.frq_start, bg='white')
            self.frq_startV.grid(row=0, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            self.frq_endL=ttk.Label(main_frame,text='End Freq:',padding=0)
            self.frq_endL.grid(row=1, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.frq_endV=Entry(main_frame, textvariable=self.frq_end, bg='white')
            self.frq_endV.grid(row=1, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            # dc points			   
            self.frq_ptL=ttk.Label(main_frame,text='Freq pts',padding=0)
            self.frq_ptL.grid(row=2, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.frq_ptV=Entry(main_frame, textvariable=self.frq_pts, bg='white')
            self.frq_ptV.grid(row=2, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            # timre			   
            self.frq_stpL=ttk.Label(main_frame,text='Time stp',padding=0)
            self.frq_stpL.grid(row=3, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.frq_stpV=Entry(main_frame, textvariable=self.time_pts, bg='white')
            self.frq_stpV.grid(row=3, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            #average time			   
            self.av_tL=ttk.Label(main_frame,text='AV times',padding=0)
            self.av_tL.grid(row=4, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.av_tV=Entry(main_frame, textvariable=self.av_t, bg='white')
            self.av_tV.grid(row=4, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            #Impidance  Rng		   
            self.Imp_RngL=ttk.Label(main_frame,text='Imp Rng',padding=0)
            self.Imp_RngL.grid(row=5, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
    
            self.Imp_RngV=Entry(main_frame, textvariable=self.imp_rng, bg='white')
            self.Imp_RngV.grid(row=5, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            self.DC_vL=ttk.Label(main_frame,text='DC (V)',padding=0)
            self.DC_vL.grid(row=6, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            self.DC_vV=Entry(main_frame, textvariable=self.DC, bg='white')
            self.DC_vV.grid(row=6, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
                        
            self.ac_voltageL=ttk.Label(main_frame,text='Sig.Volt',padding=0)
            self.ac_voltageL.grid(row=7, column=0, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
            self.ac_voltageV=Entry(main_frame, textvariable=self.ac_volt, bg='white')
            self.ac_voltageV.grid(row=7, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)

            self.run_Button=ttk.Button(main_frame,text='Run Imp measure',command=self.runIMPMeasurements)
            self.run_Button.grid(row=8, column=1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
        
        
    def updateInstHandle(self,handle_1,handle_2):
        self.inst_handle_1=handle_1	
        self.inst_handle_2=handle_2	
        
    def updateFileName(self,filename):
        self.filename=filename

    def runCorrections(self):
        """ 
        to set up setSignalLevelAndFrequency
        to set up setCorrectionParameters
        this  help to set the correction
        """
        print ("Correction.........")
        setSignalLevelAndFrequency(self.inst_handle_1,
                                self.freq.get(),
                                self.ac_volt.get(),1)
        print ("Done")

    def run_setting(self):
        """ 
        to set up setSignalLevelAndFrequency
        to set up setCorrectionParameters
        this  help to set the correction
        """
        print ("Correction.........")
        setSignalLevelAndFrequency(self.inst_handle_1,
                                self.frq_start.get(),
                                self.ac_volt.get(),1)
        print ("Done")
        
    def runCVMeasurements(self):
        self.runCorrections()
        print ("setIntegrationTime....")
        print ("Run CV....")
        vBias = VBias = np.linspace(self.dc_start.get(),self.dc_end.get(),int(self.dc_pts.get())) #V
        runCVLoop(self.inst_handle_1,self.inst_handle_2,VBias,self.filename,self.parent,self.time_pts.get())
        print('Done')

    def runIMPMeasurements(self):
        self.run_setting()
        print ("Run Impedance....")
        stp=np.log10(self.frq_start.get())
        lsp=np.log10(self.frq_end.get())
        frq_g = VBias = np.logspace(stp,lsp,int(self.frq_pts.get())) #V
        runIMPLoop(self.inst_handle_1,self.inst_handle_2,frq_g,self.filename,self.parent,self.time_pts.get())
        print('Done')