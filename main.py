import kivy
import pip
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import cv2
import utils as u
import time
kivy.require('1.9.0')

img_path = ""
class MyRoot(BoxLayout):
    def __init__(self):

        super(MyRoot, self).__init__()
        self.label.text = "ImgCrypt"
        self.image.size = (0, 0)
        u.hide_widget(self.back_button, True)
        u.hide_widget(self.file_chooser,True)
        u.hide_widget(self.process_button,True)
        u.hide_widget(self.process_button_dec,True)
        u.hide_widget(self.text_box, True)
    def back(self): #resets everything to home screen
        self.label.text = "ImgCrypt"
        u.hide_widget(self.back_button,True)
        u.hide_widget(self.file_chooser, True)
        u.hide_widget(self.process_button, True)
        u.hide_widget(self.process_button_dec, True)
        u.hide_widget(self.text_box, True)
        u.hide_widget(self.encode_button,False)
        u.hide_widget(self.decode_button, False)
        u.hide_widget(self.image, True)
    def open_encode(self):
        self.label.text = "Select Image and Type Message"
        u.hide_widget(self.back_button, False)
        u.hide_widget(self.file_chooser, False)
        u.hide_widget(self.encode_button,True)
        u.hide_widget(self.decode_button,True)
        u.hide_widget(self.process_button,False)
        u.hide_widget(self.text_box, False)
        self.text_box.text = "input text"
        self.text_box.pos_hint = ({"x":.1})
        self.process_button.pos_hint = ({"x":.1,"y":0})
        #img_path = self.file_chooser.selection[0]
        try:
            img = cv2.imread(img_path)
            #self.image.source = img_path
            #self.image.size_hint = (.8,.8)
            #self.image.pos_hint = ({'x':.1})
            #self.file_chooser.size_hint = (0,0)
            #self.file_chooser.pos_hint = ({'x':-10, 'y':-10})
        except:
            print("Please select an image")
    def process_encode(self):
        self.label.text = "Message has been encoded"
        img_path = self.file_chooser.selection[0]
        img = cv2.imread(img_path)
        msg = u.ArrToBin(u.TextToNum(self.text_box.text))

        cv2.imwrite(("outputs/output"+str(time.strftime("%x")).replace("/",",")+str(time.strftime("%X")).replace(":",",")+".png"),u.encode(img,msg))
        try:
            img = cv2.imread(img_path)
            self.image.source = img_path
            self.image.size_hint = (.8,.8)
            self.image.pos_hint = ({'x':.1})
            u.hide_widget(self.file_chooser,True)
        except:
            print("Please select an image")
        return 1
    def open_decode(self):
        self.label.text = "Select Image"
        u.hide_widget(self.back_button, False)
        u.hide_widget(self.file_chooser, False)
        u.hide_widget(self.encode_button, True)
        u.hide_widget(self.decode_button, True)
        u.hide_widget(self.process_button_dec, False)
    def process_decode(self):

        img_path = self.file_chooser.selection[0]
        img = cv2.imread(img_path)
        u.hide_widget(self.text_box, False)
        self.text_box.text = u.NumToText(u.BinToArr(u.decode(img,30)))
        #print(u.NumToText(u.BinToArr(u.decode(img,30))))
        self.label.text = "Message has been decoded"
        return 1

class ImgCrypt_home(App):
    def build(self):

        textinput = TextInput(text='Hello world')

        return MyRoot()


imgcrypt_home = ImgCrypt_home()
imgcrypt_home.run()



