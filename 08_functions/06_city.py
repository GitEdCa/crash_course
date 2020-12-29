def city_country(city, country):
    """
    Return the city and its country separated by comma
    """
    return city + ", " + country

cc = city_country("Santiago", "Chile")
cc2 = city_country("Guadalajara", "Mexico")
cc3 = city_country("Buenos Aires", "Argentina")
print(cc)
print(cc2)
print(cc3)
