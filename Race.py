from graphics import GraphWin, Image, Point, Line, Text
from Dice import Dice

class Horse:
    def __init__(self, speed, y, image, window):
        #Starting position
        self.x_pos = 100
        self.y_pos = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        self.x_pos += self.dice.roll()

    def draw(self):
        self.image.draw_at_pos(self.window, self.x_pos, self.y_pos)

    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x

def main():
    win = GraphWin("Pokemon Race", 1650, 800, autoflush = False)

    # images
    image1 = Image(Point(0, 0), "Charmander.gif")
    image2 = Image(Point(0, 0), "Squirtle.gif")
    image3 = Image(Point(0, 0), "Bulbasaur.gif")



    # Horses
    pokemon1 = Horse(3, 100, image1, win)
    pokemon2 = Horse(3, 350, image2, win)
    pokemon3 = Horse(3, 600, image3, win)

    # Finish Line
    finish_x = 1450
    finish_line = Line(Point(finish_x, 50), Point(finish_x, 850))
    finish_line.setWidth(10)
    finish_line.setFill("red")

    #Finish Text
    finish_text = Text(Point(finish_x, 30), "FINISH LINE")
    finish_text.draw(win)

    # race draw
    finish_line.draw(win)
    pokemon1.draw()
    pokemon2.draw()
    pokemon3.draw()
    win.flush()

    print("Click the window to start race!!")
    win.getMouse()

    # loop
    race_over = False
    while race_over == False:
        win.clear_win()
        finish_line.draw(win)
        finish_text.draw(win)

        # move horses
        pokemon1.move()
        pokemon2.move()
        pokemon3.move()

        # redraw
        pokemon1.draw()
        pokemon2.draw()
        pokemon3.draw()

        win.flush()

        win.checkMouse()

        if pokemon1.crossed_finish_line(finish_x) == True:
            race_over = True
        elif pokemon2.crossed_finish_line(finish_x) == True:
            race_over = True
        elif pokemon3.crossed_finish_line(finish_x) == True:
            race_over = True

    win1 = pokemon1.crossed_finish_line(finish_x)
    win2 = pokemon2.crossed_finish_line(finish_x)
    win3 = pokemon3.crossed_finish_line(finish_x)

    if win1 == True and win2 == True:
        print("Tie Horse 1 with Horse 2")
    elif win2 == True and win3 == True:
        print("Tie Horse 2 with Horse 3")
    elif win1 == True and win3 == True:
        print("Tie Horse 1 with Horse 3")
    elif win1 == True:
        print("Horse 1 is the winner")
    elif win2 == True:
        print("Horse 2 is the winner")
    elif win3 == True:
        print("Horse 3 is the winner")
    else:
        print("Everyone tied!")

    print("Race over! Click to close.")
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()



