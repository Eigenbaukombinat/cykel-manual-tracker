

var mymap = L.map('mapid').setView([51.482807, 11.969723], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibmlsbzE5NzkiLCJhIjoiY2s5c284ZmtlMDQ0MDNmb2QxbzNqcTNucCJ9.181WaQu7HGUUB_vhe987jQ'
}).addTo(mymap);


var popup = L.popup();

function onMapClick(e) {
	data = {
		lat: e.latlng.lat,
		lon: e.latlng.lng,
		name: $('input#name').val(),
		voltage: $('input#voltage').val(),
	}
	$.post('/set_tracker', data)
	console.log(data);
    popup
        .setLatLng(e.latlng)
        .setContent("Updated position to " + e.latlng.toString())
        .openOn(mymap);
}

mymap.on('click', onMapClick);

