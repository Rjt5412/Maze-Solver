from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    
    p1 = Point(0,0)
    p2 = Point(500,500)

    line = Line(p1, p2)

    win.draw_line(line, "red")

    win.wait_for_close()


if __name__=="__main__":
    main()