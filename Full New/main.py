from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
import time
import pymysql
from user.user import User
from user.module import Module, HPModuleButton, HomePage, ModuleGUI
from user.outil import Outil, HPOutilsButton
from gui.loginscreen import MascaretLoginScreen
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, FallOutTransition, NoTransition
from gui.hoverclasses import HoverButton

class MascaretRoot(FloatLayout):

    def __init__(self):
        super(MascaretRoot, self).__init__()
        self.mascaretloginscreen = MascaretLogScreen()
        self.add_widget(self.mascaretloginscreen)

    def show_bigscreen(self):
        self.clear_widgets()
        self.mascarethomescreen = MascaretHomeScreen()
        self.add_widget(self.mascarethomescreen)


class MascaretHomeScreen(ScreenManager):
    mode = StringProperty("wide")

    def __init__(self,**kwargs):
        super(MascaretHomeScreen, self).__init__()
        self.transition=NoTransition()

        module_data = self.get_module_available()

        self.homepage = HomePage()
        self.add_widget(self.homepage)

        self.create_modules_and_tools(module_data)
                  
        
##        self.right_panel= RightPanel()
##        self.current_screen.screen1_box.add_widget(self.right_panel)


    def get_module_available(self):
        
                ###################Looking into Module#####################

        #DB CONNECTION
        db = pymysql.connect("localhost","root","","mascaretdb")
        cursor = db.cursor()

        login_query = """SELECT m.intitule, o.intitule
                        FROM module AS m , outil AS o, utilisateur AS u, utilisateuroutil AS uo
                        WHERE u.login =%s AND uo.idUtilisateur = u.idUtilisateur
                        AND uo.idOutil = o.idOutil AND o.idModule = m.idModule"""
        # METTRE UN BLOC TRY

        #Execute la requete SQL, mettre un try
        global user_logged
        temporaire = cursor.execute(login_query,(user_logged.login))

        #On obtient une matrice
        module_data = cursor.fetchall()

        cursor.close()
        db.close()

        return module_data

    
    def create_modules_and_tools(self, module_data):

        list_modules = []

        #On va chercher les infos
        for row in module_data:

            module_appearance = False
            for mod in list_modules:
                #Si le module existe deja dans la liste
                if mod.module_name == str(row[0]):
                    module_appearance = True
                    index_mod = list_modules.index(mod)
                    break

            if module_appearance:
                list_modules[index_mod].list_outils.append(Outil(str(row[1])))
            else:
                temp_module = Module(str(row[0]),[])
                temp_module.list_outils.append(Outil(str(row[1])))
                list_modules.append(temp_module)

        #On créer la GUI pour chaque Module
        for mod in list_modules:
            newmodule = ModuleGUI(name = mod.module_name)
            for tools in mod.list_outils:
                newmodule.tools_box.add_widget(HPOutilsButton(tools.outil_name))
            self.add_widget(newmodule)
            self.homepage.module_box.add_widget(HPModuleButton(strLinkedModule=mod.module_name))
    


    def on_mode(self, widget, mode):
        if mode == "wide" :
            print("wide")
            for screen in self.screens:
                print(screen.name)
                screen.right_Button.pos_hint = {'x': 1}
                screen.right_Button.disabled= True
                try:
                    screen.get_screen('2').remove_widget(screen.right_panel)    
                except:
                    pass
                try:
                    screen.screen1_box.add_widget(screen.right_panel)
                except:
                    pass

            
        else:
            print("narrow")
            for screen in self.screens:
                print(screen.name)
                screen.right_Button.pos_hint = {'x': 0.93}
                screen.right_Button.disabled= False
                try:
                    screen.screen1_box.remove_widget(screen.right_panel)
                except:
                    pass
                try:
                    screen.get_screen('2').add_widget(screen.right_panel)
                except:
                    pass








class MascaretLogScreen(MascaretLoginScreen):
    def on_right_id(self):
        app = Mascaret.get_running_app()
        app.root.show_bigscreen()



class RightPanel(FloatLayout):
    pass

class RightPanelBtn(Button):
    pass


class Mascaret(App):
    global user_logged
    user_logged = User("claeysremi")

Mascaret().run()
