from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
import time
import pymysql
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, FallOutTransition, NoTransition





class HoverBehavior(object):
    """Hover behavior.
 
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """
 
    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''
 
    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)
 
    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        #Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            #We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')
 
    def on_enter(self):
        pass
 
    def on_leave(self):
        pass




class HoverButton(Button, HoverBehavior):
    def on_enter(self):
        self.background_normal= 'rectbut2.png'
 
    def on_leave(self):
        self.background_normal= 'rectbut1.png'






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
        self.pan_screen= Image(source= "mylogo1.jpg", keep_ratio= False, allow_stretch= True,
                        color= (1, 1, 1, 0.1))
        self.add_widget(self.pan_screen)
        animation.bind(on_complete=self.check_login)

    def check_login(self, *args):
        app = Mascaret.get_running_app()
        user_login = self.login_box.text
        user_password = self.password_box.text

        db = pymysql.connect("localhost","root","","mascaretdb")
        cursor = db.cursor()

        login_query = "SELECT * FROM utilisateur WHERE login =%s AND password = %s"
        #a l'avenir capter une exception TMTC la security
        
        login_data = cursor.execute(login_query,(user_login,user_password))

        
        if login_data:
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
        for mod in [ModuleRH(),ModuleCG(),ModuleCO(),ModuleLO()]:
            self.add_widget(mod)
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








