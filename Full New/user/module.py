from gui.hoverclasses import HoverButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class HPModuleButton(HoverButton):

    def __init__(self, strLinkedModule):
        super(HPModuleButton, self).__init__()
        self.linkedmodule = strLinkedModule
        self.text= self.linkedmodule
        self.background_normal= 'gui/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)

    def on_release(self):
        self.parent.parent.parent.parent.parent.manager.current = self.linkedmodule

    
class HomePage(Screen, ScreenManager):
    screen1_box= ObjectProperty()
    right_Button= ObjectProperty()
    module_box= ObjectProperty()
    right_panel= ObjectProperty()
    

class Module:

    def __init__(self, module_name, listoutils):
        self.module_name = module_name
        self.list_outils = listoutils

class ModuleGUI(Screen, ScreenManager):
    tools_box = ObjectProperty()
    screen1_box = ObjectProperty()
    right_Button= ObjectProperty()
    right_panel= ObjectProperty()
