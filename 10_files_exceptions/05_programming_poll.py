filename = "programming_poll.txt"

with open(filename, "a") as file:
    while True:
        reason = input("Why do you like to program? ")
        file.write(reason.title() + "\n")
