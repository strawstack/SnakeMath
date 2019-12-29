# SnakeMath

![](./logo.png)

This `readme` covers everything you need to know to understand and start using SnakeMath. The goal of SnakeMath aligns with the simple goals all snakes share: `motivate computer science`, and `promote snake culture`.

`SnakeMath` uses postfix operator syntax, a stack, and a grid to render 5x5 characters. It's inspired by [the adventures of a scientist and his grandson](https://rickandmorty.fandom.com/wiki/Rattlestar_Ricklactica). For example, the following expression renders the letter `S`:

    S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@

# Understanding SnakeMath

To understand SnakeMath you have to understand snakes, or, more specifically, understand *my* understanding of snakes. The following three principles provide a good amount of insight to snake behavior and, by extension, SnakeMath:

1. Snakes like to `slither` along paths.
2. Snakes like to `share` their paths with other snakes.
3. Snakes prefer to slither on `meaningful` paths.

# Why SnakeMath?

Snakes like to `slither`, and snakes like to `share`, so, naturally, snakes have developed a syntax with which they can share expressions that describe the paths they slither along. Snakes like to slither on `meaningful` paths, and paths are all-the-more meaningful if a good `slither-path` can be shared amongst `snake-friends`.

# How SnakeMath Works

**Symbols**: Snake math uses only eleven symbols: `o`, `c`, `u`, `s`, `S`, `3`, `Y`, `.`, `@`, `(`, and `)`.

**The Nest**: The symbols above are combined in specific ways to create SnakeMath `expressions` which `draw` characters to a 5x5 grid (called `the nest`). The state of the 5x5 grid is rendered to form the output of the given SnakeMath expression. Each element of `the nest` is initialized to `.` at the start of an expression.

**The Stack**: SnakeMath expressions are parsed from `left to right` (a direction that snakes like to move). During parsing, integers are pushed to a `stack` (a data-structure that snakes like almost as much as linked-lists do to its similarity to their own bodies). When `operators` are encountered, integers from the stack are sometimes used to preform a calculation, and the result is pushed to the stack. The stack starts out empty at the beginning of an expression.

# Evaluating a SnakeMath Expression

Snakes begin slithering in the lower-left cell of their nest and are facing right. SnakeMath expressions direct a snake to slither around their nest. Every cell in the nest that is touched gets tagged with `s`. In the diagram below, I use `>` to represent a snake that is facing to the right:

    . . . . .
    . . . . .
    . . . . .
    . . . . .
    > . . . .

Let's evaluating the following SnakeMath expression:

    S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@

This expression causes the snake to travel around its nest. The resulting path looks like this:

    s s s s >
    s . . . .
    s s s s s
    . . . . s
    s s s s s

The expression has finished evaluating and the snakes path has the shape of a letter `S`. As we will see below, the operator `@` causes the grid to be saved as one character of output. If the expression were longer, more characters could be saved and output by the expression.

We don't always have to draw something. As a second example, lets use nested brackets to multiply two numbers without using the build-it multiply operator.

    o.uo.(cu.(c.Y3))

This expression has two `embedded` arguments in this example we are multiplying `uo` with `cu` which are in base6; in base10, these numbers are 12 and 8 respectively. After evaluating this expression, we can find the answer as the only element on the stack: 96.

## Integers

- *`o`, `c`, `u`, `s`, `S`, `3`*: These symbols are called `snake shapes` and they can be used to represent the digits of a `base six` integer. Each symbol has a value from 0 to 5. `o is zero` and `3 is five`. `c`, `u`, `s`, `S` have values 1, 2, 3, 4 respectively. Think of `snake shapes` as hex numbers only instead of using `0 to F` to represent `0 to 15`, we use `o to 3` to represent `0 to 5`. Numbers are written so that the left-most digit is the most significant digit. When an integer is parsed during evaluation of a SnakeMath expression, the integer is immediately pushed to the stack.

## Delimiter Symbol

- `.`: This symbol is used as the separator between integers and operators.

## Operator Indicator

- `Y`: This symbol means interpret the next set of symbols as a string of operators. See below for a list of operators.

## Operators

In this section, let `{1}` be the value on the top of the stack, and let `{2}` be the value under {1}.

- `o`: Pop {1}, and move forward by value of {1}.

- `c`: Turn clockwise.

- `u`: Copy {1} and push copy to stack.

- `s`: Pop and `multiply` {1} and {2} then push result.

- `S`: Pop and `subtract` {1} and {2} then push result.

- `3`: Pop and `add` {1} and {2} then push result.

- `@`: Save the current state of the 5x5 grid, and clear the grid.

## Brackets

- `(` and `)`: When an expression is enclosed in brackets. Pop {1} and repeat the enclosed expression a number of times equal to {1} before moving on to the rest of the expression.

# SnakeMath Expressions

This expression causes six numbers to be pushed to the stack.

    cu.su.S3.3.o.co.
    resulting stack: 8, 20, 29, 5, 0, 6

This expression causes the letter `S` to be drawn to the nest.

    S.u.(u.S).u.(Yo.Yccc).u.(Yo.Yc).Yo.@
    resulting nest:
    s s s s s
    s . . . .
    s s s s s
    . . . . s
    s s s s s

# Code in this Repo

**examples.py**: Run this file with `python examples.py`. This file will run some demo expressions, and print the output to the console.

**SnakeMath.py**: This file is the python implementation of SnakeMath.

    s s s s s s s     s s s s s s s     s s s s s s s
    s         s s s   s s       s s   s s   s        
    s s s s s s   s s s s s s s s s s s     s s s s s
            s s     s s s       s s   s s   s        
    s s s s s s       s s       s s     s s s s s s s
