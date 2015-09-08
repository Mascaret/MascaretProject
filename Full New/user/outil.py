from gui.hoverclasses import HoverButton


class HPOutilsButton(HoverButton):

    def __init__(self, strLinkedOutils):
        super(HPOutilsButton, self).__init__()
        self.linkedoutils = strLinkedOutils
        self.text= self.linkedoutils
        self.background_normal= 'gui/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)

    def on_release(self):
        print(self.linkedoutils)
##        self.parent.parent.parent.parent.parent.manager.current = self.linkedoutils




class Outil:

    def __init__(self,outil_name):
        self.outil_name = outil_name
