import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.graphics import Ellipse, InstructionGroup
from test import *

import time
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.core.window import Window





class MainScreen(Screen):
    pass

class MapScreen(Screen):

    def btn_sanctuary(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(584, 450),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_centrum(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(293, 623),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_comhall(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(630, 655),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_adminoffice(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(625, 585),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_youth(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(120, 600),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_southoffice(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(175, 773),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_choirroom(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(1300, 500),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_chapel(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(475, 650),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_southadult(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(315, 685),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_northadult(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(550, 750),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_library(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(655, 605),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_southconf(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(163, 745),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_carecenter(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(230, 740),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_checkin(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(1218, 640),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_warmworld(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(1120, 668),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_starbright(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(1340, 671),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_coffee(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(299, 519),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_restrooms(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(200, 690),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(232, 665),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(492, 586),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(515, 630),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_staircases(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(598, 527),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(490, 705),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()

    def btn_prayerroom(self):
        self.dot = Dot(
            size_hint=(None, None),
            size=(15, 15),  # size of the dot
            pos=(505, 789),  # position of the dot
            counter=5,  # how many times have to blink
            visibility=False,  # if false on stop is hidden
            color=[1, 0, 0, 1],  # color of the widget
            interval=.6  # blinking frequency
        )
        self.add_widget(self.dot)
        self.dot.start_blink()



class PrayerRequests(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("66style.kv")

class MainApp(App):

    def build(self):
        return presentation

if __name__ == "__main__":
    Window.fullscreen = True
    MainApp().run()
