prompt = "\nPlease enter a topping"
prompt += "\n(Enter 'quit' when you are finished) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    print("Adding " + topping + " to your pizza")
