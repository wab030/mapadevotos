import L from 'leaflet';

export const SchoolLocationIcon = L.icon({
  iconUrl: require('../assets/venue_location_icon.svg'),
  iconRetinaUrl: require('../assets/venue_location_icon.svg'),
  iconAnchor: null,
  shadowUrl: null,
  shadowSize: null,
  shadowAnchor: null,
  iconSize: [5, 5],
  className: 'leaflet-venue-icon'
});

export const SchoolCircleIcon = L.circle({
  color: 'red',
  fillColor: '#f03',
  weight: 1,
  fillOpacity: 0.2
})


// export const SchoolLocationIcon = L.icon({
//   iconUrl: require('../assets/venue_location_icon.svg'),
//   iconRetinaUrl: require('../assets/venue_location_icon.svg'),
//   iconAnchor: null,
//   shadowUrl: null,
//   shadowSize: null,
//   shadowAnchor: null,
//   iconSize: [35, 35],
//   className: 'leaflet-venue-icon'
// });