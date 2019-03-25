import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import ScreenManagerException
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup


class MainMenu(Screen):
    pass

class NewCustomTraining(Screen):
    pass

class PaceSelection(Screen):
    pass

class SavedCustomTrainings(Screen):
    pass

class SavingCustomTraining(Screen):
    pass


class CustScreenManager(ScreenManager):

    #Sliders
    minslider = NumericProperty(60) # used to reset the sliders
    maxslider = NumericProperty(120)

    def reset_min(self): # forced to do this because = 0 does not work
        self.minslider += 1
        self.minslider -= 1

    def reset_max(self):
        self.maxslider += 1
        self.maxslider -= 1
    #____________________________________________________________________
        
    #Button animation
    @staticmethod
    def button_click(self): # green when cliked, normal when uncliked
        if self.background_color == [.88, .88, .88, 1]:
            self.background_color = [0, 1, 0, 1]
        else:
            self.background_color = [.88, .88, .88, 1]
    #____________________________________________________________________

    #Select all areas button
    @staticmethod
    def areas_select_button(self):
        if self.text == "Select all":
            self.text = "Unselect" + "\n" + "      all"
        else:
            self.text = "Select all"
    
##    @staticmethod
##    def all_areas_selection(self,area_selection_button):
##        area_selection_button = ObjectProperty()
##        button1 = ObjectProperty()
##        button2 = ObjectProperty()
##        button3 = ObjectProperty()
##        button4 = ObjectProperty()
##        button5 = ObjectProperty()
##        button6 = ObjectProperty()
##        button7 = ObjectProperty()
##        list_buttons = [button1,button2,button3,button4,button5,button6,button7]
##        if area_selection_button.text == "Select all":
##            for button in list_buttons:
##                if button.background_colour == [0, 1, 0, 1]:
##                    button.background_color = [.88, .88, .88, 1]
##        else:
##            for button in list_buttons:
##                if button.background_colour == [.88, .88, .88, 1]:
##                    button.background_color = [0, 1, 0, 1]
    
    #____________________________________________________________________

    #Save custom trainings
    class TrainingsListButton(ListItemButton):
        pass
    
    new_training_text_input = ObjectProperty()
    training_list = ObjectProperty()

    def submit_training(self):
        self.training_list.adapter.data.extend([self.new_training_text_input.text])
        self.training_list._trigger_reset_populate()

sm = Builder.load_string("""
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<CustButton@Button>:
    color: 0, 0, 0, 1
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1

<CustLabel@Label>:
    color: 0, 0, 0, 1
    orientation: "vertical"

<CustSpinner@Spinner>:
    color: 0, 0, 0, 1
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1

<TrainingsListButton>:
    font_size: 20
    color: 0, 0, 0, 1
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1
    
CustScreenManager:
<CustScreenManager>:

    new_training_name_text_input: new_training
    training_list: training_list_view
    
    MainMenu:
        name: "MainMenu"
        id: MainMenu
        
        BoxLayout:
            orientation: "vertical"
            padding: 10
            spacing: 10

            CustButton:
                text: "Saved Custom Trainings"
                font_size: 40
                on_press:
                    root.transition.direction = 'left'
                    root.transition.duration = 0.5
                    root.current = 'SavedCustomTrainings'

            CustButton:
                text: "New Custom Training"
                font_size: 40
                on_press:
                    root.transition.direction = 'left'
                    root.transition.duration = 0.5
                    root.current = 'NewCustomTraining'

            CustButton:
                text: "Random"
                font_size: 40



    NewCustomTraining:
        name: "NewCustomTraining"
        id: NewCustomTraining
        BoxLayout:
            orientation: "vertical"
            padding: 10

            BoxLayout:
                orientation: "horizontal"
                size_hint_y: 0.1
                spacing : 5

                CustButton:
                    text: "<= Back"
                    font_size: 25
                    size_hint_x: 3
                    on_press:
                        root.transition.direction = 'right'
                        root.transition.duration = 0.5
                        root.current = 'MainMenu'

                BoxLayout:
                    size_hint_x: 10
                    CustLabel:
                        text:"Custom Training"
                        font_size: 50 

                Button:
                    on_press:
                        root.transition.direction = 'left'
                        root.transition.duration = 0.5
                        root.current = 'SavingCustomTraining'
                    canvas:
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    size_hint_x: 1
                    Image:
                        source: 'disk.png'
                        y: self.parent.y + self.parent.height - 50
                        x: self.parent.x
                        size: 40,40
                        allow_stretch: True
                        
                    
                CustButton:
                    text: "Start"
                    font_size: 25
                    size_hint_x: 3
                    on_press:
                        root.transition.direction = 'left'
                        root.transition.duration = 0.5
                        root.current = 'PaceSelection'


            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint_y: 0.9

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        text: "Speed"
                        font_size: 40

                    BoxLayout:
                        orientation: "horizontal"
                        spacing: 10
                        
                        CustButton:
                            text: "Reset Min"
                            font_size: 20
                            on_press: root.reset_min()

                        CustButton:
                            text: "Reset Max"
                            font_size: 20
                            on_press: root.reset_max()
                            

                    CustLabel:
                        text: "Min Speed: "+str(minslider_id.value)+"km/h  "
                        font_size: 30

                    Slider:
                        id: minslider_id
                        min: 60
                        max: maxslider_id.value
                        value: root.minslider
                        step: 5

                    CustLabel:
                        text: "Max Speed: "+str(maxslider_id.value)+"km/h  "
                        font_size: 30

                    Slider:
                        id: maxslider_id
                        min: minslider_id.value
                        max: 120
                        value: root.maxslider
                        step: 5

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 20

                    CustLabel:
                        text: "Spin"
                        font_size: 40

                    CustButton:
                        text: "Random"
                        font_size: 20
                        on_press:
                            root.button_click(self)

                    CustLabel:
                        text: "Direction"
                        font_size: 30

                    CustSpinner:
                        text: "No Spin"
                        font_size: 25
                        values: ["No Spin","Top Spin", "Right Spin", "Left Spin"]
                        id: spinner_direction_id

                    CustLabel:
                        text: "Speed"
                        font_size: 30

                    CustSpinner:
                        text: "No Spin"
                        font_size: 25
                        values: ["No Spin", "Slow", "Fast"]
                        id: spinnerspeed_id

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        size_hint_y: None
                        height: 80
                        text: "Area"
                        font_size: 40

                    GridLayout:
                        cols: 3
                        rows: 4
                        spacing: 10

                        CustLabel:
                            size_hint_x: 1
                        CustButton:
                            text: "Select all"
                            id: area_selection_button
                            font_size: 20
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.all_areas_selection(self,area_selection_button)
                                root.areas_select_button(self)
                                
                        CustLabel:
                            size_hint_x: 1
                        CustButton:
                            text: "1"
                            font_size: 30
                            id: button1
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustLabel:
                            size_hint_x: 1
                        CustButton:
                            text: "2"
                            font_size: 30
                            id: button2
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustButton:
                            text: "3"
                            font_size: 30
                            id: button3
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustLabel:
                            size_hint_x: 1
                        CustButton:
                            text: "4"
                            font_size: 30
                            id: button4
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustButton:
                            text: "5"
                            font_size: 30
                            id: button5
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustButton:
                            text: "6"
                            font_size: 30
                            id: button6
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
                        CustButton:
                            text: "7"
                            font_size: 30
                            id: button7
                            size_hint_x: 1
                            on_press:
                                root.button_click(self)
                                #root.update_list_areas(self, root.list_areas)
#            Label:
#                size_hint_y: 0.05
#                text: str(root.list_areas)

    PaceSelection:
        name: "PaceSelection"
        id: PaceSelection
        BoxLayout:
            orientation: "vertical"
            padding: 10

            BoxLayout:
                orientation: "horizontal"
                size_hint_y: None
                height: 60

                CustButton:
                    text: "<= Back"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.transition.direction = 'right'
                        root.transition.duration = 0.5
                        root.current = 'NewCustomTraining'

                BoxLayout:
                    size_hint_x: 0.6
                    CustLabel:
                        text:"Custom Training"
                        font_size: 50 

                CustButton:
                    text: "Start"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.transition.direction = 'left'
                        root.transition.duration = 0.5

            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint_y: 0.85

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        text: "Speed"
                        font_size: 40

                    CustLabel:
                        text: "Min Speed: "+str(minslider_id.value)+"km/h  "
                        font_size: 30

                    CustLabel:
                        text: "Max Speed: "+str(maxslider_id.value)+"km/h  "
                        font_size: 30

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 20

                    CustLabel:
                        text: "Spin"
                        font_size: 40

                    CustLabel:
                        text: "Direction\\n" + spinner_direction_id.text
                        font_size: 30

                    CustLabel:
                        text: "Speed\\n" + spinnerspeed_id.text
                        font_size: 30

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        size_hint_y: 6

                    CustLabel:
                        size_hint_y: 20
                        text: "Area"
                        font_size: 40

                    GridLayout:
                        cols: 3
                        rows: 3
                        size_hint_y: 74
                        spacing: 10

                        CustLabel:
                            font_size: 30
                            text: "1"
                            color: button1.background_color
                            size_hint_x: 1
                        CustLabel:
                            size_hint_x: 1
                        CustLabel:
                            font_size: 30
                            text: "2"
                            color: button2.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "3"
                            font_size: 30
                            color: button3.background_color
                            size_hint_x: 1
                        CustLabel:
                            size_hint_x: 1
                        CustLabel:
                            text: "4"
                            font_size: 30
                            color: button4.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "5"
                            font_size: 30
                            color: button5.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "6"
                            font_size: 30
                            color: button6.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "7"
                            font_size: 30
                            color: button7.background_color
                            size_hint_x: 1
                
            BoxLayout:
                orientation: "horizontal"
                size_hint_y: 0.15

                CustLabel:
                    size_hint_x: 0.3
                    text: "Pace: " + str(pace_slider_id.value) + "s"
                    font_size: 30
                    
                Slider:
                    size_hint_x: 0.4
                    id: pace_slider_id
                    min: 1
                    max: 10
                    step: 1

                CustButton:
                    size_hint_x: 0.3
                    text: "Manual"
                    font_size: 25
                    on_press:
                        root.button_click(self)
                        
    SavingCustomTraining:
        name: "SavingCustomTraining"
        id: SavingCustomTraining
        
        BoxLayout:
            orientation: "vertical"
            padding: 10

            BoxLayout:
                orientation: "horizontal"
                size_hint_y: None
                height: 60

                CustButton:
                    text: "<= Back"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.transition.direction = 'right'
                        root.transition.duration = 0.5
                        root.current = 'NewCustomTraining'

                BoxLayout:
                    size_hint_x: 0.6
                    CustLabel:
                        text:"Save Custom Training"
                        font_size: 40 

                CustButton:
                    text: "Save"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.submit_training() #######
                        root.transition.direction = 'left'
                        root.transition.duration = 0.5
                        root.current = 'NewCustomTraining'
                        
            BoxLayout:
                orientation: "horizontal"
                size_hint_y: 0.15
                padding: 10
                
                CustLabel:
                    text: "New Training Name: "
                    font_size: 30
                    size_hint_x: 0.4
                    
                TextInput:
                    id: new_training
                    font_size: 20
                    size_hint_x: 0.6
                    hint_text: "Enter the name here"
                    

            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint_y: 0.85

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        text: "Speed"
                        font_size: 40

                    CustLabel:
                        text: "Min Speed: "+str(minslider_id.value)+"km/h  "
                        font_size: 30

                    CustLabel:
                        text: "Max Speed: "+str(maxslider_id.value)+"km/h  "
                        font_size: 30

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 20

                    CustLabel:
                        text: "Spin"
                        font_size: 40

                    CustLabel:
                        text: "Direction\\n" + spinner_direction_id.text
                        font_size: 30

                    CustLabel:
                        text: "Speed\\n" + spinnerspeed_id.text
                        font_size: 30

                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: 40

                    CustLabel:
                        size_hint_y: 6

                    CustLabel:
                        size_hint_y: 20
                        text: "Area"
                        font_size: 40

                    GridLayout:
                        cols: 3
                        rows: 3
                        size_hint_y: 74
                        spacing: 10

                        CustLabel:
                            font_size: 30
                            text: "1"
                            color: button1.background_color
                            size_hint_x: 1
                        CustLabel:
                            size_hint_x: 1
                        CustLabel:
                            font_size: 30
                            text: "2"
                            color: button2.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "3"
                            font_size: 30
                            color: button3.background_color
                            size_hint_x: 1
                        CustLabel:
                            size_hint_x: 1
                        CustLabel:
                            text: "4"
                            font_size: 30
                            color: button4.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "5"
                            font_size: 30
                            color: button5.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "6"
                            font_size: 30
                            color: button6.background_color
                            size_hint_x: 1
                        CustLabel:
                            text: "7"
                            font_size: 30
                            color: button7.background_color
                            size_hint_x: 1
    
    SavedCustomTrainings:
        name: "SavedCustomTrainings"
        id: SavedCustomTrainings
                
        BoxLayout:
            orientation: "vertical"

            BoxLayout:
                orientation: "horizontal"
                size_hint_y: 0.1

                CustButton:
                    text: "<= Back"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.transition.direction = 'right'
                        root.transition.duration = 0.5
                        root.current = 'MainMenu'

                BoxLayout:
                    size_hint_x: 0.6
                    CustLabel:
                        text:"Saved Custom Training"
                        font_size: 40 

                CustButton:
                    text: "Start"
                    font_size: 25
                    size_hint_x: 0.2
                    on_press:
                        root.transition.direction = 'left'
                        root.transition.duration = 0.5
                        root.current = 'PaceSelection'
            BoxLayout:
                size_hint_y: 0.1
                
            ListView:
                id: training_list_view
                spacing: 10
                adapter:
                    ListAdapter(data=["Training 1"], cls = root.TrainingsListButton)
                    
""")

class TestApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return sm

TestApp().run()
