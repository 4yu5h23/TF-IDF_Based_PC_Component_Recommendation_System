import turtle

# Function to draw a rectangle with text
def draw_rectangle(t, text, width=150, height=50):
  t.penup()
  t.goto(-width // 2, height // 2)
  t.pendown()
  t.begin_fill()
  for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
  t.end_fill()
  t.penup()
  t.goto(0, height // 4)
  t.pendown()
  t.write(text, align="center", font=("Arial", 12, "normal"))

# Function to draw a decision diamond
def draw_diamond(t, size=30):
  t.penup()
  t.goto(0, 0)
  t.pendown()
  for _ in range(4):
    t.forward(size)
    t.right(135)

# Function to draw a connection line with an arrow
def draw_line(t, start_x, start_y, end_x, end_y, message=None):
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()
  t.goto(end_x, end_y)
  if message:
    t.penup()
    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2
    t.goto(mid_x, mid_y - 10)
    t.write(message, align="center", font=("Arial", 10, "normal"))

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set turtle speed to fastest

# Draw flowchart elements
start_rect = draw_rectangle(t.clone(), "Start")
decision_diamond = draw_diamond(t.clone(), 30)
process_rect = draw_rectangle(t.clone(), "Process")
end_rect = draw_rectangle(t.clone(), "End")

# Draw connecting lines
draw_line(t, start_rect.xcor() + start_rect.boundingbox()[2], start_rect.ycor() - start_rect.boundingbox()[3], 
          decision_diamond.xcor(), decision_diamond.ycor() + decision_diamond.boundingbox()[1])
draw_line(t, decision_diamond.xcor() - decision_diamond.boundingbox()[0], decision_diamond.ycor() - decision_diamond.boundingbox()[3], 
          process_rect.xcor() - process_rect.boundingbox()[0], process_rect.ycor() + process_rect.boundingbox()[1], "Yes")
draw_line(t, decision_diamond.xcor() + decision_diamond.boundingbox()[2], decision_diamond.ycor() - decision_diamond.boundingbox()[3], 
          end_rect.xcor() - end_rect.boundingbox()[0], end_rect.ycor() + end_rect.boundingbox()[1], "No")
draw_line(t, process_rect.xcor() + process_rect.boundingbox()[2], process_rect.ycor() - process_rect.boundingbox()[3], 
          decision_diamond.xcor(), decision_diamond.ycor() + decision_diamond.boundingbox()[1])

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()