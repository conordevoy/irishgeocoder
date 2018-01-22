$(document).ready(function() {
	var map = L.map('map').setView([53.34981, -6.26024], 12);
	map.zoomControl.setPosition('topright');
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

	$(".pressSubmit").click(function() {
		var input = $(".searchWords").val();
		$.ajax({
	        url: "http://localhost:5000/test/" + input
	    }).then(function(data) {
	        $('.results').html(data.blob);
	        L.marker([data.lat, data.lon]).addTo(map);
	        map.panTo(new L.LatLng(data.lat, data.lon));
	    });
	});
});