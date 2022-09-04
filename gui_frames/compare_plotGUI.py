from tkinter import *
from tkinter.tix import *
import matplotlib
import pandas as pd
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk

class ComparePlot(Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding=(1, 1, 1, 1)) # super class initialization
        self.f = Figure(figsize=(80,30), dpi=100) # figur size and dpi setting
 
    def plot_compare(self,files):
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
        for file in files:
            data=pd.read_csv("./Data/"+file, index_col=0)
            print(data.columns)
            v=data.loc[:,"  Vs Ag/AgCl "].values
            c=data.loc[:,"Cp(F)"].values
            self.ax1.plot(v, c, label=file)
            self.ax1.set_title('Data Plot')
            self.ax1.set_xlabel('Voltage(V vs EM)')

        self.ax1.legend()
        self.ax1.set_ylabel("1/C^2 [F cm^4] ", color='b')
        self.ax1.set_xlabel(" Potential (V vs. Ag/AgCl ", color='b')
        self.ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))

        canvas = FigureCanvasTkAgg(self.f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(expand=True)

    