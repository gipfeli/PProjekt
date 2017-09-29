# -*- coding: utf-8 -*-
#!/usr/bin/env python

#......................
#version OK

import gtk
import gtk.glade

import inspect, time
from ctypes import *

#...........................................................................
#OK
class IOsim():
    def __init__(self):      
        self.gladeXml = gtk.glade.XML("iosim_03a.glade")
        self.gladeXml.signal_autoconnect(self)
        self.window = self.gladeXml.get_widget("mainwindow")
        #self.window.set_title("IOsim")
        #self.window.show_all()
        
#...........................................................................
#OK
    #button close / function program stop
    def btnClose(self):                 #beenden befehl zum ausfuehren
        gtk.main_quit()
             
    def on_btnExit_clicked(self,*args): #funktion beenden gedrueckt
        self.btnClose()  
        
    def on_imagemenuitem1_activate(self,btn):   #funktion bestaetigt, noch keine beenden befehl
        self.btnClose()

#...........................................................................
#OK
iosim = cdll.LoadLibrary(r"C:\Program Files\HEIDENHAIN\TNCvbBase\control\JHIOsim.dll")  #iosim = "self" ??

#...........................................................................
#OK
SIM = (
	('O10','I10'),
	('O11','I11'),
	('O12','I12'),
	('O13','I13'),
	('O14','I14'),
	('O15','I15'),
)

#...........................................................................
#OK
SIM_ID = 111

#...........................................................................
CYCLE_TIME = 0.005
#CYCLE_TIME = 1.0

#...........................................................................
#Konstanten (intern)
JHIO_SUCCESS = 0

JHIO_TYPE_INPUT 		= 1  #(Logic) 
JHIO_TYPE_OUTPUT 		= 2  #(Logic) 
JHIO_TYPE_INPUTBYTE 	= 3  #(Byte) 
JHIO_TYPE_INPUTWORD  	= 4  #(Short) 
JHIO_TYPE_INPUTDWORD 	= 5  #(Long) 
JHIO_TYPE_INPUTFLOAT 	= 6  #(Float) 
JHIO_TYPE_OUTPUTBYTE 	= 7  #(Byte) 
JHIO_TYPE_OUTPUTWORD 	= 8  #(Short) 
JHIO_TYPE_OUTPUTDWORD 	= 9  #(Long) 
JHIO_TYPE_OUTPUTFLOAT 	= 10 #(Float)

#...........................................................................
#import fuktion 
def GetAddressByClamp(hardware,connector,clamp):
	AddressOffset = c_ulong(0)
	pAddressOffset = pointer(AddressOffset)
	Type = c_int(0)
	pType = pointer(Type)
	ret = iosim.JHIOGetAddressByClamp(c_int(hardware),c_int(connector),c_int(clamp),pAddressOffset,pType)
	return int(ret),AddressOffset.value,Type.value
	
def GetAddressByName(symbolName):
	AddressOffset = c_ulong(0)
	pAddressOffset = pointer(AddressOffset)
	Type = c_int(0)
	pType = pointer(Type)
	ret = iosim.JHIOGetAddressByName(symbolName,pAddressOffset,pType)  #JHIOGetAddressByName
                                                                        #Ermittelt die Shared Memory Adresse aus dem symbolischen PLC Bezeichner oder der logischen Adresse.
                                                                        
	return int(ret),AddressOffset.value,Type.value
	
def GetLogicValue(AddressOffset):
	fValue = c_bool()
	pfValue = pointer(fValue)
	ret = iosim.JHIOGetLogicValue(AddressOffset,pfValue)
	return int(ret),fValue.value

#...........................................................................	
#import fuktion 
def CallOk(ret):
	if type(ret) in (tuple,list):
		ret = ret[0]
	if ret != JHIO_SUCCESS:    #JHIO_SUCCESS = 0, erfolgreich
		lineNr = inspect.getouterframes(inspect.currentframe(),0)[1][2]
		print 'Error %s in line %s'%(ret,lineNr)
		return False
	else: return True                                                      #erfolgreich return


#...........................................................................    
print 'Setze Simulation-ID auf %s'%SIM_ID
if CallOk(iosim.JHIOSetSimulationId(SIM_ID)):       #ID für die PLC setzen, bzw. I/O Simulation aktivieren
                                                    #PLC Modul 9035 mit Parameter 110 abgefragt
                                                    #nicht explizit gesetzt = PLC Doppelwort D296 den Wert 0
                                                    #neue nc vers., I/O Simulation nur aktiv, wenn die Simulations-ID auf einen Wert <> 0 gesetzt wird.
	print 'Simulation-ID erfolgreich gesetzt' 

#...........................................................................
#HSCI Notaus-Eingänge (kette) ES.A und ES.B setzen
	CallOk(iosim.JHIOLockMemory(1000))             #Shared Memory für mehrere aufeinanderfolgende Speicherzugriffe reservieren
                                                    #1s, Timeoutzeit in Millisekunden für den Versuch den Speicher zu reservieren

	print 'Schliesse Not-Aus Kette' 
	CallOk(iosim.JHIOSetHSCILogicValue(1,0,1))     #AddressOffset?    #JHIOLockMemory den Speicherzugriff reserviert 
                                                    #int iSignalType: 1:JHIO_HSCI_ES_A, 2:..ES_B
                                                    #long AddressOffset: 0?
                                                    #BOOL fValue: 1,2                                                    
	CallOk(iosim.JHIOSetHSCILogicValue(1,0,2)) #AddressOffset?    
	print 'Not-Aus Kette geschlossen' 

	CallOk(iosim.JHIOUnlockMemory())               #Beenden der Reservierung des Shared Memory für mehrere aufeinanderfolgende Speicherzugriffe

#...........................................................................
#Memory Offsets lesen
	print 'Lese Memory Offsets'
	sim_offset = []                                #leer, null setzen??
	for src,des in SIM:                            #SIM = ('O10','I10'), ..
		sim_offset.append([GetAddressByName(src)[1:3],GetAddressByName(des)[1:3]])
	print 'Memory Offsets gelesen'
	
#...........................................................................
	print 'Starte Simulation'                      #Simulations-ID Wert <> 0 
	try:
		while True:
			CallOk(iosim.JHIOLockMemory(3000))   #3s, Timeoutzeit in Millisekunden für den Versuch den Speicher zu reservieren
			for src,des in sim_offset:
				srcValue = None
				if src[1] in (JHIO_TYPE_INPUT,JHIO_TYPE_OUTPUT):    # =1, =2
					srcValue = GetLogicValue(src[0])[1]
				else:
					print 'Nicht implementiert!'
                    
				if srcValue != None:
					if des[1] in (JHIO_TYPE_INPUT,JHIO_TYPE_OUTPUT):
						CallOk(iosim.JHIOSetLogicValue(des[0],srcValue))  #Schreiben eines Logik-Wertes: JHIO_TYPE_INPUT = 1
					else:
						print 'Nicht implementiert!'
			
			CallOk(iosim.JHIOUnlockMemory())
			time.sleep(CYCLE_TIME)
	except KeyboardInterrupt:
		print('Simulation durch Anwender abgebrochen!')
	
	iosim.JHIOSetSimulationId(0)                                           #ID für die PLC setzen, bzw. I/O Simulation aktivieren

#...........................................................................
if __name__ == "__main__":
    IOsim = IOsim()
    gtk.main()
