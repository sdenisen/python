__author__ = 'sdeni'

import time
from tkinter import *
from WSLib.web_client import EngineActions

class Application(Frame):

    BTN_HEIGHT=5
    BTN_WIDTH=15
    BTN_NAME_LEFT = 'left'
    BTN_NAME_RIGHT = 'right'
    BTN_NAME_DOWN = 'down'
    BTN_NAME_UP = 'up'
    BTN_NAME_STOP = 'stop'

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.btn_left = Button(self.parent, text = '<', width=self.BTN_WIDTH, height=self.BTN_HEIGHT, name=self.BTN_NAME_LEFT)
        self.btn_stop = Button(self.parent, text = 'STOP', width=self.BTN_WIDTH, height=self.BTN_HEIGHT, name=self.BTN_NAME_STOP)
        self.btn_right = Button(self.parent, text = '>', width=self.BTN_WIDTH, height=self.BTN_HEIGHT, name=self.BTN_NAME_RIGHT)
        self.btn_top = Button(self.parent, text = '/\\', width=self.BTN_WIDTH, height=self.BTN_HEIGHT, name=self.BTN_NAME_UP)
        self.btn_bottom = Button(self.parent, text = '\\/', width=self.BTN_WIDTH, height=self.BTN_HEIGHT, name=self.BTN_NAME_DOWN)

        self.btn_bottom.place(x=150, y=300)
        self.btn_top.place(x=150, y=100)
        self.btn_right.place(x=280, y=200)
        self.btn_stop.place(x=150, y=200)
        self.btn_left.place(x=20, y=200)

        self.parent.bind("<Key>", self.eventHandler)
        self.parent.focus()

        self.web_ea = EngineActions("http://192.168.1.121:5000")

    def bindControls(self):
        self.btn_left.bind("<Button-1>", self.eventHandler)
        self.btn_right.bind("<Button-1>", self.eventHandler)
        self.btn_top.bind("<Button-1>", self.eventHandler)
        self.btn_bottom.bind("<Button-1>", self.eventHandler)
        self.btn_stop.bind("<Button-1>", self.eventHandler)


    def eventHandler(self, event=None):
        if not event:
            return

        keycode = None
        button_name = None

        if isinstance(event.widget, Tk):
            keycode = event.keycode
        elif isinstance(event.widget, Button):
            button_name = event.widget._name


        print (keycode)
        if keycode == 38 or button_name==self.BTN_NAME_UP: # Up
            print ("Up")
            self.web_ea.stop()
            time.sleep(1)
            self.web_ea.forward()

        elif keycode == 37 or button_name==self.BTN_NAME_LEFT: # Left
            print ("Left")
            self.web_ea.stop()
            time.sleep(1)
            self.web_ea.left()
        elif keycode == 40 or button_name==self.BTN_NAME_DOWN: # Down
            print ("Down")
            self.web_ea.stop()
            time.sleep(1)
            self.web_ea.backward()
        elif keycode == 39 or button_name==self.BTN_NAME_RIGHT: # Right
            print ("Right")
            self.web_ea.stop()
            time.sleep(1)
            self.web_ea.right()
        elif keycode == 13 or button_name==self.BTN_NAME_STOP: # Stop
            print ("Stop")
            self.web_ea.stop()


root = Tk()
root.resizable(False, False)
root.minsize(500, 500)
root.maxsize(1000, 1000)
root.size()
app = Application(root)
app.pack(side='top', fill='x')
print (app.btn_bottom)
app.bindControls()
root.mainloop()