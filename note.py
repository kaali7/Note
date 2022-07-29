#modules of kivymd
from tkinter import Scrollbar
from kivymd.app import MDApp
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

#modules of kivy
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.button import Button
from kivy.graphics import Color , RoundedRectangle, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.utils import get_hex_from_color as C

#other modules
import os
from datetime import datetime

#ScreenManger 
sm = ScreenManager(transition = NoTransition())

#window fix size
Window.size = (630,450)
# Window.minimum_width, Window.minimum_height = Window.size

#connected to desgin file
Builder.load_file("desgin.kv")

#main variable
title_note_v = [0]
find_text_note = [0]
replace_text_note = [0]

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

# dialog of replace word 
class Replace_Con(BoxLayout):
    
    def find_text(self, text):
        find_text_note[0] = text

    def relplce_text(self, text):
        replace_text_note[0] = text


#Screen
class Main(Screen):

    dialog_title = None
    dialog_new_file = None
    dialog_save_as = None
    dialog_exit_note = None
    dialog_find_word = None
    dialog_replace_word = None
    dialog_emoji = None
    dialog_setting = None
    dialog_short_cut = None
    dialog_about_note = None
    dialog_save_file = None
    dialog_new_file_save =None
    dialog_new_file_dont_save = None
    dialog_exit_note_file = None

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        os.chdir("D:\\sweety\\Git_learn\\project\\gui_project\\file_manager")

        self.text_note = ''
        self.title_note = 'note.txt'
        self.emoji_task = False

    #---------------------------save-button------------------------#

    # if wirte in note ,then color of save button is change  
    def color_save_btn(self, text_btn):

        self.text_note = text_btn
        
        with open(self.title_note, "r") as file:
            text = file.read()
            if text!=text_btn:     
               self.ids.but_save.opacity = 1            
            else:
                self.ids.but_save.opacity = 0.5
            
            file.close()

    def saving_text(self):

        with open(self.title_note, "r") as file:
            text = file.read()

            if text != self.text_note:

                with open(self.title_note, "w") as file:
                    file.write(self.text_note)
                    file.close()
                    
                    self.ids.but_save.opacity = 0.5       

            else:
                print('write something!!!! :| ' )
            
    #----------------------------title dialog-----------------------#

    #change title and close popup 
    def title_change(self, btn):

        old_name = self.title_note
        self.title_note = f"{title_note_v[0]}.txt"
        os.rename(old_name, self.title_note)
        
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

    #save file and create new file   

    def new_file_save_save(self, btn):

        self.title_note = title_note_v[0]+".txt"
        
        create_file = open(self.title_note, "x")
        create_file.close()

        self.ids.note_input.text = ''

        self.dialog_new_file_save.dismiss()

    def new_file_save_cancel(self, btn):

        self.dialog_new_file_save.dismiss()
        
    def new_file_save(self, btn):

        self.dialog_new_file.dismiss()

        # save file 
        with open(self.title_note, "w") as file:
            file.write(self.text_note)
            file.close()

        #create new file
        if not self.dialog_new_file_save:
            self.dialog_new_file_save = MDDialog(
                title  = "New file",
                type = 'custom',
                content_cls = Title_Con(),
                size_hint=(0.4, 0.5),
                buttons=[
                    MDFlatButton(
                        text = "save",
                        on_release = self.new_file_save_save
                    ),
                    MDFlatButton(
                    text = 'cancel',
                    on_release = self.new_file_save_cancel
                    )
                ]
            )

        self.dialog_new_file_save.open()       

    
    #don't save file and create new file

    def new_file_dont_save_save(self, btn):

        self.title_note = title_note_v[0]+".txt"
        
        create_file = open(self.title_note, "x")
        create_file.close()

        self.ids.note_input.text = ''

        self.dialog_new_file_dont_save.dismiss()

    def new_file_dont_save_cancel(self, btn):
        
        self.dialog_new_file_dont_save.dismiss()

    def new_file_dont_save(self, btn):   
        
        self.dialog_new_file.dismiss()

        if not self.dialog_new_file_dont_save:
            self.dialog_new_file_dont_save = MDDialog(
                title  = "New file",
                type = 'custom',
                content_cls = Title_Con(),
                size_hint=(0.4, 0.5),
                buttons=[
                    MDFlatButton(
                        text = "save",
                        on_release = self.new_file_dont_save_save
                    ),
                    MDFlatButton(
                    text = 'cancel',
                    on_release = self.new_file_dont_save_cancel
                    )
                ]
            )

        self.dialog_new_file_dont_save.open()   


    #cancel to create new file
    def new_file_cancel(self, btn):
        self.dialog_new_file.dismiss()

    def new_Cfile_save(self, btn):

        self.title_note = title_note_v[0]+".txt"
        
        create_file = open(self.title_note, "x")
        create_file.close()

        self.ids.note_input.text = ''

        self.dialog_save_file.dismiss()

    def new_Cfile_cancel(self, btn):
        self.dialog_save_file.dismiss()

    #to create new file 
    def new_file(self):

        with open(self.title_note, "r") as file:
            text = file.read()

            if text != self.text_note:

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
            
            else:
                
                if not self.dialog_save_file:
                    self.dialog_save_file = MDDialog(
                        title  = "New file",
                        type = 'custom',
                        content_cls = Title_Con(),
                        size_hint=(0.4, 0.5),
                        buttons=[
                            MDFlatButton(
                                text = "save",
                                on_release = self.new_Cfile_save
                            ),
                            MDFlatButton(
                                text = 'cancel',
                                on_release = self.new_Cfile_cancel
                            )
                        ]

                    )

                self.dialog_save_file.open()

            file.close()

    
    #---------------------------file >>  exit----------------------------------#

    #save and exit from app
    def exit_save(self, btn):  

        #save file
        with open(self.title_note, "w") as file:
            file.write(self.text_note)
            file.close()   
        
        self.dialog_exit_note.dismiss()

        #exit the winodw
        MDApp.get_running_app().stop()
        Window.close()

    #don't save and exit from app
    def exit_dont_save(self, btn):  
        
        self.dialog_exit_note.dismiss()

        MDApp.get_running_app().stop()
        Window.close()
    
    #cancel exit of note window
    def exit_cancel(self, btn):

        self.dialog_exit_note.dismiss()

    #exit a note
    def exit_note(self):

        with open(self.title_note, "r") as file:
            text = file.read()
            
            if text != self.text_note:
                 
                if not self.dialog_exit_note:
                    self.dialog_exit_note = MDDialog(
                        title  = "New file",
                        text = "do you want to save this?",
                        type='custom',
                        size_hint=(0.5,0.5),
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
            else:
                
                MDApp.get_running_app().stop()
                Window.close()
            
            file.close()

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
                'text':'[b]emoji[/b]',
                'viewclass':'OneLineListItem',
                'height':45,
                'font_size':15,
                'on_release':lambda x='emoji':self.emoji()
            }
        ]

        self.menu_edit = MDDropdownMenu(
            caller = btn,
            items = menu_items,
            width_mult = 2.3,
            radius = [8,24,24,24],
            max_height = 250
        )

        self.menu_edit.open()
    
    #-------------------------Edit >> find------------------------#

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
    
    #-------------------------Edit >> replace------------------------#
    
    def replace_save(self, btn):

        find = find_text_note[0]
        repl = replace_text_note[0]

        new_text = self.text_note.replace(find, repl)

        self.text_note = new_text
        self.ids.note_input.text = self.text_note

        self.dialog_replace_word.dismiss()
    
    def replace_cancel(self, btn):
        self.dialog_replace_word.dismiss()

    #replace word in passage
    def replace_word(self):

        if not self.dialog_replace_word:
            self.dialog_replace_word = MDDialog(
                title  = "Replace Word",
                type='custom',
                content_cls = Replace_Con(),
                size_hint = (0.5,0.5),
                buttons=[
                    MDFlatButton(
                        text = 'save',
                        on_release = self.replace_save
                    ),
                    MDFlatButton(
                        text = 'cancel',
                        on_release = self.replace_cancel
                    )
                ]

            )

        #open dialog of new file
        self.dialog_replace_word.open()
    
    #-------------------------Edit >> emoji------------------------#

    #exit the emoji
    def exit_emoji(self, but, *args):

        anime = Animation(height = 1, duration=0.2)

        but.clear_widgets()

        anime.start(but)

        self.emoji_task = False

    #add the taskbar
    def emoji(self, *args):

        emo = self.ids.emoji_show

        anime = Animation(height = 50, duration=0.2)
           
        #scroller 
        scroll = ScrollView(bar_color = (0,0,0,0),bar_inactive_color = (0,0,0,0) ,do_scroll_y = False,size_hint_y = None,height = 45)

        #box of emoji
        emoji_box = BoxLayout(orientation = 'horizontal', size_hint_x = None, width = 700)
          
        #emoji in box
        for i in range(20):
            emoji = Button(text = "\N{winking face}", font_size = 25, size_hint_x =  None, width = 45, pos_hint = {'center_y': 0.5}, font_name = "seguiemj", background_color = (0,0,0,0))
            emoji_box.add_widget(emoji)

        # cancel button 
        cross_btn = MDIconButton(icon = "close-circle-outline", pos_hint = {'center_y': .5})
        cross_btn.bind(on_release = lambda x: self.exit_emoji(emo))

        # emoji_box.add_widget(emoji)
        scroll.add_widget(emoji_box)

        emo.add_widget(scroll)
        emo.add_widget(cross_btn)

        if self.emoji_task == False:
            anime.start(emo)
            self.emoji_task=True

        elif self.emoji_task!= False:
            self.exit_emoji(emo)

    #-------------------------Edit >> setting------------------------#

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
     
    #-------------------------Help >> short cut------------------------#

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

    #-------------------------Help >> about------------------------#
 
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

        

#variable
#note name
note_name_v = [0]

#dialog of file create
class Create_file_Con(BoxLayout):
    
    def note_name(self, text):
        note_name_v[0] = text

#file manager
class File_Manager(Screen):

    dialog_file_create = None
    dialog_delete_file = None

    def __init__(self, **kw):
        super().__init__(**kw)

        self.file_note = ''
        self.file_list = {}

        self.set_note()

    #set note 

    def set_note_save(self, filename):
        # main box
        file_manager = self.ids.note_manager

        file_note = filename

        #file
        File_card = MDCard(orientation = 'horizontal', size_hint_y = None, height = 45, padding = [10,0], radius = [20])
        self.ids[f"{file_note}"] = File_card

        #file open
        file_open_card = MDCard(orientation = 'horizontal', size_hint_y = None, height = 45, radius = [20])
        file_open_card.bind(on_release = lambda x: self.file_open(File_card))

        # file_open_card contents 
        # button 
        file_open_icon = MDIconButton(icon = "file-document-outline", pos_hint = {'center_y': 0.5}, size_hint_x = None)

        # note name
        file_open_name = MDLabel(text = f"[b]{file_note}[/b]",markup = True , font_size = 20)

        #file delete button
        file_delete_btn = MDIconButton(icon = "delete-outline")
        file_delete_btn.bind(on_release = lambda x: self.delete_file(File_card))

        # file_open_card contents are adding
        file_open_card.add_widget(file_open_icon)
        file_open_card.add_widget(file_open_name)
    
        #file_card contents are adding
        File_card.add_widget(file_open_card)
        File_card.add_widget(file_delete_btn)

        #file are adding in file_manager
        file_manager.add_widget(File_card)
            
        #adding file in file_list
        self.file_list.update({f"{File_card}":f"{file_note}"})

    def set_note(self):

        os.chdir("D:\\sweety\\Git_learn\\project\\gui_project\\file_manager")
        file_list_folder = os.listdir()
        num_file = len(file_list_folder)

        # main box
        file_manager = self.ids.note_manager

        #deleted extra space
        extra_spce = self.ids.extra_space
        file_manager.remove_widget(extra_spce)

        for i in range(num_file):
            self.set_note_save(file_list_folder[i])

        #extra space are adding bottom
        extra_label = Label()
        self.ids["extra_space"] = extra_label
        file_manager.add_widget(extra_label)

    #create file
    def create_file_save(self, btn):
        
        self.file_note = note_name_v[0] + ".txt"

        # create a file 
        f = open(self.file_note, "x")
        f.close()

        # main box 
        file_manager = self.ids.note_manager
        # delete the extra_space label 
        extra_spce = self.ids.extra_space
        file_manager.remove_widget(extra_spce)

        File_card = MDCard(orientation = 'horizontal', size_hint_y = None, height = 45, padding = [10,0], radius = [20])
        self.ids[f"{self.file_note}"] = File_card

        file_open_card = MDCard(orientation = 'horizontal', size_hint_y = None, height = 45, radius = [20])
        file_open_card.bind(on_release = lambda x: self.file_open(File_card))

        # file_open_card contents 
        
        # button 
        file_open_icon = MDIconButton(icon = "file-document-outline", pos_hint = {'center_y': 0.5}, size_hint_x = None)

        # note name
        file_open_name = MDLabel(text = f"[b]{self.file_note}[/b]" ,markup = True , font_size = 20)

        #file delete button
        file_delete_btn = MDIconButton(icon = "delete-outline")
        file_delete_btn.bind(on_release = lambda x: self.delete_file(File_card))

        #extra space
        extra_label = Label()
        self.ids["extra_space"] = extra_label

        # file_open_card contents are adding
        file_open_card.add_widget(file_open_icon)
        file_open_card.add_widget(file_open_name)

        #file_card contents are adding
        File_card.add_widget(file_open_card)
        File_card.add_widget(file_delete_btn)

        #file are adding in file_manager
        file_manager.add_widget(File_card)
        file_manager.add_widget(extra_label)

        #adding file in file_list
        self.file_list.update({f"{File_card}":f"{self.file_note}"})


        self.dialog_file_create.dismiss()
    
    def create_file_cancel(self, btn):
        self.dialog_file_create.dismiss()
    
    def create_file(self):

        if not self.dialog_file_create:
            self.dialog_file_create = MDDialog(
                title='Create Note',
                type='custom',
                size_hint = (0.5, 0.4),
                content_cls=Create_file_Con(),
                buttons = [
                    MDFillRoundFlatButton(
                        text="save",
                        on_release=self.create_file_save
                    ),
                    MDFillRoundFlatButton(
                        text="cancel",
                        on_release=self.create_file_cancel
                    )
                ]
            )

        self.dialog_file_create.open()

    #open file
    def file_open(self, obj):
        note_file = self.file_list[str(obj)]
 
        #main
        main = sm.get_screen("main")

        #title name change
        main.ids.note_title.text = note_file
        main.title_note = note_file

        #give text to note
        with open(note_file, "r") as file:
            text = file.read()

            main.ids.note_input.text = text

            file.close()        

        sm.current =  "main"
        
    #delete file
    def delete_file(self, obj):
        
        #del file in file_manage folder
        f = self.file_list[str(obj)]
        os.remove(f)

        #del file in note file_manager
        file_manage = self.ids.note_manager
        file_manage.remove_widget(obj)

        #del file in self.file_list
        self.file_list.pop(str(obj))


#main app
class Note(MDApp):

    def build(self):

        # color theme of app
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"

        sm.add_widget(Main(name="main"))
        sm.add_widget(File_Manager(name='file'))

        return sm

#run app
App = Note()
App.run()
