class Submarine:
    x = 0
    y = 0

    def __init__(self, name):
        self.name = name
        self.pos = 0
        self.depth = 0
        self.aim = 0

    def __str__(self):
        return f"Submarine {self.name} is at position {self.pos} at a depth of {self.depth}"

    def move(self, scalar):
        self.pos += scalar
        self.depth += self.aim * scalar

    def depth_delta(self, scalar):
        self.aim += scalar


foo = Submarine("yellow")

print(foo)

with open('input.txt', 'r') as inputfile:
    commands = inputfile.readlines()

# Main loop to parse directions
for command in commands:
    args = command.strip().split(" ")
    # print(f'{args}')

    if "forward" in args[0]:
        foo.move(int(args[1]))
    elif "up" in command:
        foo.depth_delta(-int(args[1]))
    elif "down" in command:
        foo.depth_delta(int(args[1]))
    else:
        print("huh?")

# Final position
print(foo)
answer = int(foo.pos * foo.depth)
print(f"answer: {answer}")
