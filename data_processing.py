import csv, os


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        index = self.search(table)
        if index == -1:
            self.table_database.append(table)
        else:
            print(f"{table}: Duplicated table; nothing to be insert")

    def search(self, table_name):
        for table in self.table_database:
            if table == table_name:
                return table
        return -1

    def __str__(self):
        item = ''
        for x in self.table_database:
            item += str(x) + ", "
        return item

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_key, aggregation_function):
        values = []
        for city in self.table:
            values.append(float(city[aggregation_key]))
        return aggregation_function(values)

    def __str__(self, ) -> str:
        return f"Table: {self.table_name}, with {len(self.table)} variant"


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

all_city = Table('all_city', cities)

city_DB = TableDB()

city_DB.insert(all_city)

# Print the min and max latitude for cities in every country
country = ['Denmark', 'United Kingdom', 'Sweden', 'Turkey', 'Spain', 'France', 'Netherlands', 'Italy', 'Andorra', \
 'Romania', 'Greece', 'Germany', 'Moldova', 'Switzerland', 'Serbia', 'Norway', 'Poland', 'Ukraine', 'Portugal', \
    'Slovakia', 'Belarus', 'Czech Republic', 'Belgium', 'Hungary', 'Bulgaria', 'Ireland', 'Latvia', 'Albania', 'Austria', \
        'Finland', 'Lithuania', 'Slovenia', 'Montenegro', 'Croatia', 'Bosnia and Herzegovina', 'Macedonia', 'Estonia']


func = [min, max]
for _func in func:
    print(f'\n\nprint {_func} for every countries:\n')
    for i in country:
        table = Table(i, cities)
        table = table.filter(lambda x : x['country'] == i)
        sub_city_table = Table('sub_city_table', table)
        val = sub_city_table.aggregate('latitude', _func)
        print(f'{str(_func)} latitude in {i} is {val}')
