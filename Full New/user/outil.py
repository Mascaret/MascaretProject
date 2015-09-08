from gui.hoverclasses import HoverButton
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView, ListItemLabel
from kivy.uix.boxlayout import BoxLayout


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

        if self.parent.parent.parent.parent.parent.parent.mode == "narrow":
            print("rrrr")
            self.parent.parent.parent.parent.manager.transition.direction = 'left'
            self.parent.parent.parent.parent.manager.current = "2"


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

        elif self.linkedoutils_name == "Formulaire dtb 1":

            return Formulaire_database_1()





class Outil:

    def __init__(self,outil_name):
        self.outil_name = outil_name



class Forecast_Tool(RelativeLayout):
    pass

class Liste_Employes(RelativeLayout):
    pass

class CJSL01(RelativeLayout):
    pass

class Creation_Facture(RelativeLayout):
    pass

class Liste_Commandes(RelativeLayout):
    pass

class Formulaire_database_1(RelativeLayout):
    new_legal_entity_box = ObjectProperty()

    def send_new_legal_entity(self):
        print(self.new_legal_entity_box.text)







class TestListItem(ListItemButton):
    pass

class TestList(BoxLayout):
##    list_view = ObjectProperty()
##
##    def force_list_view_update(self):
##        self.list_view.adapter.update_for_new_data()
##        self.list_view._trigger_reset_populate()
##
##    def roster_converter(self, row_index, rec):
##        return {'text': rec['text'],'size_hint_y': None, 'height': 25}
##
##    ListAdapter(data=[{'text': str(i), 'is_selected': False} for i in range(100)],
##                   cls=lb, args_converter=root.roster_converter)
##
##    self.adapter = ListAdapter(data=[{'text': str(i), 'is_selected': False} for i in range(100)],
##                           args_converter=self.roster_converter,
##                           propagate_selection_to_data=True,
##                           cls=ListItemButton)

    def __init__(self, *args, **kwargs):
        super(TestList, self).__init__()
        data = [{'text': str(i), 'is_selected': False} for i in range(100)]

        args_converter = lambda row_index, rec: {'text': rec['text']}

        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=TestListItem,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        list_view = ListView(adapter=list_adapter)
        self.add_widget(list_view)









