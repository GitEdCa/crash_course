def make_car(manufacturer, model, **features):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in features.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
car = make_car('Bajaj', 'Pulsar', color='black/blue', cc=200)
print(car)
car = make_car('Ford', 'Fiesta')
print(car)
