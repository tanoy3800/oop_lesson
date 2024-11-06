import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

x = filter(lambda x: float(x['latitude']) >= 60.0, cities)
for item in x:
    print(item)
print()

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    val = [float(x[aggregation_key]) for x in dict_list]
    print(val)
    return aggregation_function(val)

# Let's write code to
# - print the average temperature for all the cities in Italy
def av_temp(condition, cities_set):
    temps = []
    for item in cities_set:
        if condition(item):
            temps.append(float(item['temperature']))
    # print(temps)
    return sum(temps)/len(temps)

av_temp_Italy = av_temp(lambda x : x['country'] == 'Italy', cities)
print(f'The average temperature of all the cities in Italy :\n{av_temp_Italy}\n')

# - print the average temperature for all the cities in Sweden
av_temp_Sweden = av_temp(lambda x : x['country'] == 'Sweden', cities)
print(f'The average temperature of all the cities in Sweden :\n{av_temp_Sweden}\n')

# - print the min temperature for all the cities in Italy
def min_temp(condition, cities_set):
    temps = []
    for item in cities_set:
        if condition(item):
            temps.append(float(item['temperature']))
    return min(temps)

min_temp_Italy = min_temp(lambda x : x['country'] == 'Italy', cities)
print(f'The min temperature of all the cities in Italy :\n{min_temp_Italy}\n')

# - print the max temperature for all the cities in Sweden
def max_temp(condition, cities_set):
    temps = []
    for item in cities_set:
        if condition(item):
            temps.append(float(item['temperature']))
    return max(temps)

min_temp_Sweden = max_temp(lambda x : x['country'] == 'Sweden', cities)
print(f'The min temperature of all the cities in Sweden :\n{min_temp_Sweden}\n')
