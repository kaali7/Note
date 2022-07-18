#import 
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

#window size
Window.size = (630,450)

#connected to desgin file
KV =  Builder.load_file("desgin.kv")

class Note(MDApp):
    def build(self):
        return KV

App = Note()
App.run()
