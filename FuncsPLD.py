import serial
import time
import picamera
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
import os
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from fpdf import FPDF 

from threading import Thread
class servoUnlock(Thread):
    def run(self):
        '''Start your thread here'''
        ser1 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=4)                 
        time.sleep(2)
        ser1.write(b"Servou\n")
        pass
def servo_unlock():
    thread = servoUnlock()
    thread.daemon = True
    thread.start()

ser = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)
class initialWeightCheck(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.initial_weight = -1
    def run(self):
        #ser = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        #time.sleep(1.5)
        ser.write(b"Weight\n")
        ser.reset_input_buffer()
        ser.flush()
        while True:
            line2 = ser.readline().decode('utf-8').rstrip()
            #print(line2)
            if line2 != "":
                print(float(line2))
                if float(line2) < 0.02:
                    self.initial_weight = 0
                else:
                    self.initial_weight = 1
                break
thread = 1
def initiate_weight_check():
    global thread
    thread = initialWeightCheck()
    thread.daemon = True
    thread.start()
def return_initial_weight():
    return thread.initial_weight

class hallSensorCheck(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.door_shut = -1
    def run(self):
        #ser = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        #time.sleep(1.5)
        ser.write(b"Hall\n")
        #time.sleep(0.5)
        ser.reset_input_buffer()
        ser.flush()
        #time.sleep(0.2)
        while True:
            line3 = ser.readline().decode('utf-8').rstrip()
            if line3 != "":
                print(float(line3))
                if float(line3) <= 300.0:
                    self.door_shut = 1
                else:
                    self.door_shut = 0
                break
thread0 = 2
def initiate_hall_sensor():
    global thread0
    thread0 = hallSensorCheck()
    thread0.daemon = True
    thread0.start()
def return_door_shut():
    return thread0.door_shut

class parcelCheck(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.parcel_spec = -1
    def run(self):
        ser4 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        time.sleep(1.5)
        ser4.write(b"Distance1\n")
        time.sleep(0.5)
        ser4.reset_input_buffer()
        ser4.flush()
        time.sleep(0.2)
        while True:
            line4 = ser4.readline().decode('utf-8').rstrip()
            if line4 != "":
                OD1 = float(line4)
                #print(OD1)
                break
        if OD1 > 157:
            verifier1 = False
        else:
            verifier1 = True
        
        ser5 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        time.sleep(1.5)
        ser5.write(b"Distance2\n")
        time.sleep(0.5)
        ser5.reset_input_buffer()
        ser5.flush()
        time.sleep(0.2)
        line5 = ser5.readline().decode('utf-8').rstrip()
        OD2 = float(line5)
        if OD2 > 250:
            verifier2 = False
        else:
            verifier2 = True
        
        ser6 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        time.sleep(1.5)
        ser6.write(b"Distance3\n")
        time.sleep(0.5)
        ser6.reset_input_buffer()
        ser6.flush()
        time.sleep(0.2)
        line6 = ser6.readline().decode('utf-8').rstrip()
        OD3 = float(line6)
        if OD3 > 350:
            verifier3 = False
        else:
            verifier3 = True
        
        ser7 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3)                 
        time.sleep(1.5)
        ser7.write(b"Weight\n")
        time.sleep(0.5)
        ser7.reset_input_buffer()
        ser7.flush()
        time.sleep(0.2)
        line7 = ser7.readline().decode('utf-8').rstrip()
        if float(line7) > 2:
            verifier4 = False
        else:
            verifier4 = True
        
        if verifier1 is True and verifier2 is True and verifier3 is True and verifier4 is True:
            self.parcel_spec = 1
        else:
            self.parcel_spec = 0
thread1 = 3
def initiate_parcel_check():
    global thread1
    thread1 = parcelCheck()
    thread1.daemon = True
    thread1.start()
def return_parcel_spec():
    return thread1.parcel_spec

class cam(Thread):
    def run(self):
        with picamera.PiCamera() as camera:
            camera.capture("Enclosure.jpg")
def camera():
    thread = cam()
    thread.daemon = True
    thread.start()

class servoLock(Thread):
    def run(self):
        ser8 = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=4)                 
        time.sleep(2)
        ser8.write(b"Servol\n")
def servo_lock():
    thread = servoLock()
    thread.daemon = True
    thread.start()

payment_in_use = False
class paymentCheck(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.payment_presented = False
    def run(self):
        reader = SimpleMFRC522()
        proceed = reader.read()
        global payment_in_use
        payment_in_use = False
        if(proceed):
            self.payment_presented = True
thread2 = 4
def initiate_payment_check():
    global payment_in_use
    payment_in_use = True
    global thread2
    thread2 = paymentCheck()
    thread2.daemon = True
    thread2.start()
def return_payment_presented():
    return thread2.payment_presented
def return_payment_in_use():
    return payment_in_use

def label_creation(name,line,code,town,Class):
    f = open("LabelFile.txt","w+")
    f.write(name)
    f.write("\n")
    f.write(line)
    f.write("\n")
    f.write(code)
    f.write("\n")
    f.write(town)
    f.close()
    qr=qrcode.make('THIS IS TEST QR CODE')
    qr.save('qr1.png')
    with open('somefile2.png','wb') as f:
        EAN13('100000011111',writer=ImageWriter()).write(f)
    class PDF(FPDF):
        def header(self):
            self.image('rmglogo.png', 65,9,30)
            self.set_font('Arial','B',6)
            self.cell(0,30,'',border=1)
            self.set_x(73)
            self.cell(10,8,'Delivered by')
            self.set_y(32)
            self.cell(80,8,'Postage paid GB',align='R')
            self.set_y(12)
            self.set_x(15)
            self.set_font('Arial','B',20)
            self.cell(40,20,Class,border=0,align='C')   
            self.ln(2)
        def footer(self):
            self.set_y(-30)
            self.set_font('Arial','B',11)
            self.cell(0,27,'',border=1)
            self.set_y(-28)
            self.cell(30,6,'Customer Reference:',ln=1)
            self.cell(30,6,'0000012645362221',ln=1)
            self.cell(30,6,'Depertment Reference:',ln=1)
            self.cell(30,6,'10002311',ln=1)
        def chapter_body(self,LabelFile):
            with open(LabelFile, 'rb') as fh:
                txt = fh.read().decode('latin-1')
                self.set_y(-67)
                self.set_font('times','',16)
                self.multi_cell(0,7,txt,border=1)
                self.ln()
    pdf = PDF('P','mm',(104,159))
    pdf.add_page()
    pdf.chapter_body('LabelFile.txt')
    pdf.set_font('times','B',16)
    pdf.set_y(40)
    pdf.cell(0,45,'',border=1)
    pdf.image('qr1.png',12,42,35)
    pdf.image('somefile2.png',48,51,45)
    pdf.output('test3.pdf')
    os.system("lp test3.pdf")

class reStart(Thread):
    def run(self):
        '''Start your thread here'''
        os.system("python3 HomePage1.py")
        pass
def restart():
    thread = reStart()
    thread.daemon = True
    thread.start()