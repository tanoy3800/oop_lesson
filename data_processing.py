import csv
import os

# class City:
#     def __init__(self, city, country, temperature, latitude):
#         self.city = city
#         self.country = country
#         self.temperature = float(temperature)
#         self.latitude = float(latitude)

#     def __repr__(self):
#         return f"City(city={self.city}, country={self.country}, temperature={self.temperature}, latitude={self.latitude})"

class CityData:
    def __init__(self, cities, countries):
        self.cities = cities
        self.countries = countries

    def filter(self, condition):
        filtered_list = []
        for item in cities:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_key, aggregation_function):
        values = []
        for city in self.cities:
            values.append(float(city[aggregation_key]))
        return aggregation_function(values)

    def av_temp(self, condition):
        temps = []
        for item in cities:
            if condition(item):
                temps.append(float(item['temperature']))
        return sum(temps)/len(temps)

    def min_temp(self, condition):
        temps = []
        for item in cities:
            if condition(item):
                temps.append(float(item['temperature']))
        return min(temps)

    def max_temp(self, condition):
        temps = []
        for item in cities:
            if condition(item):
                temps.append(float(item['temperature']))
        return max(temps)

    def cities_in_country(self, country_name):
        cic = []
        for city in self.cities:
            if city['country'] == country_name:
                cic.append(str(city['city']))
        return cic


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

city_data = CityData(cities, countries)


# Print the average temperature of all cities
print("The average temperature of all the cities:")
print(city_data.aggregate('temperature', lambda temps: sum(temps) / len(temps)))
print()

# Print all cities in Italy
print("All the cities in Italy:")
italy_cities = city_data.cities_in_country('Italy')
print(italy_cities)
print()

# Print the average temperature for all the cities in Italy
print("The average temperature of all the cities in Italy:")
av_temp_Italy = city_data.av_temp(lambda x: x['country'] == 'Italy')
print(av_temp_Italy)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature of all the cities in Italy:")
max_temp_Italy = city_data.max_temp(lambda x: x['country'] == 'Italy')
print(max_temp_Italy)
print()

# Print the min temperature for all the cities in Italy
print("The min temperature of all the cities in Italy:")
min_temp_Italy = city_data.min_temp(lambda x: x['country'] == 'Italy')
print(min_temp_Italy)
print()

# Print the average temperature for all the cities in Sweden
print("The average temperature of all the cities in Sweden:")
av_temp_Sweden = city_data.av_temp(lambda x: x['country'] == 'Sweden')
print(av_temp_Sweden)
print()

# Print the min temperature for all the cities in Sweden
print("The min temperature of all the cities in Sweden:")
min_temp_Sweden = city_data.min_temp(lambda x: x['country'] == 'Sweden')
print(min_temp_Sweden)
print()

# Print cities with latitude >= 60
print("Cities with latitude >= 60:")
x = city_data.filter(lambda x: float(x['latitude']) >= 60.0)
for item in x:
    print(item['city'], end=', ')
