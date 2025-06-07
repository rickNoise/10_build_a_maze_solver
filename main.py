from Window import Window
from Point import Point
from Line import Line


def main():
    win = Window(800, 600)

    line1 = Line(Point(20, 20), Point(200,20))
    line2 = Line(Point(20, 20), Point(20,200))
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()
