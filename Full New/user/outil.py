from gui.hoverclasses import HoverButton
from kivy.uix.floatlayout import FloatLayout


class HPOutilsButton(HoverButton):

    def __init__(self, strLinkedOutils):
        super(HPOutilsButton, self).__init__()
        self.linkedoutils_name = strLinkedOutils
        self.text= self.linkedoutils_name
        self.background_normal= 'gui/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)
        self.linkedoutils = self.define_linked_tool()
            

    def on_release(self):
        print(self.linkedoutils_name)

        self.parent.parent.parent.parent.parent.right_panel.clear_widgets()
        self.parent.parent.parent.parent.parent.right_panel.add_widget(self.linkedoutils)
        

    def define_linked_tool(self):

        if self.linkedoutils_name == "Forecast tool":

            return Forecast_Tool()
        
        elif self.linkedoutils_name == "Liste employes":

            return Liste_Employes()

        elif self.linkedoutils_name == "CJSL01":

            return CJSL01()

        elif self.linkedoutils_name == "Creation facture":

            return Creation_Facture()

        elif self.linkedoutils_name == "Liste commandes":

            return Liste_Commandes()


class Outil:

    def __init__(self,outil_name):
        self.outil_name = outil_name



class Forecast_Tool(FloatLayout):
    pass

class Liste_Employes(FloatLayout):
    pass

class CJSL01(FloatLayout):
    pass

class Creation_Facture(FloatLayout):
    pass

class Liste_Commandes(FloatLayout):
    pass
