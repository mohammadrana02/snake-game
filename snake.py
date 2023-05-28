from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # the snake segments are held in this list
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # function that creates the snake
        for position in STARTING_POSITIONS:  # creates 3 snake segments
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # each snake segment is a square-shaped turtle
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):  # increases the length of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):  # controls how the snake moves
        for seg_num in range(len(self.segments) - 1, 0, -1):  # connects the snake segments together in movement
            new_x = self.segments[seg_num - 1].xcor()  # gets the x-value for the segments in front of it
            new_y = self.segments[seg_num - 1].ycor()  # get the y-value for the segment in front of it
            self.segments[seg_num].goto(new_x, new_y)  # the segment goes to the location of the segment in front
        self.segments[0].forward(MOVE_DISTANCE)  # default movement is forward

    def up(self):  # the changing direction of the head controls the snake movement
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
