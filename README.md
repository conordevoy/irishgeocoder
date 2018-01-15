This is a geocoder for Irish placenames.

Data: a list of placename, the OSI data on townlands and counties.

System: Flask app(Python backend), SQLite, HTTP REST JSON API, Leaflet Map, Javascript frontend

Use case: Enter in a string in a search bar over a map of Ireland. JS form and field validation. Sned HTTP request to server. Server handles request, queries data, and returns coordinates and information to be displayed on the map.
