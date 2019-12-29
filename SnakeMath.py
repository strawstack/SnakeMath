class SnakeMath:
    def __init__(self, debug=False):
        # Debug
        self.D = debug

        # Internal datastructures
        self.stack = []
        self.nests = [] # all pushed nests
        self.nest = []
        for _ in range(5):
            self.nest.append(['.' for _ in range(5)])
        self.nest[4][0] = "s"

        # Symbols
        self.sep = "."
        self.bracket = "()"
        self.open_bracket = "("
        self.close_bracket = ")"
        self.function = "Y"
        self.out = "@"
        self.integer = "ocusS3"

        # State
        self.in_function  = False
        self.bracket_index = 0
        self.bracket_value = 0
        self.cur = []
        self.pos = [4, 0] # row, column
        self.facing = 1 # 0 - up, 1 - right, 2 - down, 3 - left
        self.move = {
            0: [-1, 0],
            1: [0, 1],
            2: [1, 0],
            3: [0, -1]
        }

        self.value = {
            "o": 0,
            "c": 1,
            "u": 2,
            "s": 3,
            "S": 4,
            "3": 5
        }
        if self.D: print("SnakeMath")

    def _base10(self, base6):
        size = len(base6)
        total = 0
        for i, c in enumerate(base6):
            total += self.value[c] * (6**(size - i - 1))
        return total

    def _copyAndClear(self, nest):
        new_nest = []
        for r, row in enumerate(nest):
            new_nest.append(row[:])
            for j, cell in enumerate(nest[r]):
                nest[r][j] = "."
        return new_nest

    def _clear_state(self):
        self.in_function = False
        self.bracket_index = 0
        self.bracket_value = 0
        self.cur.clear()
        self.nests.clear()
        self.stack.clear()
        self.nest.clear()
        for _ in range(5):
            self.nest.append(['.' for _ in range(5)])
        self.nest[4][0] = "s"

    def eval(self, exp):
        self._clear_state()
        i = 0
        while i < len(exp):
            if self.D: print("stack:", self.stack, end=", ")
            if self.D: print("cur:", self.cur)
            c = exp[i]
            if self.D: print("c:", c)

            if c in self.sep:
                if self.D: print("sep")
                self.in_function = False
                if len(self.cur) > 0:
                    self.stack.append(self._base10(self.cur))
                    self.cur.clear()
                i += 1

            elif c in self.bracket:
                if self.D: print("bracket")
                if c in self.open_bracket: # (
                    if self.D: print("  open bracket")
                    self.in_bracket = True
                    self.bracket_index = i + 1
                    self.bracket_value = self.stack.pop() - 1
                    i += 1

                else: # )
                    if self.D: print("  close bracket")

                    if len(self.cur) > 0:
                        self.stack.append(self._base10(self.cur))
                        self.cur.clear()

                    if self.bracket_value > 0:
                        self.bracket_value -= 1
                        i = self.bracket_index
                    else:
                        i += 1

            elif c in self.function:
                if self.D: print("function")
                self.in_function = True
                i += 1

            elif c in self.out:
                if self.D: print("out")
                self.nests.append(self._copyAndClear(self.nest))
                i += 1

            elif self.in_function and (c in self.integer):
                if self.D: print("in_function and function")

                if c == "o":
                    value = self.stack.pop()
                    m = self.move[self.facing]
                    for _ in range(value):
                        nr = self.pos[0] + m[0]
                        nc = self.pos[1] + m[1]
                        if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
                            self.pos[0] = nr
                            self.pos[1] = nc
                            self.nest[nr][nc] = "s"

                elif c == "c":
                    self.facing = (self.facing + 1) % 4

                elif c == "u":
                    self.stack.append(self.stack[-1])

                elif c == "s":
                    v1 = self.stack.pop()
                    v2 = self.stack.pop()
                    self.stack.append(v2 * v1)

                elif c == "S":
                    v1 = self.stack.pop()
                    v2 = self.stack.pop()
                    self.stack.append(v2 - v1)

                elif c == "3":
                    v1 = self.stack.pop()
                    v2 = self.stack.pop()
                    self.stack.append(v2 + v1)

                i += 1

            elif c in self.integer:
                if self.D: print("integer")
                self.cur.append(c)
                i += 1

            else:
                print("Unknown symbol:", c)

        return self.stack

    def show(self):
        SIZE = 5
        print("\nOUTPUT")
        for r in range(SIZE):
            for nest in self.nests:
                nx = " ".join(nest[r]).replace(".", " ")
                print(nx, end="")
            print("")

    def show_stack(self):
        print("\nSTACK:", ", ".join([str(x) for x in self.stack]))
