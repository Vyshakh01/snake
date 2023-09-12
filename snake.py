import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
move_dist=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        self.head.shape("turtle")

#        self.head.color("red")
#   screen.tracer(0)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self,position):
        snake = turtle.Turtle()
        snake.shape("circle")
        snake.penup()
        snake.color("red")
        snake.setpos(position)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")
    def extend(self):
        self.add_block(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(move_dist)

    def up(self):
        if self.head.heading() !=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)




#        self.segments[0].left(90)

