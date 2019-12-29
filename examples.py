from SnakeMath import SnakeMath

# Examples
e1 = "S.u.(u.S).u.(Yo.Yu.Yccc).u.(Yo.Yu.Yc).Yo.Y@"
e2 = "cu.su.S3.3.o.co"
e3 = ""

# Call library and evaluate expression
snake = SnakeMath(True)

# Evaluate expression
snake.eval(e2)

# Show expression output
snake.show()

# Show resulting stack
snake.show_stack()
