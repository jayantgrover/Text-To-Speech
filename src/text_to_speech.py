import os 
import sys
import pyttsx3

engine = pyttsx3.init()
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox,QFileDialog
class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/text_to_speech.ui', self)
        self.cncl_btn.clicked.connect(self.cncl)
        self.speech_btn.clicked.connect(self.speak)
        self.download_btn.clicked.connect(self.download)
        self.male.clicked.connect(self.gender_chkbox)
        self.female.clicked.connect(self.gender_chkbox)
        self.slow_spd.clicked.connect(self.speed_chkbox)
        self.normal_spd.clicked.connect(self.speed_chkbox)
        self.fast_spd.clicked.connect(self.speed_chkbox)

        self.show()
    def show_message_box(self,message,title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()

    def genderchk(self):
        if self.male.isChecked():
            return "Male" 
        if self.female.isChecked():
            return "female"

    def speedchk(self):
        if self.slow_spd.isChecked():
            return "Slow"
        if self.normal_spd.isChecked():
            return "Normal"
        if self.fast_spd.isChecked():
            return "Fast"
        
    def speak(self):
        text = self.textbox.text()
        if text :
            gender = self.genderchk()
            if gender:
                speed = self.speedchk()
                if speed :
                    voices = engine.getProperty('voices')
                    def setvoice():
                        if( gender=='Male'):
                            engine.setProperty('voice',voices[0].id)
                            engine.say(text)
                            engine.runAndWait()
                        else:
                            engine.setProperty('voice',voices[1].id)
                            engine.say(text)
                            engine.runAndWait()
                            engine.stop()
                    if(text):
                        if(speed =='Fast'):
                            engine.setProperty('rate',250)
                            setvoice()
                        elif(speed =='Normal'):
                            engine.setProperty('rate',150)
                            setvoice()
                        else:
                            engine.setProperty('rate',50)
                            setvoice()
                else:
                    self.show_message_box("Select Speed ","Valid_Input ")
            else:
                self.show_message_box("Select Gender ","Valid_Input ")
        else:
            self.show_message_box("Write Text","Valid_Input ")
    def download(self):
        print("download")
        # path = r"F:\Project Work\Python Text To Speech\Downloads"
        text = self.textbox.text()
        if text != "":
            gender = self.genderchk()
            speed = self.speedchk()
            if gender != "" :
                if speed != "" :
                    voices = engine.getProperty('voices')
                    def setvoice():
                        if(gender=='Male'):
                            engine.setProperty('voice',voices[0].id)
                            # engine.say(text)
                            path= QFileDialog.getExistingDirectory(self,"Open a folder")
                            os.chdir(path)
                            engine.save_to_file(text,'Text.mp3')
                            engine.runAndWait()
                        else:
                            engine.setProperty('voice',voices[1].id)
                            # engine.say(text)
                            # path=filedialog.askdirectory()
                            path= QFileDialog.getExistingDirectory(self,"Open a folder")
                            os.chdir(path)
                            engine.save_to_file(text,'Text.mp3')
                            engine.runAndWait()
                            engine.stop()
                    if(text):
                        if(speed =='Fast'):
                            engine.setProperty('rate',250)
                            setvoice()
                        elif(speed =='Normal'):
                            engine.setProperty('rate',150)
                            setvoice()
                        else:
                            engine.setProperty('rate',50)
                            setvoice()
                else:
                    self.show_message_box("Select Speed ","Valid_Input ")
            else:
                self.show_message_box("Select Gender ","Valid_Input ")
        else:
            self.show_message_box("Write Text","Valid_Input ")  
        self.show_message_box(f"Download Sucessfull  ","Success") 
        self.close()
        
        
    def gender_chkbox(self):
        sender = self.sender()
        if sender == self.male:
            self.female.setChecked(False)
        elif sender == self.female:
            self.male.setChecked(False)
            
    def speed_chkbox(self):
        sender = self.sender()
        if sender == self.slow_spd:
            self.normal_spd.setChecked(False)
            self.fast_spd.setChecked(False)
        elif sender == self.normal_spd:
            self.slow_spd.setChecked(False)
            self.fast_spd.setChecked(False)
        elif sender == self.fast_spd:
            self.slow_spd.setChecked(False)
            self.normal_spd.setChecked(False)



    def cncl(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()