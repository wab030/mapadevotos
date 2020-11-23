import React from 'react';
import { Popup } from 'react-leaflet';

const MarkerPopup = ({ school }) => {
    return (<Popup>
        <div className='poup-text'>{school.nome}</div>
        <div className='poup-text'>Votos: {school.quantidadeVotos}</div>
    </Popup>);
};

export default MarkerPopup;
