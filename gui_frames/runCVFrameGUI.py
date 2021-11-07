from tkinter import *
from utils import setSignalLevelAndFrequency,runCVLoop
import numpy as np
from tkinter import ttk
from time import gmtime, strftime
		
class RunCVFrame(Frame):

    def __init__(self, master,inst_handle_1,inst_handle_2,app):
        ttk.Frame.__init__(self, master)
        self.relief = GROOVE
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.Widgets()
        self.inst_handle_1=inst_handle_1
        self.inst_handle_2=inst_handle_2
        self.parent=app
        
    def Widgets(self):   
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
        
        
        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
		

        self.dc_startL=ttk.Label(main_frame,text='Start(V):',padding=0)
        self.dc_startL.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.dc_startV=Entry(main_frame, textvariable=self.dc_start, bg='white')
        self.dc_startV.grid(row=2, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        self.dc_endL=ttk.Label(main_frame,text='End (V):',padding=0)
        self.dc_endL.grid(row=3, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.dc_endV=Entry(main_frame, textvariable=self.dc_end, bg='white')
        self.dc_endV.grid(row=3, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        # dc points			   
        self.dc_ptL=ttk.Label(main_frame,text='DC pts',padding=0)
        self.dc_ptL.grid(row=4, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.dc_ptV=Entry(main_frame, textvariable=self.dc_pts, bg='white')
        self.dc_ptV.grid(row=4, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        # timre			   
        self.dc_ptL=ttk.Label(main_frame,text='Time stp',padding=0)
        self.dc_ptL.grid(row=5, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.dc_ptV=Entry(main_frame, textvariable=self.time_pts, bg='white')
        self.dc_ptV.grid(row=5, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        #average time			   
        self.av_tL=ttk.Label(main_frame,text='AV times',padding=0)
        self.av_tL.grid(row=6, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.av_tV=Entry(main_frame, textvariable=self.av_t, bg='white')
        self.av_tV.grid(row=6, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

		#Impidance  Rng		   
        self.Imp_RngL=ttk.Label(main_frame,text='Imp Rng',padding=0)
        self.Imp_RngL.grid(row=7, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.Imp_RngV=Entry(main_frame, textvariable=self.imp_rng, bg='white')
        self.Imp_RngV.grid(row=7, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
		
		#Imp Auto Rng			   
        self.auto_range = ttk.Checkbutton(main_frame, text="Imp Auto Rng?",
                        variable=self.aut_rng)
        self.auto_range.grid(row=8, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        
        self.imp_typeL=ttk.Label(main_frame,text='ImpType:',padding=0)
        self.imp_typeL.grid(row=9, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.load_typeV= ttk.Combobox(main_frame, 
		                values=["Auto","Manual"])
        self.load_typeV.grid(row=9, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        self.speedL=ttk.Label(main_frame,text='Speed:',padding=0)
        self.speedL.grid(row=10, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.integ_timeV= ttk.Combobox(main_frame, 
		values=["LOW","MED","HIGH"])
        self.integ_timeV.grid(row=10, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S) 

       
        self.run_Button=ttk.Button(main_frame,text='Run',command=self.runCVMeasurements)
        self.run_Button.grid(row=11, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        
    def updateInstHandle(self,handle_1,handle_2):
        self.inst_handle_1=handle_1	
        self.inst_handle_2=handle_2	
        
    def updateFileName(self,filename):
        self.filename=filename
        
    def runCVMeasurements(self):
        
        print ("setIntegrationTime....")
        print ("Run CV....")
        vBias = VBias = np.linspace(self.dc_start.get(),self.dc_end.get(),int(self.dc_pts.get())) #V
        runCVLoop(self.inst_handle_1,self.inst_handle_2,VBias,self.filename,self.parent,self.time_pts.get())
        print('Done')