import sqlite3

def get_connection():
	try:
		conn = sqlite3.connect('places.db')
	except:
		print "Can't open DB"
	return conn

def search_location(location):
	location = extract_location(location)
	county = location[-1].strip()
	conn = get_connection()
	cur = conn.cursor()
	location[0] = location[0].replace('"', '')
	location[0] = location[0].replace("'", '')
	cur.execute("SELECT * FROM townlands WHERE English_Name = '%s' COLLATE NOCASE" % location[0])
	rows = cur.fetchall()
	if len(rows) > 1:
		for row in rows:
			if row[3] == county.upper():
				return row
		return rows[0]
	if not rows:
		cur.execute("SELECT * FROM counties WHERE County = '%s' COLLATE NOCASE" % county)
	conn.close()
	return rows

def extract_location(location):
	if isinstance(location, list):
		loc_elements = location.split(",")
	else:
		loc_string = location.split();
		loc_elements = location.split(",")
	return loc_elements