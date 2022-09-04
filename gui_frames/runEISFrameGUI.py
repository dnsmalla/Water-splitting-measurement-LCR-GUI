from tkinter import *
from tkinter import ttk
from EIS_fiting import preprocessing
from EIS_fiting.models.circuits import CustomCircuit
import matplotlib
from EIS_fiting.visualization import plot_nyquist
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image,ImageTk
		
class RunEIS(Frame):

    def __init__(self, master,app):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE # tkinter relief attribute.
        self.grid() # grid the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.parent=app
        self.Widgets()
		
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

        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
		
		
        self.calc_method1L=ttk.Label(main_frame,text='Circuit :',padding=0)
        self.calc_method1L.grid(row=0, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.calc_method1V= ttk.Combobox(main_frame, 
		values=["C","R","L","R + C || R","R + C + W || R"])
        self.calc_method1V.current(0)
        self.calc_method1V.grid(row=0, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

					   
        self.calc_method2L=ttk.Label(main_frame,text='Max iter:',padding=0)
        self.calc_method2L.grid(row=1, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.calc_method2V= ttk.Combobox(main_frame, 
		values=["100","1000","5000","10000"])
        self.calc_method2V.current(0)
        self.calc_method2V.grid(row=1, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        #free space
        self.free_1=ttk.Label(main_frame,text='',padding=0)
        self.free_1.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)

        #measurement setting button
        self.corr_Button=ttk.Button(main_frame,text='Run Fitting', command=self.set_fitting)
        self.corr_Button.grid(row=3, column=1, rowspan=2, columnspan=1,
                       sticky=W + E + N + S)


        self.textarea_ = Text(main_frame, width=50, height=10, font= ('Arial', 16, 'bold'),)
        self.textarea_.grid(row=0, column=8, rowspan=4, columnspan=8,sticky=W + E + N + S)
        self.textarea_.config(state=DISABLED)

        self.canvas= Canvas(self.textarea_, width=780, height= 150)
        self.canvas.pack(expand = True, fill = BOTH)

        # #measurement setting button
        # self.corr_Button=ttk.Button(main_frame,text='Parameters', command=self.show_)
        # self.corr_Button.grid(row=2, column=6, rowspan=3, columnspan=2,
        #                sticky=W +  N )

        
    def set_fitting(self):
        """ 
        to set up setSignalLevelAndFrequency
        to set up setCorrectionParameters
        this  help to set the correction
        """
        print ("EIS measurement setting.........")
        print ("Done")
        frequencies, Z = preprocessing.readCSV('./EIS_fiting/input_data/exampleData.csv')
        circ_string = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
        initial_guess = [.01, .01, 100, .01, .05, 100, 1]
        circuit = CustomCircuit(circ_string, initial_guess=initial_guess)
        # Now loop through data list to create circuits and fit them
        circuit.fit(frequencies, Z)
        print(circuit.parameters_)
        self.show_data(circuit.parameters_)
        Z_fit = circuit.predict(frequencies)
        self.parent.Plot_use(Z,Z_fit)

    def show_data(self,data):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        pil_image = Image.open("CR.png")
        img = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(canvas_width / 2,canvas_height / 2,  anchor=NW, image=img)
        pass

    def show_():
        pass
        
