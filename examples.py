from SnakeMath import SnakeMath

#
# Examples
#

# Draw letter S to the nest
e1 = "S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@"

# Push 8, 20, 29, 5, 0 to the stack
e2 = "cu.su.S3.3.o.co"

# Factorial n, answer pushed to stack
#args   n
e3 = "c.3.c.YS.(Yu.c.Y3).Yu.c.YS.(Ys)"

# Nested brackets multiply 'a' and 'b' using only addition
# In this example, a = 12 and b = 8
#       a   b
e4 = "o.uo.(cu.(c.Y3))"

# Write SNAKE
_S = "S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@."
_N = "S.Yccc.Yo.Yc.s.(c.Yoc.c.Yoccc).c.Yoc.c.Yocc.S.Yo.@."
_A = "Yccc.s.(S.Yoc).Yc.u.Yoccc.s.Yo.@."
_K = "Yccc.S.Yocc.u.(u.Yoccc).u.(c.Yoc.c.Yoccc).u.(c.Yccco).Yc.c.Yoccc.c.Yo.u.(c.Yoccc.c.Yoc).@."
_E = "s.(S.Yocc.S.Yoc.u.Yoc).@"
e5 = _S + _N + _A + _K + _E

# Call library and evaluate expression
snake = SnakeMath()

# Evaluate expressions
print("Example 1: Draw letter S to nest")
snake.eval(e1)
snake.show()
snake.show_stack()

print("\n\n\nExample 2: Push integers to the stack")
snake.eval(e2)
snake.show_stack()

print("\n\n\nExample 3: Calculate factorial")
snake.eval(e3)
snake.show_stack()

print("\n\n\nExample 4: Multiply with nested loops and addition")
snake.eval(e4)
snake.show_stack()

print("\n\n\nExample 5: Write the word snake")
snake.eval(e5)
snake.show()
snake.show_stack()
