with open("learning_python.txt") as file:
    entire_file = file.read()

print(entire_file.rstrip())

with open("learning_python.txt") as file:
    for line in file:
        print(line.rstrip())

with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
