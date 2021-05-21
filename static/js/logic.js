// This is the state where the user is located
var user_state = 'Guanajuato';

// Variable that contains information about Mexico's states
// The information was obtained from https://en.wikipedia.org/wiki/List_of_states_of_Mexico
var states = [
    {
      name: 'Aguascalientes',
      capital: 'Aguascalientes',
      location: [22.016667, -102.35],
      territory: 5615.7,
    },
    {
        name: 'Baja California',
        capital: 'Mexicali',
        location: [30, -115.166667],
        territory: 71450
    },
    {
        name: 'Baja California Sur' ,
        capital: 'La Paz',
        location: [25.85, -111.966667],
        territory: 73909.4
    },
    {
        name: 'Campeche',
        capital: 'Campeche',
        location: [18.833333, -90.4],
        territory: 57484.9
    },
    {
        name: 'Chiapas',
        capital: 'Tuxtla Gutierrez',
        location: [16.416667, -92.416667], 
        territory: 73311
    },
    {
        name: 'Chihuahua',
        capital: 'Chihuahua',
        location: [28.816667, -106.433333],
        territory: 247412.6
    },
    {
        name: 'Coahuila',
        capital: 'Saltillo',
        location: [27.3, -102.05],
        territory: 151594.8
    },
    {
        name: 'Colima',
        capital: 'Colima',
        location: [19.166667, -103.883333],
        territory: 5626.9
    },
    {
        name: 'Durango',
        capital: 'Durango',
        location: [24.933333, -104.916667],
        territory: 123364
    },
    {
        name: 'Mexico City',
        capital: 'Mexico City',
        location: [19.433333, -99.133333],
        territory: 1494.3
    },
    {
        name: 'Guanajuato',
        capital: 'Guanajuato',
        location: [21.016667, -101.266667],
        territory: 30606.7
    },
    {
        name: 'Guerrero',
        capital: 'Chilpancingo',
        location: [17.616667, -99.95],
        territory: 63595.9
    },
    {
        name: 'Hidalgo',
        capital: 'Pachuca',
        location: [20.483333, -98.866667],
        territory:20821.4
    },
    {
        name: 'Jalisco',
        capital: 'Guadalajara',
        location: [20.566667, -103.683333],
        territory: 78595.9

    },
    {
        name: 'State of Mexico',
        capital: 'Toluca',
        location: [19.35, -99.633333],
        territory: 22351.8
    },
    {
        name: 'Michoacan',
        capital: 'Morelia',
        location: [19.166667, -101.9],
        territory: 58598.7
    },
    {
        name: 'Morelos',
        capital: 'Cuernavaca',
        location: [18.75, -99.066667],
        territory: 4878.9
    },
    {
        name: 'Nayarit',
        capital: 'Tepic',
        location: [21.75, -105.233333],
        territory: 27856.5
    },
    {
        name: 'Nuevo Leon',
        capital: 'Monterrey',
        location: [25.566667, -99.966667],
        territory: 64156.2
    },
    {
        name: 'Oaxaca',
        capital: 'Oaxaca',
        location: [17.0669, -96.7203],
        territory: 93757.6
    },
    {
        name: 'Puebla',
        capital: 'Puebla',
        location: [19, -97.883333],
        territory: 34309.6
    },
    {
        name: 'Queretaro',
        capital: 'Queretaro',
        location: [20.583333, -100.383333],
        territory: 11690.6
    },
    {
        name: 'Quintana Roo',
        capital: 'Chetumal',
        location: [19.6, -87.92],
        territory: 17260.8
    },
    {
        name: 'San Luis Potosi',
        capital: 'San Luis Potosi',
        location: [22.6, -100.433333],
        territory: 23605.5
    },
    {
        name: 'Sinaloa',
        capital: 'Culiacan',
        location: [25, -107.5],
        territory: 22148.9 
    },
    {
        name: 'Sonora',
        capital: 'Hermosillo',
        location: [29.646111, -110.868889],
        territory: 179354.7
    },
    {
        name: 'Tabasco',
        capital: 'Villahermosa',
        location: [17.966667, -92.583333],
        territory: 24730.9
    },
    {
        name: 'Tamaulipas',
        capital: 'Ciudad Victoria',
        location: [24.283333, -98.566667],
        territory: 80249.3
    },
    {
        name: 'Tlaxcala',
        capital: 'Tlaxcala',
        location: [19.433333, -98.166667],
        territory: 3996.6
    },
    {
        name: 'Veracruz',
        capital: 'Xalapa',
        location: [19.433333, -96.383333],
        territory: 71823.5
    },
    {
        name:'Yucatan' ,
        capital: 'Merida',
        location: [20.833333, -89],
        territory: 39524.4
    },
    {
        name: 'Zacatecas',
        capital: 'Zacatecas',
        location: [23.3, -102.7],
        territory: 75275.3
    }
    
  ];

// Look out for the information of the state where the user is located
var fState = states.filter(s => s.name === user_state);
var coord = fState.map(f => f.location);
var z = fState.map( c => c.territory)
var closeness = 0

// Conditions to determine the zoom needed according to the state territory
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


////////////////////////////////////////////////////////

// Creating map object
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
