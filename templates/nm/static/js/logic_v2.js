user_state = 'Mexico City'

d3.json("./static/json/states.json").then((importedData) => {
    let data = importedData;
    let states = [];

    for (i = 0; i < data.length; ++i) {
        states.push(data[i].name)
    }

    var fState = states.filter(s => s.name === user_state);
    var coord = fState.map(f => f.location);
    var z = fState.map(c => c.territory);
    var closeness = 0;

    if (z[0]< 2000){
        closeness = 11;
    }
    else if (z[0] < 6000){
        closeness = 10;
    }
    else if (z[0] < 100000) {
        closeness = 9;
    }
    else if (z[0] < 160000){
        closeness = 8;
    }
    else {
        closeness = 7;
    }

    var myMap = L.map("map", {
        center: coord[0],
        zoom: closeness
      
    });
      
    // Adding tile layer to the map
    L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
    }).addTo(myMap);
      
    var appleIcon = L.icon({
        iconUrl:'./static/data/apple.png',
        iconSize: [20,20]
    })
      
    $.get('./static/data/nutricionist_directory.csv', function(csvFile){
        var data = Papa.parse(csvFile, {header: true, dynamicTyping: true}).data;
        data.forEach( d => {
            L.marker([d.latitud,d.longitud], {icon: appleIcon})
            .bindPopup("</h1>" + d.nom_estab + "</h1> <hr> <h4>Address: " + d.nom_vial + " " 
            + d.numero_ext + ", " + d.tipo_asent + " " + d.nomb_asent + ", C.P. " +
            d.cod_postal + "</h4> <hr> <h4>Phone: " + d.telefono + "</h4>" )
            .addTo(myMap)
        })
    });
      
    // Use this link to get the geojson data.
    // The information was obtained from https://github.com/angelnmara/geojson/blob/master/mexicoHigh.json
    var link = "static/data/mexicoHigh.json";
      
    // Our style object
    var mapStyle = {
        color: "red",
        fillColor: "pink",
        fillOpacity: 0.5,
        weight: 1.5
    };
      
    // Grabbing our GeoJSON data..
    d3.json(link).then(function(data) {
    // Creating a GeoJSON layer with the retrieved data
        L.geoJson(data, {
            style:mapStyle
        }).addTo(myMap);
    });
})