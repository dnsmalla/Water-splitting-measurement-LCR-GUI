#!/usr/bin/env python
__author__ = "Dinesh Bahadur Malla"
__copyright__ = "NONE"
__credits__ = ["Sogabe sensei,Sakamoto sensei, Ono sensei"]
__license__ = "NONE"
__version__ = "1.0.1"

# importing library

import visa 
import numpy as np
import time
import logging
import os
import os.path
from time import gmtime, strftime



# to set calculation 1 n calcualtion 2 form different frame work from GUI

Calc_1=[]
Calc_2=[]
def set_cal(c1,c2):
    Calc_1.clear()
    Calc_2.clear()
    Calc_1.append(c1)
    Calc_2.append(c2)


def openVisaResource_1(address,parents):
    ''' 
    openVisaResource(address)
    
    Creates the intsrument handle 

    Arguments:
    
    address:GPIB address :Integer   
    '''
    try:
        rm = visa.ResourceManager()
        inst_handle = rm.open_resource('GPIB0::'+str(address)+'::INSTR')
        parents.update_status("Initialized-1")
        return inst_handle
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " connection error"


def openVisaResource_2(address,parents):
    ''' 
    openVisaResource(address)
    
    Creates the intsrument handle 

    Arguments:
    
    address:GPIB address :Integer   
    '''
    try:
        rm = visa.ResourceManager()
        inst_handle = rm.open_resource('GPIB0::'+str(address)+'::INSTR')
        parents.update_status("Initialized-2")
        return inst_handle
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " connection error"

  
def close_(parents,address_1=2,address_2=14): # GPIB0 for LCR is 2, electrometer is __ and Multimete is 14 
    
    ''' 
    close VisaResource(address)
    
    reset the intsrument handle 

    Arguments:
    
    address_1:GPIB address0 :Integer  
    address_2:GPIB address0 :Integer  
    '''
    inst_handle_1=openVisaResource_1(address_1,parents)
    inst_handle_1.write("*RST")
    inst_handle_1.write("*CLS")
    inst_handle_2=openVisaResource_2(address_2,parents)
    inst_handle_2.write("*RST")
    inst_handle_2.write("*CLS")
    setdefaultParameters_1(inst_handle_1)
    setdefaultParameters_2(inst_handle_2)
    parents.update_status("Initialized")
    print('Initialized')
    return inst_handle_1

   
def initInstrument_1(inst_handle_1,do_reset):
    ''' 
    initInstrument(inst_handle)
    
    Initializes the instrument and returns the instrument name
    
    Arguments:
    
    inst_handle:intsrument handle from 'openVisaResource()' 
    do_reset:True/False
    
    '''
    try:
        name = inst_handle_1.query("*IDN?")
        if do_reset:
            inst_handle_1.write("*RST")   
        inst_handle_1.write("*CLS")
        setdefaultParameters_1(inst_handle_1)
        return name
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " initInstrument error"

def initInstrument_2(inst_handle_2,do_reset):
    ''' 
    initInstrument(inst_handle)
    
    Initializes the instrument and returns the instrument name
    
    Arguments:
    
    inst_handle:intsrument handle from 'openVisaResource()' 
    do_reset:True/False
    
    '''
    try:
        name = inst_handle_2.query("*IDN?")
        if do_reset:
            inst_handle_2.write("*RST")   
        inst_handle_2.write("*CLS")
        setdefaultParameters_2(inst_handle_2)
        return name
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " initInstrument error"
    
def setdefaultParameters_1(inst_handle_1):
    ''' 
    setCorrectionParameters(inst_handle)
                            
    corrections before the measurements 
    
    Arguments:
    
    inst_handle:instrument handle from 'openVisaResource()'
    
    '''
    set_cal("C","D")
    try:
        command= ''':SENS:CORR:OPEN ON
                    ;:SENS:CORR:SHOR ON
                    ;:CAL:CABL {clen}
                    ;:AVER:COUN 100
                    ;:AVER:ON
                    ;:SOUR:FREQ {freq}
                    ;:SOUR:VOLT {isV}
                    ;:CALC1:FORM {calc_1}
                    ;:CALC2:FORM {calc_2}'''.format(
                clen=str(1),
                freq=1000,
                isV=str(0.0001),
                calc_1='C',
                calc_2='D')
        inst_handle_1.write(':SOUR:VOLT:OFFS:STAT 1') # for  DC bias voltate off state 1
        inst_handle_1.write(':SOUR:VOLT:MODE CONT')   # for  voltate mode continuous
        inst_handle_1.write(':TRIG:SOUR EXT')         # for  triger external
        inst_handle_1.write(':FUNC:CONC ON')          # for  set measurement function
                
        result = inst_handle_1.write(command)
        return 1
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " setdefaultParameters error"

def setdefaultParameters_2(inst_handle_2):
    ''' 
    setCorrectionParameters()
                            
    Carries our any corrections before the measurements 
    
    '''
    try:
        # Turn of guard shield.
        inst_handle_2.write('sense:voltage:guard 0')

        #Disable math
        inst_handle_2.write('calculate:state 0')

        #Disable filters and reference
        inst_handle_2.write('sense:voltage:average:state 0')
        inst_handle_2.write('sense:voltage:median:state 0')
        inst_handle_2.write('sense:voltage:reference:state 0')

        #Fix the voltage range
        inst_handle_2.write('sense:voltage:range 2')

        #Enable user input text shown on screen
        inst_handle_2.write('display:text:state 1')

        #Disable zerocheck
        inst_handle_2.write('system:zcheck 0')

        #To achieve higher resolution in the timestamps, I use relative timing
        inst_handle_2.write('system:tstamp:type relative')

        #I'm not awfully concerned with noise from the powerline, so the sync
        # is turned off. This also increases the sample rate drastically.
        inst_handle_2.write('system:lsync:state 0') 

        #Setting absolute timestamps from initiation
        inst_handle_2.write('trace:timestamp:format absolute')


        #immediate triggering
        #enable and set trigger to be immediate - i.e. without delay
        inst_handle_2.write('trigger:source immediate')

        #Quickest measurement averaging time
        inst_handle_2.write('voltage:nplc 0.01')

        #A sufficiently high resolution is selected (6digit)
        inst_handle_2.write('voltage:digits 3')

        #Return to ordinary display
        inst_handle_2.write('display:text:state 0')
        

    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return "setdefaultParameters error"

    


    
def setCorrectionParameters(inst_handle_1,calc_1,calc_2,cable_length):
    ''' 
    setCorrectionParameters(inst_handle,calc_1,calc_2,cable_length)
                            
    Carries our any corrections before the measurements 
    
    Arguments:
    
    inst_handle:instrument handle from 'openVisaResource()'
    cable_length: Length in meters : Positive Integer 
    Calcuation_1-->["Z","C","Cs","CPRP","Cp","Ls","Lp"])
    calculation_2-->["Rs","Rp","PHAS","D"]
    average :  is on with 100 as default
    '''
    set_cal(calc_1,calc_2)
    try:
        
        command= ''':SENS:CORR:OPEN ON
                    ;:SENS:CORR:SHOR ON
                    ;:CAL:CABL {clen}
                    ;:AVER:COUN 100
                    ;:AVER:ON
                ;:CALC1:FORM {calc_1}
                ;:CALC2:FORM {calc_2}'''.format(
                clen=str(cable_length),
                calc_1=calc_1,
                calc_2=calc_2)
                
        inst_handle_1.write(command)
        return 1
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('openVisaResource ERROR')
        return " setCorrectionParameters error"
    
def setSignalLevelAndFrequency(inst_handle_1,frequency,                               
                               ac_signl):
    ''' 
    SetSignalLevelAndFrequency(inst_handle,frequency,                                          
                               is_voltage_signal)
    
    Sets the Signal type(Voltage) and frequency
     
    '''
        
    try:
        command= ''':SOUR:FREQ {freq}
                    ;:SOUR:VOLT {isV}'''.format(
                    freq=frequency,
                    isV=str(ac_signl))
        inst_handle_1.write(command)
        return 1
    
    except:
        logging.getLogger().error("openVisaResource ERROR",exc_info=True)
        print('setSignalLevelAndFrequency ERROR')
        return " setSignalLevelAndFrequency error"


    
def fetchData(inst_handle_1,v_n,delay):
    ''' 
    fetchData(inst_handle):
    
    Fetches the data
    
    Arguments:
    
    inst_handle:instrument handle from 'openVisaResource()'
    
    '''
    
    WAIT_TIME_SEC=1.0
    
    try:
        inst_handle_1.write(':SOUR:VOLT:OFFS ' +str(v_n)) # to set each time dc voltage
        inst_handle_1.write(':INIT')
        #inst_handle_1.write(':TRIG:SOUR EXT') #always trig from the external
        inst_handle_1.write(':TRIG:SOUR INT') #always trig from the internal 
        #inst_handle_1.write(':TRIG')
        #inst_handle.write(':TRIG:DEL '+str(delay))
        time.sleep(delay)# to make sleep to measure data
        values=inst_handle_1.query_ascii_values(':FETC?',separator=',', container=np.array)
        #inst_handle_1.write(':TRIG:SOUR EXT') #always trig from the external
        return values
    except:
        logging.getLogger().error("fetchData ERROR", 
                                   exc_info=True)
        print('fetchData ERROR')
        return -1

def fetch_emv(inst_handle_2):
    ''' 
    fetchData(inst_handle):
    
    Fetches the data
    
    Arguments:
    
    inst_handle:instrument handle from 'openVisaResource()'
    
    '''

    try:
        #clear internal memory
        inst_handle_2.write('*CLS')
        inst_handle_2.write('trace:clear')
        #Select number of points and the feed control
        inst_handle_2.write('trace:points ',str(100))

        #Reading out a list of values.
        value_2=inst_handle_2.query_ascii_values(':READ?',separator=',', container=np.array)
        
        return value_2[0]

    except:
        logging.getLogger().error("fetch_emv ERROR", 
                                   exc_info=True)
        print('fetch_emv ERROR')
        return -1


def runCVLoop(inst_handle_1,inst_handle_2,VBias,filename,parent,time_s):
    ''' 
    fetchData(inst_handle):
    
    Fetches the data
    
    Arguments:
    
    inst_handle:instrument handle from 'openVisaResource()'
    freq:Frequency in HZ at which to measure CV
    VBias:Array with voltage data points at which to measure Capacitance
    Calcuation_1-->["Z","C","Cs","CPRP","Cp","Ls","Lp"])
    calculation_2-->["Rs","Rp","PHAS","D"]
    
    '''
    #if inst_handle==None:
        #inst_handle=openVisaResource("2")
        #setdefaultParameters(inst_handle)
    print("inst2",inst_handle_2)


    calc_1=Calc_1[0] # set calculation 1 for data save
    calc_2=Calc_2[0] # set calculation 2 for data save
    C1_data = [] #list for calculation data 1
    C2_data = [] #list for calculation data 2
    #set data save path to data folder 
    os.makedirs('./Data/', exist_ok=True)
    save_path = './Data/'
    #make file name using date and time at measuring time
    if filename==None:
        filename=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        name=filename+".csv"
    else:
        f=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        name=f+filename+".csv"
    print(filename)
    fullName = os.path.join(save_path,name ) 
    # fullname is file save path csv file 
    f = open(fullName, 'w+')
    #set header for csv file according to calcualtion 1 and calcualtion 2
    if (calc_1 == 'C'):
        xaxis1='Cp(F)' 
        xaxis2='D'
    elif (calc_1 == 'Cs'):
        xaxis1='Cp(F)' 
        xaxis2='Q'
    elif (calc_1 == 'Z'):
        xaxis1='Rs(ohm)' 
        xaxis2='D'
    elif (calc_1 == 'CPRP'):
        xaxis1='Cp(F)' 
        xaxis2='G(s)'
    elif (calc_1 == 'Cp'):
        xaxis1='Cp(F)' 
        xaxis2='Rp(Ohms)'
    elif (calc_1 == 'Ls'):
        xaxis1='Lp(H)' 
        xaxis2='D'
    elif (calc_1 == 'Lp'):
        xaxis1='Lp(H)' 
        xaxis2='D'
    elif (calc_1 == 'C'):
        xaxis1='Cs(F)' 
        xaxis2='Rs(Ohms)'
    #set the column of csv
    f.write('Voltage (V),  Vs Ag/AgCl ,'+xaxis1+', '+xaxis2+'\r')
    f.close() # file close
    parent.update_x_y(xaxis1,xaxis2) # for GUI Data column update 
    parent.clear_data() # clear GUI data 

    try:
        em=[] # empty list for data from multimeter 
        for j,v in enumerate(VBias):
            parent.update_status("Running")
            #Set Bias Voltage - Turn on Bias Voltage - Pause - Read Front Panel
            time.sleep(time_s) # sleep for time sleep set in GUI set 
            v=round(v,2)# round up the voltage value near mili voltage to show in GUI
            data=fetchData(inst_handle_1,v,time_s)#Get Capacitance Reading
            #data=np.random.random(3)# to test the GUI
            emv=fetch_emv(inst_handle_2)
            print("this is data fetched",v,data,emv)
            em.append(emv)# append multimeter data to list
            
            C1 = data[1]
            C2 = data[2] 

            f = open(fullName, 'a')
            f.write(str(v) + ','+ str(emv)+ ',' + str(C1) + ',' + str(C2) + '\r')
            f.close()
           
            C1_data.append(C1)  # append data to list calcualtion1
            C2_data.append(C2)  # append data to list calcualtion2
            
            print('Voltage:'+str(v)+' V')
            parent.update_data(emv,C1,C2,j) # GUI data update
            parent.update_()    # update GUI show
        
        fetchData(inst_handle_1,0,time_s)
        parent.update_status("End") # GUI status update 
        parent.No_update()          # call GUI no update 
        parent.clear_plot()         # call GUI plot clear
        parent.updatePlot(em,C1_data,C2_data,xaxis1,xaxis2) # to update the GUI plot
        
    except:
        parent.update_status("ERROR")
        logging.getLogger().error("runCVLoop ERROR", 
                                   exc_info=True)
        print('runCVLoop ERROR')
        return -1       


   
