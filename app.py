from flask import Flask, render_template, jsonify, abort
from db_connect import *

app = Flask(__name__, static_url_path="/static")
app.debug = True

@app.route("/")
def app_index():
	return render_template("index.html")

@app.route('/test/<string:input>', methods = ['GET'])
def get_test(input):
	row = search_location(input)
	if not row:
		abort(404)
	if isinstance(row, list):
		row = row[0]
	return jsonify( { 'lon': row[0], 'lat': row[1], 'blob': row } )

if __name__ == '__main__':
	app.run()
