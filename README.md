# A Geocoder

This is a geocoder for Irish placenames.

Data: a list of placename, the OSI data on townlands and counties.

System: Flask app(Python backend), SQLite, HTTP REST JSON API, Leaflet Map, Javascript frontend

Use case: Enter in a string in a search bar over a map of Ireland. JS form and field validation. Send HTTP request to server. Server handles request, queries data, and returns coordinates and information to be displayed on the map.

## Run App
#### In terminal:
1. **Activate venv**:
  
	```
	source venv/bin/activate
	```
	or **set up a virtualenv and pip install requirements.txt**:
				  
	```
	pip install -r requirements.txt
	```
2. **Execute**:
  ```
  python2 app.py
  ```
3. **Run through Browser**:
	```
  localhost:5000/
  ```
