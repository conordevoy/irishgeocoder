import sqlite3

# location = "TULLAHEEN MORE"
def get_connection():
	try:
		conn = sqlite3.connect('places.db')
		print "Connected"
	except:
		print "Can't open DB"
	return conn
