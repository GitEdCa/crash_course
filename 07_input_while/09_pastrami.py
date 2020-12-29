sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'egg', 'pork', 'pastrami', 'chilaquiles']
finished_sandwiches = []

print(sandwich_orders)
print("We run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I've made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("Sandwiches made: ")
for finish in finished_sandwiches:
    print(finish.title())
