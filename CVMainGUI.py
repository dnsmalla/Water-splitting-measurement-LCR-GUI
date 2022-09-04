#!/usr/bin/python
# -*- coding: utf-8 -*-
#importing tkinter library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#importing frame work 
from gui_frames.initFrameGUI import InitFrame
from gui_frames.runCVFrameGUI import RunCVFrame
from gui_frames.fileSaveFrameGUI import FileSaveFrame
from gui_frames.pltDataFrameGUI import PltDataFrame
from gui_frames.corrFrameGUI import CorrFrame
from gui_frames.runEISFrameGUI import RunEIS
from gui_frames.compare_fileSelectGUI import CompareFile
from gui_frames.compare_plotGUI import ComparePlot
from gui_frames.compare_settingGUI import CompareSetting
from utils import close_

#initialize tkinter
root = Tk()
#add image icon at top
ico = Image.open('nf.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Create and grid the outer content frame
mainFrame = ttk.Frame(root, padding=(10, 10, 10, 10))
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_rowconfigure(0, weight=3)
#added name in the title
mainFrame.master.title('NF - ZM2372 -Instrument Driver')

# Class Application inherits ttk.Frame

class Application(ttk.Frame):

    def __init__(self, master=None,inst_handle_1=None,inst_handle_2=None,file_name=None):
        ttk.Frame.__init__(self, master) # super class initialization
        self.inst_handle_1=inst_handle_1 # initalize the instant handle 1 for LCR meter
        self.inst_handle_2=inst_handle_2  # initalize the instant handle 2 for multi-meter
        self.file_name=file_name ## initalize the file name to save data
        self.v_=" Ag/Agcl"  ## initalize data show column 0
        self.x_="x_data"    ## initalize data show column 1
        self.y_="y_data"    ## initalize data show column 2
        self.d_col=4        ## initalize data column size
        self.grid()         ## initalize tkinter grid function to grid the window
        self.compare=0
        self.fitting=0
        for r in range(14):  ## initalize row size
            self.master.rowconfigure(r, weight=1)
        for c in range(22): ## initalize column size
            self.master.columnconfigure(c, weight=1)
        self.mainWidgets()
		
    def mainWidgets(self):
        """ 
        main window of the GUI 
        containt:- 
        - initFrame 
        - corrFrame
        - runCVFrame
        - fileSaveFrame
        - Data_Frame
        - pltDataFrame

        """
        self.initFrame = InitFrame(master=mainFrame,inst_handle_1=self.inst_handle_1,inst_handle_2=self.inst_handle_2, app=self)
        self.initFrame.grid(row=0, column=0, rowspan=2, columnspan=2,
                       sticky=W + E + N + S)
        if self.compare==0:
            self.corrFrame = CorrFrame(master=mainFrame,inst_handle_1=self.inst_handle_1,app=self)
            self.corrFrame.grid(row=2, column=0, rowspan=3, columnspan=2,
                        sticky=W + E + N + S)
            self.runCVFrame = RunCVFrame(master=mainFrame,inst_handle_1=self.inst_handle_1,inst_handle_2=self.inst_handle_2,app=self,typ_c=self.corrFrame.measure_type)
            self.runCVFrame.grid(row=5, column=0, rowspan=11, columnspan=2,
                        sticky=W + E + N + S)

            self.fileSaveFrame = FileSaveFrame(master=mainFrame,filename=self.file_name, app=self)
            self.fileSaveFrame.grid(row=0, column=2, rowspan=1, columnspan=8,
                        sticky=W + E + N + S)

            self.Data_Frame = self.data_frame()
            self.Data_Frame.grid(row=1, column=2, rowspan=14, columnspan=self.d_col,
                        sticky= W )  

            self.pltDataFrame = PltDataFrame(master=mainFrame)
            self.pltDataFrame.grid(row=1, column=6, rowspan=14, columnspan=12,
                        sticky= W + E + N + S)
            
            self.status = self.sts_txt()
            self.status.grid(row=14, column=6, rowspan=1, columnspan=10,
                        sticky= W + E + N + S) 
        else:
            self.compare_file=CompareFile(master=mainFrame)
            self.compare_file.grid(row=2, column=0, rowspan=6, columnspan=2,
                        sticky=W + N )
            self.compare_setting=CompareSetting(master=mainFrame,file_=self.compare_file,parent=self)
            self.compare_setting.grid(row=8, column=0, rowspan=5, columnspan=2,
                        sticky=W + N )
            self.title_=self.title_compare()
            self.title_.grid(row=0, column=2, rowspan=2, columnspan=8,
                        sticky=W+N)
            self.compare_plot=ComparePlot(master=mainFrame)
            self.compare_plot.grid(row=1, column=2, rowspan=12, columnspan=22,
                    sticky=E+N)
            self.status = self.sts_txt()
            self.status.grid(row=14, column=6, rowspan=1, columnspan=7,
                        sticky= E+S)
        
    def update_cvmeasure(self):
        self.runCVFrame = RunCVFrame(master=mainFrame,inst_handle_1=self.inst_handle_1,inst_handle_2=self.inst_handle_2,app=self,typ_c=self.corrFrame.measure_type)
        self.runCVFrame.grid(row=5, column=0, rowspan=11, columnspan=2,
                       sticky=W + E + N + S)
        #if self.status=="END" and self.corrFrame.measure_type=="z":
        if self.corrFrame.measure_type=="z":
            self.run_Button=ttk.Button(self.status,text='EIS fitting',command=self.add_fitting)
            self.run_Button.grid(row=1, column=0, rowspan=1, columnspan=1,
                       sticky=W + N + S)

    def compare_mode(self):
        self.compare=1
        self.fileSaveFrame.destroy()
        self.corrFrame.destroy()
        self.runCVFrame.destroy()
        self.Data_Frame.destroy()
        self.pltDataFrame.destroy()
        self.status.destroy()
        self.update_()
        self.compare_file=CompareFile(master=mainFrame)
        self.compare_file.grid(row=2, column=0, rowspan=6, columnspan=2,
                    sticky=W + N )
        self.compare_setting=CompareSetting(master=mainFrame,file_=self.compare_file,parent=self)
        self.compare_setting.grid(row=8, column=0, rowspan=5, columnspan=2,
                    sticky=W + N )
        self.title_=self.title_compare()
        self.title_.grid(row=0, column=2, rowspan=2, columnspan=8,
                        sticky=W+N)
        self.compare_plot=ComparePlot(master=mainFrame)
        self.compare_plot.grid(row=0, column=2, rowspan=12, columnspan=22,
                    sticky=E+N)
        self.status = self.sts_txt()
        self.status.grid(row=14, column=6, rowspan=1, columnspan=7,
                        sticky= E+S)

        self.update_()

    def clear_compare_plot(self):
        """ 
        to clear the plot 

        """
        self.compare_plot.destroy()
        self.compare_plot=ComparePlot(master=mainFrame)
        self.compare_plot.grid(row=2, column=2, rowspan=12, columnspan=22,
                    sticky=E+S )
        

    def plot_compare(self,files):
        self.compare_plot.plot_compare(files)
        self.update_()

    def title_compare(self):
        """ 
        
        """
        self.title_c="   "
        self.t_compare= ttk.Frame(mainFrame, borderwidth=2, relief=GROOVE, padding=5)
        self.t_compare.grid_columnconfigure(0, weight=1)
        self.t_compare.grid_rowconfigure(0, weight=1)
        self.update_()
        self.c_1=ttk.Label(self.t_compare,text=" -----  -----   ----    compare plot here below  in this area      ------ -----  ------       ",padding=0)
        self.c_1.grid(row=0, column=3, rowspan=1, columnspan=25,
                       sticky=W + E + N + S)
        self.file_types=Entry(self.t_compare, textvariable=self.title_c, bg='white')
        self.file_types.grid(row=0, column=28, rowspan=1, columnspan=7,
                       sticky=W +E + N + S)
        self.c_2=ttk.Label(self.t_compare,text=" -----  -----   ----    ---------------------------------------      ------ -----  ------       ",padding=0)
        self.c_2.grid(row=1, column=3, rowspan=1, columnspan=25,
                       sticky=W + E + N + S)
    
        return self.t_compare

    def add_fitting(self):
        if self.fitting==0:
            root.attributes("-fullscreen", True)
            self.fitting_Frame = RunEIS(master=mainFrame,app=self)
            self.fitting_Frame.grid(row=15, column=0, rowspan=11, columnspan=20,
                        sticky=W + E + N + S )
            self.fitting=1

    def clear_plot(self):
        """ 
        to clear the plot 

        """
        self.pltDataFrame.destroy()
        self.pltDataFrame = PltDataFrame(master=mainFrame)
        self.pltDataFrame.grid(row=1, column=3+self.d_col, rowspan=14, columnspan=8,
                      sticky= N)
                      
    def updateInstHandle(self,handle_1,handle_2):
        """ 
        to update the resuorce handle 
        there are 
        handle_1 for LCR meter
        handle_2 for multi meter
        
        """
        self.inst_handle_1=handle_1
        self.inst_handle_2=handle_2
        self.corrFrame.updateInstHandle(handle_1)
        self.runCVFrame.updateInstHandle(handle_1,handle_2)

    def update_(self):
        """ 
        to update the entire GUI
        
        """
        self.master.update()

    def up_d_data(self,frame):
        """ 
        to update the data frame
        
        """
        self.Data_Frame = frame
        self.Data_Frame.grid(row=1, column=2, rowspan=14, columnspan=self.d_col,
                      sticky= N)
        
    def updateFileName(self,filename):
        """ 
        to update the updateFileName
        
        """
        self.file_name=filename
        self.runCVFrame.updateFileName(filename)
        
    def clear_data(self):
        """ 
        to clear data in the GUI
        
        """
        self.textarea1.config(state=NORMAL)
        self.textarea1.delete('1.0', END)

    def update_status(self,status):
        """ 
        to clear Status in the GUI according to instrument status
        
        """
        self.textarea22.config(state=NORMAL)
        self.textarea22.delete('1.0', END)
        self.textarea22.insert(END,"  "+status)

    def update_data(self,freq,V_data,Cp_data,j):
        """ 
        to update the data in GUI
        data:-
        - Ag/Agcl
        - Calculation 1 data 
        - calculation 2 data
        """
        self.textarea1.config(state=NORMAL)
        em_t="{:2.1f}".format(freq)
        cp_t="{:.2e}".format(Cp_data)
        v_t= "{:.2e}".format(V_data)
        txt=' '+str(em_t)+'  '+str(v_t)+"  "+str(cp_t)
        self.textarea1.insert(END,"\n"+txt)

    def No_update(self):
        """ 
        to set the text area disable
        
        """
        self.textarea1.config(state=DISABLED)
        self.textarea22.config(state=DISABLED)
        
    def update_x_y(self,xaxis1,xaxis2):
        """ 
        to update GUI data column according to Cal 1 and cal 2
        
        """
        self.c_1=ttk.Label(self.data_f,text=xaxis1,padding=0)
        self.c_1.grid(row=1, column=self.d_col-2, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)
        self.c_2=ttk.Label(self.data_f,text=xaxis2,padding=0)   
        self.c_2.grid(row=1, column=self.d_col-1, rowspan=1, columnspan=1,
                        sticky=W + E + N + S)	
    
    def updatePlot(self,V_data,Cp_data,Gp_data,xaxis1,xaxis2):
        """ 
        to update plot using data  ag/agcl , Cal 1, cal 2
        
        """
        self.pltDataFrame.updatePlot(V_data,Cp_data,Gp_data,xaxis1,xaxis2)

    def updatePlot_imp(self,frq,Cp_data,Gp_data,xaxis1,xaxis2):
        """ 
        to update plot using data  ag/agcl , Cal 1, cal 2
        
        """
        self.pltDataFrame.updatePlot_imp(frq,Cp_data,Gp_data,xaxis1,xaxis2)

    def Plot_use(self,Z,Z_fit):
        """ 
        to update plot using plot
        
        """
        self.clear_plot()
        self.pltDataFrame.showPlot(Z,Z_fit)


    def use_c(self):
        """ 
        to cleare the GUI for restart
        
        """
        if self.compare==1:
            self.clear_compare_plot()
            self.compare_file.destroy()
            self.compare_setting.destroy()
            self.title_.destroy()
        elif self.fitting:
            self.fitting_Frame.destroy()
            self.fitting=0
        else:
            self.fileSaveFrame.destroy
            self.corrFrame.destroy()
            self.Data_Frame.destroy()
            self.clear_plot()

        self.clear_plot()
        self.compare=0
        self.mainWidgets()
        #close_(self)
        self.master.update()
        self.mainWidgets()
        close_(self)
        self.update_()


    def data_frame(self):
        """ 
        setup data frame and using  scrollbar1
        - text lable 3
        - textarea1
        
        """
        self.n=25
        self.data_f= ttk.Frame(mainFrame, borderwidth=2, relief=GROOVE, padding=5)
        self.data_f.grid_columnconfigure(0, weight=1)
        self.data_f.grid_rowconfigure(0, weight=1)
        scrollbar = Scrollbar(self.data_f)
        self.update_()
        if self.initFrame.gpib2.get():
            self.c_0=ttk.Label(self.data_f,text=self.v_,padding=0)
            self.c_0.grid(row=1, column=self.d_col-3, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.c_1=ttk.Label(self.data_f,text=self.x_,padding=0)
        self.c_1.grid(row=1, column=self.d_col-2, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.c_2=ttk.Label(self.data_f,text=self.y_,padding=0)
        self.c_2.grid(row=1, column=self.d_col-1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.scrollbar1 = Scrollbar(self.data_f)
        self.textarea1 = Text(self.data_f, width=7*self.d_col, height=36)
        self.textarea1.grid(row=2, column=1, rowspan=20, columnspan=self.d_col,sticky=W + E + N + S)
        self.textarea1.config(yscrollcommand=self.scrollbar1.set)
        self.textarea1.config(state=DISABLED)
        
        return self.data_f

    def sts_txt(self):
        """ 
        setup Gui status in the cornet bottom
        - using button to clear the all setting
        - textarea2 for show status
        
        """
        self.sts_f= ttk.Frame(mainFrame, borderwidth=2, relief=GROOVE, padding=3)
        self.sts_f.grid_columnconfigure(0, weight=1)
        self.sts_f.grid_rowconfigure(0, weight=1)

        self.run_Button=ttk.Button(self.sts_f,text='Exit',command=self.use_c)
        self.run_Button.grid(row=1, column=1, rowspan=1, columnspan=1,
                       sticky=W + N + S)
        self.cc=ttk.Label(self.sts_f,text=" Status ",padding=0)
        self.cc.grid(row=1, column=2, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.textarea22 = Text(self.sts_f, width=30, height=1, font= ('Arial', 16, 'bold'),)
        self.textarea22.grid(row=1, column=3, rowspan=1, columnspan=6,sticky=W + E + N + S)
        self.textarea22.config(state=DISABLED)

        return self.sts_f
 
app = Application(master=mainFrame)

app.mainloop()