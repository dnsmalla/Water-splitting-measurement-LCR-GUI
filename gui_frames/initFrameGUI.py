from tkinter import *
from tkinter import ttk
from utils import initInstrument_1,initInstrument_2,openVisaResource_1,openVisaResource_2
		
class InitFrame(ttk.Frame):

    def __init__(self, master,inst_handle_1,inst_handle_2,app):
        ttk.Frame.__init__(self, master)# super class initialization
        self.relief = GROOVE# tkinter relief attribute.
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.Widgets()
        self.inst_handle_1=inst_handle_1# initalize the instant handle 1 for LCR
        self.inst_handle_2=inst_handle_2# initalize the instant handle 2 for multi-meter
        self.parent=app
		
    def Widgets(self):
        """ 
        main window of the GUI 
        containt:- 
        - gpib_add1 
        - gpib_add2
        - reset
        - Button

        """
        self.gpib_add1=StringVar(self)
        self.gpib_add2=StringVar(self)
        self.reset=IntVar(self)
        self.gpib1=IntVar(self)
        self.gpib2=IntVar(self)
        self.insts_name=StringVar(self)
        self.gpib_add1.set(str(2)) # set LCR meter GPIB--2
        self.gpib_add2.set(str(16))# set Multi meter GPIB--14
        #self.gpib_add2.set(str(8))# set Multi meter GPIB--8
        self.reset.set(1)
        self.gpib1.set(1) # for selecting gpib 1
        self.gpib2.set(1) # for selecting gpib 2

        main_frame= ttk.Frame(self, borderwidth=2, relief=GROOVE, padding=5)
        main_frame.grid()
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

		#instrument 1
        self.add1_name=ttk.Label(main_frame,text='GPIB Ads-1:',padding=0)
        self.add1_name.grid(row=0, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        self.add1_number=Entry(main_frame, textvariable=self.gpib_add1, bg='white')
        self.add1_number.grid(row=0, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        #instrument 2
        self.add2_name=ttk.Label(main_frame,text='GPIB Ads-2:',padding=0)
        self.add2_name.grid(row=1, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
  
        self.add2_number=Entry(main_frame, textvariable=self.gpib_add2, bg='white')
        self.add2_number.grid(row=1, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        #reset 
        self.reset_option = ttk.Checkbutton(main_frame, text="Reset?",variable=self.reset)
        self.reset_option.grid(row=2, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
        #reset gpig-1
        self.gp1_option = ttk.Checkbutton(main_frame, text="GPIB-1?",variable=self.gpib1)
        self.gp1_option.grid(row=2, column=1, sticky=W )
        
        #reset gpig-2
        self.gp2_option = ttk.Checkbutton(main_frame, text="GPIB-2?",variable=self.gpib2)
        self.gp2_option.grid(row=2, column=1,sticky= E )
		
        self.insts_nameL=ttk.Label(main_frame,text='Instruments:')
        self.insts_nameL.grid(row=3, column=0, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
					   
        self.insts_nameV=ttk.Label(main_frame,text=self.insts_name.get()[0:10],borderwidth=1,relief=SUNKEN,
                                  font=("Helvetica", 8))
        self.insts_nameV.grid(row=3, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
					   
        self.init_Button=ttk.Button(main_frame,text='Initialize',command=self.init_instrument)
        self.init_Button.grid(row=4, column=1, rowspan=1, columnspan=1,
                       sticky=W + E + N + S)
		
    def get_handle(self):
        """ 
        to update instrument handle 
        -inst_handle_1-- LCR
        -inst_handle_2-- multimeter
        
        """
        return self.inst_handle_1,self.inst_handle_2
		
    def init_instrument(self):
        """ 
        to initialize instrument
        using reset button 
        
        """
        self.parent.update_()
        print ("Initializing Instrument.................")
        
        if self.gpib2.get() and self.gpib1.get(): # if gpib 1 and 2 are selected
            self.inst_handle_1=(openVisaResource_1(self.gpib_add1.get(),self.parent))
            n_1=initInstrument_1(self.inst_handle_1,self.reset.get())[16:22]
            self.inst_handle_2=(openVisaResource_2(self.gpib_add2.get(),self.parent))
            n_2=initInstrument_2(self.inst_handle_2,self.reset.get())[32:36]
            self.insts_name.set(' '+n_1+' , KE- '+n_2)
            self.insts_nameV.config(text=self.insts_name.get().replace(',','\n'))


        elif self.gpib1.get(): # if gpib 1 only selected
            self.inst_handle_1=(openVisaResource_1(self.gpib_add1.get(),self.parent))
            self.insts_name.set(initInstrument_1(self.inst_handle_1,self.reset.get())[16:22])
            self.insts_nameV.config(text=self.insts_name.get().replace(',','\n'))

        elif self.gpib2.get(): # if gpib 2 only selected
            self.inst_handle_2=(openVisaResource_2(self.gpib_add2.get(),self.parent))
            n_2=initInstrument_2(self.inst_handle_1,self.reset.get())[32:36]
            self.insts_name.set(' KE- '+n_2)
            self.insts_nameV.config(text=self.insts_name.get().replace(',','\n'))

        else:# nothing is selected
            self.insts_name.set('')
            self.insts_nameV.config(text=self.insts_name.get().replace(',','\n'))
        self.parent.updateInstHandle(self.inst_handle_1,self.inst_handle_2)
        print ("Done")
     
		
		
