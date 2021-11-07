from tkinter import *
from tkinter.tix import *
import matplotlib
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk
		
class PltDataFrame(Frame):
    def __init__(self, master,V_data=[],Cp_data=[],Gp_data=[]):
        ttk.Frame.__init__(self, master, padding=(10, 10, 10, 10)) # super class initialization
        self.f = Figure(figsize=(8,4), dpi=100) # figur size and dpi setting
 
    def updatePlot(self,V_data,Cp_data,Gp_data,xaxis1,xaxis2):
        """ 
        main plot setting
        containt:- 
        - subplot 
        - axis
        - plot
        - setting
        - color
        - FigureCanvasTkAgg
        """
        self.ax1 = self.f.add_subplot(111)
        self.ax2 = self.ax1.twinx()
        
        self.V_data=V_data
        self.Cp_data=Cp_data
        self.Gp_data=Gp_data
        self.cp_sq=[]
        for cp in Cp_data:
            self.cp_sq.append(1/(cp*cp))
        
        t = self.V_data 
        s1 = self.cp_sq #self.Cp_data
        s2 = self.Gp_data
        xaxis1="1/c^2"

        self.ax1.plot(t, s1, 'b-')
        self.ax1.set_title('Data Plot')
        self.ax1.set_xlabel('Voltage(V vs EM)')
        self.ax1.set_ylabel(xaxis1, color='b')
        self.ax1.tick_params('y', colors='b')
        #self.ax1.ticklabel_format(style='sci', scilimits=(0,0))
        
        
        
        self.ax2.plot(t, s2, 'r.')
        self.ax2.set_ylabel(xaxis2, color='r')
        self.ax2.tick_params('y', colors='r')
        self.ax2.ticklabel_format(style='sci',scilimits=(0,0))
        
    

        canvas = FigureCanvasTkAgg(self.f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(expand=True)
