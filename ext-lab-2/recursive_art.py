import turtle
def snowflake(t, iterations, length, shortening_factor, angle):
  if iterations == 0:
    t.forward(length)
  else:
    iterations = iterations - 1
    length = length / shortening_factor
    snowflake(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    snowflake(t, iterations, length, shortening_factor, angle)
    t.right(angle * 2)
    snowflake(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    snowflake(t, iterations, length, shortening_factor, angle)
t = turtle.Turtle()
t.pencolor('blue')
t.hideturtle()
for i in range(3):
  snowflake(t, 4, 200, 3, 60)
  t.right(120)
turtle.mainloop()