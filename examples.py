from SnakeMath import SnakeMath

#
# Examples
#

# Draw letter S to the grid
e1 = "S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@"

# Push 8, 20, 29, 5, 0 to the stack
e2 = "cu.su.S3.3.o.co"

# Factorial n, answer pushed to stack
#args   n
e3 = "c.3.c.YS.(Yu.c.Y3).Yu.c.YS.(Ys)"

# Nested brackets multiply 'a' and 'b' using only addition
#       a  b
e4 = "c.S.(3.c.YS.(c.Y3))"

# Call library and evaluate expression
snake = SnakeMath(True)

# Evaluate expression
snake.eval(e3)

# Show expression output
snake.show()

# Show resulting stack
snake.show_stack()
