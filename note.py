#import 
from fileinput import filename
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.button import Button
from kivy.graphics import Color , RoundedRectangle
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

#os
import os

#window fix size
Window.size = (630,450)
# Window.minimum_width, Window.minimum_height = Window.size

#connected to desgin file
Builder.load_file("desgin.kv")

#main variable
title_note_v = [0]

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

#dialog of about note
class About_Note_Con(BoxLayout):
    pass

#dialog of short cut
class Short_Cut_Con(ScrollView):
    pass 

#dialog of title change
class Title_Con(BoxLayout):
    
    def text_title(self, text):
        title_note_v[0] = text

#Screen
class Main(Screen):

    dialog_title = None
    dialog_new_file = None
    dialog_save_as = None
    dialog_exit_note = None
    dialog_find_word = None
    dialog_replace_word = None
    dialog_taskbar = None
    dialog_setting = None
    dialog_short_cut = None
    dialog_about_note = None
    dialog_save_file = None

    def __init__(self, **kw):
        super().__init__(**kw)

        os.chdir("D:\\sweety\\Git_learn\\project\\gui_project\\file_manager")

        self.text_note = ''
        self.title_note = ''

    #---------------------------save-button------------------------#

    # if wirte in note ,then color of save button is change  
    def color_save_btn(self, text_btn):

        self.text_note = text_btn

        list_file = os.listdir()

        if self.title_note in list_file:
            with open(self.title_note, "r") as file:
                text = file.read()
                if text!=text_btn:
                    self.ids.but_save.opacity = 1
                else:
                    self.ids.but_save.opacity = 0.5
        else:
            if len(self.text_note)!=0:
                self.ids.but_save.opacity = 1
            else:
                self.ids.but_save.opacity = 0.5

    def close_save_file(self, btn):

        self.title_note = f"{title_note_v[0]}.txt"
        self.ids.note_title.text = self.title_note

        file = open(self.title_note, "a")
        file.write(self.text_note)
        self.text_note = ""
        file.close()

        self.ids.but_save.opacity = 0.5

        self.dialog_save_file.dismiss()

    def saving_text(self):

        list_file = os.listdir()

        if len(self.text_note) != 0:

            if self.title_note in list_file:

                with open(self.title_note, "a") as file:
                    file.write(self.text_note)
                    self.text_note = ''
                    file.close()
                
                self.ids.but_save.opacity = 0.5
                

                
            else:
                
                if not self.dialog_save_file:
                    self.dialog_save_file = MDDialog(
                        title = "Change Title",
                        type = 'custom',
                        content_cls = Title_Con(),
                        size_hint=(0.4, 0.5),
                        buttons = [
                            MDFlatButton(
                                text =  "save",
                                on_release = self.close_save_file
                            )
                        ]

                    )   

                self.dialog_save_file.open()          

        else:
            print('Sorry!')
            
    #----------------------------title dialog-----------------------#

    #change title and close popup 
    def title_change(self, btn):

        self.title_note = f"{title_note_v[0]}.txt"
        self.ids.note_title.text = self.title_note
        self.dialog_title.dismiss()
     
    # close title popup 
    def close_title(self, btn):
        self.dialog_title.dismiss()

    #title change
    def popup_title(self):

        if not self.dialog_title:
            self.dialog_title = MDDialog(
                title = "Change Title",
                type = 'custom',
                content_cls = Title_Con(),
                size_hint=(0.4, 0.5),
                buttons = [
                    MDFlatButton(
                        text =  "cancel",
                        on_release = self.close_title
                    ),
                    MDFlatButton(
                        text = "save",
                        on_release = self.title_change
                    )
                ]

            )
        
        self.dialog_title.open()
     
    #-------------------------File option------------------------#

    #file management option
    def file_menu(self, btn):

        menu_items = [
            {
                'text':'[b]new file[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='file':self.new_file()
            },
            {
                'text':'[b]save as[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='save as':self.save_as()
            },
            {
                'text':'exit',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='exit':self.exit_note()
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

    #save file and create new file     #isssue -----@@@@@@@55-

    def new_file_save(self, btn):

        self.dialog_new_file.dismiss()
    
    #don't save file and create new file
    def new_file_dont_save(self, btn):    #smalll issue --@#%^&*()
        
        self.dialog_new_file.dismiss()

    #cancel to create new file
    def new_file_cancel(self, btn):
        self.dialog_new_file.dismiss()

    #to create new file 
    def new_file(self):

        if not self.dialog_new_file:
            self.dialog_new_file = MDDialog(
                title  = "New file",
                text = "do you want to save this?",
                type='custom',
                size_hint=(0.5,0.5),
                buttons=[
                    MDFlatButton(
                        text = "save",
                        on_release = self.new_file_save
                    ),
                    MDFlatButton(
                        text = 'don\'t save',
                        on_release = self.new_file_dont_save
                    ),
                    MDFlatButton(
                        text = 'cancel',
                        on_release = self.new_file_cancel
                    )
                ]

            )

        #open dialog of new file
        self.dialog_new_file.open()

    def save_as_ok(self, btn):
        

        self.dialog_save_as.dismiss()

    #to save the file in any dir
    def save_as(self):     #issue ------------ @#%^&*()
        
        if not self.dialog_save_as:
            self.dialog_save_as = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = 'ok',
                        on_release = self.save_as_ok
                    )
                ]

            )

        #open dialog of new file
        self.dialog_save_as.open()
    

    #save and exit from app
    def exit_save(self, btn):     #issue---------------!@#%^&
        
        self.dialog_exit_note.dismiss()

        MDApp.get_running_app().stop()
        Window.close()

    #don't save and exit from app
    def exit_dont_save(self, btn):  #issue -----------%^&*
        
        self.dialog_exit_note.dismiss()

        MDApp.get_running_app().stop()
        Window.close()
    
    def exit_cancel(self, btn): #issue----------@#%^&

        self.dialog_exit_note.dismiss()

    #exit a note
    def exit_note(self):

        if not self.dialog_exit_note:
            self.dialog_exit_note = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = "save",
                        on_release = self.exit_save
                    ),
                    MDFlatButton(
                        text = 'don\'t save',
                        on_release = self.exit_dont_save
                    ),
                    MDFlatButton(
                        text = 'cancel',
                        on_release = self.exit_cancel
                    )
                ]

            )

        #open dialog of new file
        self.dialog_exit_note.open()


    #-------------------------Edit option------------------------#

    #edit to note option
    def edit_menu(self, btn):
        
        menu_items = [
            {
                'text':'[b]find[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='find':self.find_word()
            },
            {
                'text':'[b]replace[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='replace':self.replace_word()
            },
            {
                'text':'[b]taskbar[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='taskbar':self.taskbar()
            },
            {
                'text':'[b]setting[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='setting':self.setting()
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
    
    def find_save(self, btn):
        self.dialog_find_word.dismiss()

    #find word in passage
    def find_word(self):

        if not self.dialog_find_word:
            self.dialog_find_word = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = 'save',
                        on_release = self.find_save
                    )
                ]

            )

        #open dialog of new file
        self.dialog_find_word.open()

    def replace_save(self, btn):
        self.dialog_replace_word.dismiss()
    
    #replace word in passage
    def replace_word(self):

        if not self.dialog_replace_word:
            self.dialog_replace_word = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = 'save',
                        on_release = self.replace_save
                    )
                ]

            )

        #open dialog of new file
        self.dialog_replace_word.open()

    def taskbar_save(self, btn):
        self.dialog_taskbar.dismiss()

    #add the taskbar
    def taskbar(self):
        if not self.dialog_taskbar:
            self.dialog_taskbar = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = 'save',
                        on_release = self.taskbar_save
                    )
                ]

            )

        #open dialog of new file
        self.dialog_taskbar.open()
    
    def setting_save(self, btn):
        self.dialog_setting.dismiss()

    #setting for note
    def setting(self):

        if not self.dialog_setting:
            self.dialog_setting = MDDialog(
                title  = "New file",
                type='custom',
                buttons=[
                    MDFlatButton(
                        text = 'save',
                        on_release = self.setting_save
                    )
                ]

            )

        #open dialog of new file
        self.dialog_setting.open()


    #-------------------------Help option------------------------#
    def help_menu(self, btn):

        menu_items =  [
            {
                'text':'[b]short cut[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='short_cut':self.short_cut()
            },
            {
                'text':'[b]about[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='about':self.about_note()
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
     
    # close short cut dialog 
    def close_short_cut(self, btn):
        self.dialog_short_cut.dismiss()
    
    #show a all short cut in note
    def short_cut(self):
        
        if not self.dialog_short_cut:
            self.dialog_short_cut = MDDialog(
                title="All Short Cut",
                type="custom",
                size_hint = (0.7, 1),
                content_cls=Short_Cut_Con(),
                buttons=[ 
                    MDFillRoundFlatButton(
                        text="ok",
                        on_release=self.close_short_cut
                    )
                ]

            )
        
        self.dialog_short_cut.open()

    # close about note dialog 
    def close_about_note(self, btn):
        self.dialog_about_note.dismiss()

    #show about note
    def about_note(self):
        
        if not self.dialog_about_note:
            self.dialog_about_note = MDDialog(
                title='About Note',
                type='custom',
                size_hint = (0.6, 0.4),
                content_cls=About_Note_Con(),
                buttons = [
                    MDFillRoundFlatButton(
                        text="ok",
                        on_release=self.close_about_note
                    )
                ]
            )

        self.dialog_about_note.open()


#file manager
class File_Manager(Screen):
    pass

#main app
class Note(MDApp):

    def build(self):

        # color theme of app
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        
        self.sm = ScreenManager(transition = NoTransition())

        self.sm.add_widget(Main(name="main"))
        self.sm.add_widget(File_Manager(name='file'))

        return self.sm

#run app
App = Note()
App.run()
