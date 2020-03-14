"""
    dotwidget module, usage: import module and
    use it as any other kivy widget
"""
from kivy.properties import (
    ObjectProperty,
    ListProperty,
    NumericProperty,
    BooleanProperty
)
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class Dot(Widget):
    """Dot widget color is the property of the widget color and
        by default is set to green, counter is the number of blinks
        and by default is set to 3, interval is the blinking speed
        and by default is set to 1s it can be also float,
        visibility is boolean property and default to true
        if set to false the widget is not going to be visible
        once when stop blinking so if True opacity = 1 viceversa
        opacity = 0
    """
    color = ListProperty([0, 1, 0, 1])
    _clock = ObjectProperty(allownone=True)
    counter = NumericProperty(6)
    interval = NumericProperty(1)
    _back_counter = NumericProperty()
    visibility = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(rgba=self.color)
            Ellipse(pos=self.pos, size=self.size)

    def start_blink(self):
        """Method to call when the dot has to start blink"""
        if not self._clock:

            self._back_counter = self.counter

            self._clock = Clock.schedule_interval(self._update, self.interval)


    def stop_blink(self):
        """
            Method to call when blinking has to stop by
            default is called after counter's times default 3
        """
        self.counter = self._back_counter

        self._clock.cancel()

        self._clock = None

        self.opacity = 1 if self.visibility else 0

    def _update(self, _):
        """Internal blinking method """

        if self.opacity:

            self.opacity = 0
        else:
            self.opacity = 1

        self.counter -= 1

    def on_counter(self, *_):
        """
            on_counter event, whenever counter changes
            this method is going to be called
        """
        if self.counter == 0:

            self.stop_blink()

    def on_color(self, *args):
        """on_color event, it can be overridden"""
        pass

    def on_interval(self, *args):
        """on_interval event, it can be overridden"""
        pass

    def __del__(self):
        pass