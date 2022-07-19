#import 
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.button import Button
from kivy.graphics import Color , RoundedRectangle

#window size
Window.size = (630,450)

#connected to desgin file
Builder.load_file("desgin.kv")

#hover button
class But(Button, HoverBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_color = (0,0,0,0)
        self.size_hint = None,None
        self.size = (80,32)
        self.pos_hint = {'center_y': 0.5}

    
    def on_enter(self):
       
        with self.canvas.before:
            Color(0,0,0,0.8)
            RoundedRectangle(size=(80,32), pos= self.pos, radius=(15,15))
    
    def on_leave(self):

        self.canvas.before.clear()
    

#Screen
class Main(Screen):
    pass

#main app
class Note(MDApp):
    def build(self):

        # color theme of app
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        
        self.sm = ScreenManager(transition = NoTransition())
        self.sm.add_widget(Main(name="main"))

        return self.sm

#run app
App = Note()
App.run()
