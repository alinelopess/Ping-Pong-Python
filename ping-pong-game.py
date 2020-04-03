# Ping-Pong Game by Aline Lopes (https://github.com/alinelopess) made in DataScienceAcademy Course

from tkinter import *  # Creates a graphical interface
import random
import time

level = int(input("Hi there! What level would you like to play? 1/2/3/4/5 \n"))
length = 500 / level


class Ball:
    def __init__(self, canvas, Bar, color):
        self.canvas = canvas
        self.Bar = Bar
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Draw a ball
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Bar_pos = self.canvas.coords(self.Bar.id)

        if pos[2] >= self.Bar_pos[0] and pos[0] <= self.Bar_pos[2]:
            if pos[3] >= self.Bar_pos[1] and pos[3] <= self.Bar_pos[3]:
                self.y = -3
                global count
                count += 1
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Bar:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    #   Draw the bar
    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Bar.draw()
    Ball.draw()


def score():
    canvas.itemconfig(score_now, text="Points: " + str(count))


def game_over():
    canvas.itemconfig(game, text="Game over!")

root = Tk()  # This class allows widgets to be used in the application
root.title("Ping Pong Game")
root.resizable(0, 0)  # Used to allow Tkinter root window to change it’s size according to the users need
root.wm_attributes("-topmost", -1)  # Always keep window on top of others

canvas = Canvas(root, width=900, height=500, bd=0, highlightthickness=0)  # Canvas is used to move objects from one
# position to another in any canvas or tkinter toplevel
canvas.pack()  # Organizes widgets in blocks before placing them in the parent widget
canvas.configure(background='pink')  # Background color

root.update()

# Variable
count = 0
lost = False

Bar = Bar(canvas, "white")  # Color of bar
Ball = Ball(canvas, Bar, "black")  # Color of ball

score_now = canvas.create_text(430, 20, text="Points: " + str(count), fill="black",
                               font=("Purisa", 16))  # Text for point u ma
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Purisa", 40))

canvas.bind_all("<Button-1>", start_game)

root.mainloop()  # To display the screen. Without the event loop, the interface will not be displayed.
