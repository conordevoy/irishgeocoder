import csv
from db_connect import *

def run_all():
	with open("data/addresses_for_task.csv") as my_file:
		data = list(csv.reader(my_file))
	locations = []
	for row in data:
		print row,
		print search_location(row[0])
		# location = search_location(row[0])
		# locations.append(location.insert(0, row))
	# return locations

run_all()