from window import *

window=Window(800 , 100)
window.draw_line(Line(Point(10,1),Point(10,100)),"red")
window.wait_for_close()