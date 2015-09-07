from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
import time
import pymysql
from user.user import User
from user.module import Module
from user.outil import Outil

from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, FallOutTransition, NoTransition
from gui.hoverclasses import HoverButton

class MascaretRoot(FloatLayout):

    def __init__(self):
        super(MascaretRoot, self).__init__()
        self.mascaretloginscreen = MascaretLoginScreen()
        self.add_widget(self.mascaretloginscreen)

    def show_bigscreen(self):
        self.clear_widgets()
        self.mascaretbigscreen = MascaretBigScreen()
        self.add_widget(self.mascaretbigscreen)



class MascaretLoginScreen(FloatLayout):
    login_box = ObjectProperty()
    password_box = ObjectProperty()
    error_box = ObjectProperty()
    login_area = ObjectProperty()

    def login(self):
        animation = Animation(x=self.login_area.x - self.login_area.width, duration=0.8)
        animation.start(self.login_area)
        self.pan_screen= Image(source= "gui/mylogo1.jpg", keep_ratio= False, allow_stretch= True,
                        color= (1, 1, 1, 0.1))
        self.add_widget(self.pan_screen)
        animation.bind(on_complete=self.check_login)

    def check_login(self, *args):
        app = Mascaret.get_running_app()
        user_login = self.login_box.text
        user_password = self.password_box.text

        #######################################
        # DB CONNECTION

        db = pymysql.connect("localhost","root","","mascaretdb")
        cursor = db.cursor()

        login_query = "SELECT * FROM utilisateur WHERE login =%s AND password = %s"
        #a l'avenir capter une exception TMTC la security

        login_data = cursor.execute(login_query,(user_login,user_password))
        cursor.close()
        db.close()

        ########################################

        if login_data:
            global user_logged
            user_logged = User(user_login)
            app.root.show_bigscreen()


        else:
            self.login_box.focus = True
            self.remove_widget(self.pan_screen)
            self.error_box.text = "Wrong credentials"
            # create an animation object. This object could be stored
            # and reused each call or reused across different widgets.
            # += is a sequential step, while &= is in parallel
            animation = Animation(x=(0), t='out_bounce')

            # apply the animation on the button, passed in the "instance" argument
            # Notice that default 'click' animation (changing the button
            # color while the mouse is down) is unchanged.
            animation.start(self.login_area)

class MascaretBigScreen(ScreenManager):
    mode = StringProperty("wide")
    right_panel = ObjectProperty()

    def __init__(self,**kwargs):
        super(MascaretBigScreen, self).__init__()
        self.transition=NoTransition()
        self.add_widget(HomePage())

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
        temporaire = cursor.execute(login_query,(user_logged.login))

        #On obtient une matrice
        module_data = cursor.fetchall()

        list_modules = []

        #On va chercher les infos
        for row in module_data:
            temp_module = Module(str(row[0]))

            module_appearance = False
            for mod in list_modules:
                #Si le module existe deja dans la liste
                if mod.module_name == temp_module.module_name:
                    module_appearance = True
                    index_mod = list_modules.index(mod)
                    break

            if module_appearance:
                list_modules[index_mod].list_outils.append(Outil(str(row[1])))
            else:
                temp_module.list_outils.append(Outil(str(row[1])))
                list_modules.append(temp_module)

        for mod in list_modules:
            print(mod.module_name)


        #    if temp_mode in list_modules
        #    list_modules.append(str(row[0]))

        if temporaire:
            print("SUCCESS")
        cursor.close()
        db.close()

        for mod in [ModuleRH(),ModuleCG(),ModuleCO(),ModuleLO()]:
            self.add_widget(mod)

        ################################################################

        self.right_panel= RightPanel()
        self.current_screen.screen1_box.add_widget(self.right_panel)

    def on_mode(self, widget, mode):
        if mode == "wide" :
            print("wide")
            try:
                self.current_screen.get_screen('2').remove_widget(self.right_panel)
                self.current_screen.screen1_box.add_widget(self.right_panel)
                self.current_screen.right_Button.pos_hint = {'x': 1}
                self.current_screen.right_Button.disabled= True
            except:
                pass
        else:
            print("narrow")
            try:
                self.current_screen.screen1_box.remove_widget(self.right_panel)
                self.current_screen.get_screen('2').add_widget(self.right_panel)
                self.current_screen.right_Button.pos_hint = {'x': 0.93}
                self.current_screen.right_Button.disabled= False
            except:
                pass

        print(user_logged.login)


    def on_right_panel(self, *args):
        pass

class HomePage(Screen, ScreenManager):
    screen1_box= ObjectProperty()
    right_Button= ObjectProperty()

class ModuleRH(Screen, ScreenManager):
    pass

class ModuleCG(Screen, ScreenManager):
    pass

class ModuleCO(Screen, ScreenManager):
    pass

class ModuleLO(Screen, ScreenManager):
    pass


class RightPanel(FloatLayout):
    pass

class RightPanelBtn(Button):
    pass


class Mascaret(App):
    pass
##    def __init__(self):
##        super(Mascaret, self).__init__()

Mascaret().run()
