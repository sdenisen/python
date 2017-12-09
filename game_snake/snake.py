import random
import time

__author__ = 'sdeni'

from tkinter import Frame, Canvas, Tk
from tkinter.constants import NW, ALL
import ImageTk
from PIL import Image

class Const:
    BOARD_WIDTH = 600
    BOARD_HEIGHT = 600
    DOT_SIZE = 20
    DELAY = 300
    KEY_PORTAL = "g"
    KEY_DOWN = "Down"
    KEY_UP = "Up"
    KEY_RIGHT = "Right"
    KEY_LEFT = "Left"

class Board(Canvas):
    def __init__(self):
        super().__init__(width=Const.BOARD_WIDTH, height=Const.BOARD_HEIGHT, background="black", highlightthickness=0)
        self.init()

    def init(self):
        # load images,
        self.loadImages()

        # init constants/variables
        self.inGame = True
        self.dots = 3
        self.score = 0
        self.is_in_portal = False

        # init start positions of snake/apple
        self.moveX = Const.DOT_SIZE
        self.moveY = 0
        self.appleX = 10*Const.DOT_SIZE
        self.appleY = 5*Const.DOT_SIZE

        # create objects
        self.createObjects()
        # init key events
        self.bind_all("<Key>", self.readKeysEvent)
        self.refreshFrame()


    def refreshFrame(self):
        # check collisions with border and himself
        self.inGame = self.checkCollisions()
        col_apple = self.checkAppleCollision()
        if self.inGame:
            if col_apple:
                self.increaseSnake()
                self.generateNewApple()
                self.showNewScore()
            self.moveSnake()
            self.after(Const.DELAY, self.refreshFrame)
        else:
            self.showGaveOver()


    def loadImages(self):
        iapple = Image.open("icons/apple.jpg")
        self.apple = ImageTk.PhotoImage(iapple)

        ihead = Image.open("icons/snake_head.jpg")
        self.head = ImageTk.PhotoImage(ihead)

        idot = Image.open("icons/snake_dot.jpg")
        self.dot = ImageTk.PhotoImage(idot)

        iportal_input = Image.open("icons/portal_input.jpg")
        self.portal_input = ImageTk.PhotoImage(iportal_input)

        iportal_exit = Image.open("icons/portal_exit.jpg")
        self.portal_exit = ImageTk.PhotoImage(iportal_exit)

    def createObjects(self):
        self.create_text(30, 10, text="Score: {0}".format(self.score), tag="score", fill="white")
        self.create_image(self.appleX, self.appleY, image=self.apple, anchor=NW, tag="apple")
        self.create_image(100, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(80, 50, image=self.dot, anchor=NW, tag="dot")
        self.create_image(60, 50, image=self.dot, anchor=NW, tag="dot")
    
    
    def moveSnake(self):
        head = self.find_withtag("head")
        dots = self.find_withtag("dot")
        items = dots + head

        for z in range(len(items)-1):
            c1_x, c1_y = self.coords(items[z])
            c2_x, c2_y = self.coords(items[z+1])
            self.move(items[z], c2_x-c1_x, c2_y-c1_y )
        self.move(head, self.moveX, self.moveY)

        if self.checkPortalCollisions():
            p_input = self.find_withtag("portal_input")
            p_output = self.find_withtag("portal_exit")[0]
            x1, y1, x2, y2 = self.bbox(p_input)
            overlapping_items = self.find_overlapping(x1, y1, x2, y2)
            if len(overlapping_items) == 2:
                overlapping = list(set(overlapping_items) - set(p_input))
                ox, oy = self.coords(p_output)
                ov_x, ov_y = self.coords(overlapping[0])
                self.move(overlapping[0], ox-ov_x, oy-ov_y)
                ov_x, ov_y = self.coords(overlapping[0])
            else:
                print (overlapping_items)
                raise Exception


    def readKeysEvent(self, e):
        print (e.keysym)
        if e.keysym == Const.KEY_DOWN:
            self.moveX = 0
            self.moveY = Const.DOT_SIZE
        elif e.keysym == Const.KEY_UP:
            self.moveX  = 0
            self.moveY = -1*Const.DOT_SIZE
        elif e.keysym == Const.KEY_LEFT:
            self.moveY = 0
            self.moveX = -1 * Const.DOT_SIZE
        elif e.keysym == Const.KEY_RIGHT:
            self.moveY = 0
            self.moveX = Const.DOT_SIZE
        elif e.keysym == Const.KEY_PORTAL:

            if self.is_in_portal:
                self.removePortal()
                self.is_in_portal = False
            else:
                self.setPortal()
                self.is_in_portal = True

    def removePortal(self):
        portal = self.find_withtag("portal_input")
        self.delete(portal[0])
        portal = self.find_withtag("portal_exit")
        self.delete(portal[0])


    def setPortal(self):
        head = self.find_withtag("head")

        exit_x = random.randint(100, 500)
        exit_y = random.randint(100, 500)

        head_x, head_y = self.coords(head)

        self.create_image(head_x + 3*self.moveX, head_y +3* self.moveY, image=self.portal_input, anchor=NW, tag="portal_input")
        self.create_image(exit_x, exit_y, image=self.portal_exit, anchor=NW, tag="portal_exit")

    def checkPortalCollisions(self):
        if not self.find_withtag("portal_input") or not self.find_withtag("portal_exit"):
            return False

        head = self.find_withtag("head")[0]
        dots = self.find_withtag("dot")
        portal_input = self.find_withtag("portal_input")[0]

        x1, y1, x2, y2 = self.bbox(portal_input)
        overlapping_items = self.find_overlapping(x1, y1, x2, y2)

        if head in overlapping_items:
            return True

        for dot in dots:
            if dot in overlapping_items:
                return True

        return False

    def checkCollisions(self):
        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
        items = dots + head
        x1, y1, x2, y2 = self.bbox(head[0])
        overlapping_items = self.find_overlapping(x1, y1, x2, y2)
        if set(items) - set(overlapping_items)< set(dots):
            return False
        if (x1<0 or x2 >= Const.BOARD_WIDTH + Const.DOT_SIZE) or (y1<0 or y2>Const.BOARD_HEIGHT + Const.DOT_SIZE):
            return False
        return True

    def showGaveOver(self):
        self.delete(ALL)
        self.create_text(Const.BOARD_WIDTH/2, Const.BOARD_HEIGHT/2, text="GAME OVER! With Score: {0}".format(self.score), fill="red")

    def checkAppleCollision(self):
        head = self.find_withtag("head")[0]
        apple = self.find_withtag("apple")[0]

        x1, y1, x2, y2 = self.bbox(head)
        overlapping_items = self.find_overlapping(x1, y1, x2, y2)
        if apple in overlapping_items:
            return True
        return False

    def increaseSnake(self):
        dots = self.find_withtag("dot")

        last = dots[-1:]
        prev_last = dots[-2:-1]

        x1, y1 = self.coords(last)
        x2, y2 = self.coords(prev_last)
        delta_x = x2-x1
        delta_y = y2-y1

        self.create_image(x1+delta_x, y1+delta_y, image=self.dot, anchor=NW, tag="dot")
        self.score +=1

    def generateNewApple(self):
        apple = self.find_withtag("apple")
        self.delete(apple[0])

        x = random.randint(0, Const.BOARD_WIDTH%Const.DOT_SIZE)
        y = random.randint(0, Const.BOARD_HEIGHT%Const.DOT_SIZE)

        self.create_image(x * Const.DOT_SIZE, y * Const.DOT_SIZE, image=self.apple, anchor=NW, tag="apple")

    def showNewScore(self):
        score = self.find_withtag("score")
        self.delete(score[0])
        self.create_text(30, 10, text="Score: {0}".format(self.score), tag="score", fill="white")


class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Snake")
        self.board = Board()
        self.board.pack()

def main():
    root = Tk()
    Snake()
    root.mainloop()


if __name__ == "__main__":
    main()
