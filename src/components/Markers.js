import React, { useState } from 'react'
import { Marker, Circle } from 'react-leaflet';
import { SchoolLocationIcon } from './SchoolLocationIcon';
import MarkerPopup from './MarkerPopup';

const Markers = ({ candidate }) => {

  const [radius, setRadius] = useState(null);

  const markers = candidate.escolas.map((escola, index) => {
    return (
      <Marker key={index} position={[escola.latitude, escola.longitude]} icon={SchoolLocationIcon} >
        <MarkerPopup school={escola} />
        {escola.quantidadeVotos != 0
          ? <Circle
            center={{ lat: escola.latitude, lng: escola.longitude }}
            fillColor="#f03"
            color="red"
            fillOpacity="0.2"
            radius={escola.quantidadeVotos}
          > <MarkerPopup school={escola} /></Circle>
          : null}
      </Marker>
    )
  });

  return (
    <>
      {markers}
    </>

  )
};

export default Markers;
