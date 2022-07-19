#import 
# from kivymd.app import MDApp
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

#window size
Window.size = (630,450)

#connected to desgin file
Builder.load_file("desgin.kv")

#Screen
class Main(Screen):
    pass

#main app
class Note(App):
    def build(self):
        
        self.sm = ScreenManager(transition = NoTransition())
        self.sm.add_widget(Main(name="main"))

        return self.sm

#run app
App = Note()
App.run()
