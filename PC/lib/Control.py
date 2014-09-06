import time
import serial
import Tkinter
from PIL import Image, ImageTk 
import ImageAnalysis
###########################################################################################################
###########################################################################################################
###  ____            _                  _   ____        __ _             ##################################
### |  _ \ _ __ ___ | |_ ___   ___ ___ | | |  _ \  ___ / _(_)_ __   ___  ##################################
### | |_) | '__/ _ \| __/ _ \ / __/ _ \| | | | | |/ _ \ |_| | '_ \ / _ \ ##################################
### |  __/| | | (_) | || (_) | (_| (_) | | | |_| |  __/  _| | | | |  __/ ##################################
### |_|   |_|  \___/ \__\___/ \___\___/|_| |____/ \___|_| |_|_| |_|\___| ##################################
###########################################################################################################
###########################################################################################################
class Protocol:
    Picture = 'P'
    Hand_Left_Open = '1'
    Hand_Left_Close = '2'
    Hand_Left_Vertical = '3'
    Hand_Left_Aclinic = '4'
    Hand_Right_Open = 'A'
    Hand_Right_Close = 'B'
    Hand_Right_Vertical = 'C'
    Hand_Right_Aclinic = 'D'
########################################################################################################
########################################################################################################    
###     _    ____ ___          __    ____                                ###############################
###    / \  |  _ \_ _|   ___  / _|  / ___|__ _ _ __ ___   ___ _ __ __ _  ###############################
###   / _ \ | |_) | |   / _ \| |_  | |   / _` | '_ ` _ \ / _ \ '__/ _` | ###############################
###  / ___ \|  __/| |  | (_) |  _| | |__| (_| | | | | | |  __/ | | (_| | ###############################
### /_/   \_\_|  |___|  \___/|_|    \____\__,_|_| |_| |_|\___|_|  \__,_| ###############################
########################################################################################################
########################################################################################################     
class Camera:
    def __init__(self, serialName = '/dev/cu.usbmodem1411'):
        self.serial = serial.Serial(serialName, 38400, timeout = 5)
        #time.sleep(5)
        self.canvas = None
    def __view(self, jpgFileName):
        if not ( self.canvas is None ):
            self.canvas.delete(Tkinter.ALL)
            jpg = Image.open(jpgFileName)  
            #ImageAnalysis.trans(jpg)
            (width, height) = jpg.size
            for x in range(width):
                for y in range(height):
                    (r, g, b) = jpg.getpixel((x,y))
                    self.canvas.create_line(x, y, x+1, y+1, fill = "#%02x%02x%02x"%(r, g, b))
    def takePicture(self, jpgFileName):
        self.serial.flushInput()
        self.serial.write(Protocol.Picture)
        data = ''
        while True:
            ch = self.serial.read()
            print 'ch = ', ch
            if len(ch) == 0 :
                break
            data += ch
        print data
        # cache = ['','','','']
        # while cache != ['F', 'F', 'D', '9']:
        #     for i in range(3):
        #         cache[i] = cache[i+1]
        #     cache[3] = self.serial.read()
        #     data += cache[3]
        def f(a):
            return ( ord(a) - ord('0') ) if ( a >= '0' and a <= '9' ) else ( ord(a) - ord('A') + 10 )
        jpg = open(jpgFileName, 'wb')
        for i in range(0,len(data),2):
            v = f(data[i]) * 16 + f(data[i+1])
            jpg.write(chr(v))
        jpg.close()
        print 'takePicture','size = ',len(data), 'jpgFileName = ', jpgFileName
        self.__view(jpgFileName)
    def bindViewFrame(self, frame):
        self.canvas = Tkinter.Canvas(frame, bg="black", height=240, width=320)
        self.canvas.grid(row = 0, column = 0)
        def takePicture():
            self.takePicture('./tmp/'+time.strftime('%Y-%m-%d-%H-%M-%S')+'.jpg')
        Tkinter.Button(frame, text = 'takePicture', command = takePicture, bd = 0).grid(row = 1, column = 0)
    
########################################################################################################
########################################################################################################    
###     _    ____ ___          __   _   _                 _  ###########################################
###    / \  |  _ \_ _|   ___  / _| | | | | __ _ _ __   __| | ###########################################
###   / _ \ | |_) | |   / _ \| |_  | |_| |/ _` | '_ \ / _` | ###########################################
###  / ___ \|  __/| |  | (_) |  _| |  _  | (_| | | | | (_| | ###########################################
### /_/   \_\_|  |___|  \___/|_|   |_| |_|\__,_|_| |_|\__,_| ###########################################
########################################################################################################
########################################################################################################   
class Hand:        
    def __init__(self, serialName = '/dev/cu.usbmodem1421'):
        self.serial = serial.Serial(serialName, 38400)
    def leftOpen(self):
        self.serial.write(Protocol.Hand_Left_Open)
    def leftClose(self):
        self.serial.write(Protocol.Hand_Left_Close)
    def leftVertical(self):
        self.serial.write(Protocol.Hand_Left_Vertical)
    def leftAclinic(self):
        self.serial.write(Protocol.Hand_Left_Aclinic)
    def rightOpen(self):
        self.serial.write(Protocol.Hand_Right_Open)
    def rightClose(self):
        self.serial.write(Protocol.Hand_Right_Close)
    def rightVertical(self):
        self.serial.write(Protocol.Hand_Right_Vertical)
    def rightAclinic(self):
        self.serial.write(Protocol.Hand_Right_Aclinic)
    def events(self, events):
        for event in events:
            event()
            time.sleep(1)   
    def F(self, times = 1):
        times = (times%4+4) % 4
        if times in [1, 2]:
            self.events((self.leftOpen, self.leftVertical, self.leftClose, self.leftAclinic))
        elif times == 3:
            self.events((self.leftVertical, self.leftOpen, self.leftAclinic, self.leftClose))
    def R(self, times = 1):
        times = (times%4+4) % 4
        if times in [1, 2]:
            for i in range(times) :
                self.events((self.rightVertical, self.rightOpen, self.rightAclinic, self.rightClose))
        elif times == 3:
            self.events((self.rightOpen, self.rightVertical, self.rightClose, self.rightAclinic))
    def x(self, times = 1):
        times = (times%4+4) % 4
        if times in [1, 2]:
            for i in range(times):
                self.events((self.leftOpen, self.rightVertical, self.leftClose, self.rightOpen, self.rightAclinic, self.rightClose))
        elif times == 3:
            self.events((self.rightOpen, self.rightVertical, self.rightClose, self.leftOpen, self.rightAclinic, self.leftClose))
    def z(self, times = 1):
        times = (times%4+4) % 4
        if times in [1, 2]:
            for i in range(times):
                self.events((self.leftOpen, self.leftVertical, self.leftClose, self.rightOpen, self.leftAclinic, self.rightClose))
        elif times == 3:
            self.events((self.rightOpen, self.leftVertical, self.rightClose, self.leftOpen, self.leftAclinic, self.leftClose))
    def y(self, times = 1):
        times = (times%4+4) % 4
        if times in [1, 2]:
            for i in range(times):
                self.x()
                self.z(-1)
                self.x(-1)
        elif times == 3:
            self.x()
            self.z()
            self.x(-1)
    def U(self, times = 1):
        self.x(-1)
        self.F(times)
        self.x()
    def D(self, times = 1):
        self.x()
        self.F(times)
        self.x(-1)
    def L(self, times = 1):
        self.z(2)
        self.R(times)
        self.z(2)
    def B(self, times = 1):
        self.x(2)
        self.F(times)
        self.x(2)
    def bindOperationFrame(self, frame):
        Tkinter.Button(frame, text = 'left open', command = self.leftOpen).grid(row = 0, column = 0)
        Tkinter.Button(frame, text = 'left close', command = self.leftClose).grid(row = 0, column = 1)
        Tkinter.Button(frame, text = 'left vertical', command = self.leftVertical).grid(row = 0, column = 2)
        Tkinter.Button(frame, text = 'left aclinic', command = self.leftAclinic).grid(row = 0, column = 3)
        Tkinter.Button(frame, text = 'right open', command = self.rightOpen).grid(row = 1, column = 0);
        Tkinter.Button(frame, text = 'right close', command = self.rightClose).grid(row = 1, column = 1);
        Tkinter.Button(frame, text = 'right vertical', command = self.rightVertical).grid(row = 1, column = 2)
        Tkinter.Button(frame, text = 'right aclinic', command = self.rightAclinic).grid(row = 1, column = 3)
        
        