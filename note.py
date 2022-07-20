#import 
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.button import Button
from kivy.graphics import Color , RoundedRectangle
from kivymd.uix.menu import MDDropdownMenu

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
            Color(0,0,0,0.6)
            RoundedRectangle(size=(80,32), pos= self.pos, radius=(15,15))
    
    def on_leave(self):

        self.canvas.before.clear()
    
#save button
class Save_but(Button, HoverBehavior):
    pass


#Screen
class Main(Screen):

    def file_menu(self, btn):

        menu_items = [
            {
                'text':'[b]new file[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='file':print("new file")
            },
            {
                'text':'[b]save[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='save':print("save")
            },
            {
                'text':'[b]save as[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='save as':print("save as")
            },
            {
                'text':'exit',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='exit':print("exit")
            }
        ]

        self.menu_file = MDDropdownMenu(
            caller = btn,
            items = menu_items,
            width_mult = 2,
            radius = [8,24,24,24],
            max_height = 250
        )

        self.menu_file.open()

    def edit_menu(self, btn):
        
        menu_items = [
            {
                'text':'[b]find[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='find':print("find")
            },
            {
                'text':'[b]replace[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='replace':print("replace")
            },
            {
                'text':'[b]taskbar[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='taskbar':print("taskbar")
            },
            {
                'text':'[b]theme[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='theme':print("theme")
            },
            {
                'text':'[b]setting[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='setting':print("setting")
            },
        ]

        self.menu_edit = MDDropdownMenu(
            caller = btn,
            items = menu_items,
            width_mult = 2.3,
            radius = [8,24,24,24],
            max_height = 250
        )

        self.menu_edit.open()
    
    def help_menu(self, btn):

        menu_items =  [
            {
                'text':'[b]short cut[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='short cut':print("short cut")
            },
            {
                'text':'[b]help[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='help':print("new file")
            },
        ]

        self.menu_help = MDDropdownMenu(
            caller = btn,
            items = menu_items,
            width_mult = 2.3,
            radius = [8,24,24,24],
            max_height = 150
        )

        self.menu_help.open()


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
