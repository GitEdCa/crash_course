sandwich_orders = ['tuna', 'ham', 'egg', 'pork', 'chilaquiles']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I've made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("Sandwiches made: ")
for finish in finished_sandwiches:
    print(finish.title())
