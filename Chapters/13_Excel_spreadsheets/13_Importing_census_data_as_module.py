import os
import census2010

print(census2010.all_data['AK']['Anchorage'])
anchorage_population = census2010.all_data['AK']['Anchorage']['pop']

print(f'The 2010 population of Anchorage was {anchorage_population}')