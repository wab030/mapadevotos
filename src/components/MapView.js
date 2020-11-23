import React, { useState } from 'react';
import { Map, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import data from '../assets/data';
import Markers from './Markers';
import candidates from '../assets/candidates.json';
import './MapView.css';

const MapView = () => {

  const [currentLocation, setCurrentLocation] = useState({lat:-22.930556,lng:-47.058833});
  const [zoom, setZoom] = useState(12);
  const [candidate, setCandidate] = useState(null);
  const [totalVotes, setTotalVotes] = useState(0);

  const handleChange = (event) => {
    sumVotes(event.target.value);
    setCandidate(candidates.candidates[event.target.value]);
  };

  const sumVotes = (cand) =>{
    let totalVotes = 0;
    console.log(candidates.candidates[cand]);
    candidates.candidates[cand].escolas.map((escola) => {
      totalVotes = totalVotes + escola.quantidadeVotos;
    });
    console.log(totalVotes);
  }


  const clearMap = () => {
    console.log("Clear map");
  };

  return (
    <Map center={currentLocation} zoom={zoom}>
      <div className="titulo">
        <p>Mapa de Votos - Campinas - 2020</p>
      </div>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
      />
      <div className="controles">
        <label>Candidato/a:</label>
        <select onChange={handleChange}>
          {candidates.candidates.map((candidate, key) => {
            return (
              <option key={key} value={key}>{candidate.nomeCandidato}</option>
            )
          })}
        </select>
        <div id="boxTotalVotos"></div>
        <div className="limpaMapa">
          <button onClick={clearMap}>Limpa Mapa</button>
        </div>
      </div>
      {candidate ?
        <Markers candidate={candidate} />
        :
        null}
      <footer className="rodape">
        <p>
          <a href="mailto:albordignon@gmail.com"
          >Desenvolvido por André Luís Bordignon</a
          >
        </p>
        <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">
          <img
            alt="Licença Creative Commons"
            // style="border-width: 0;"
            src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"
          />
        </a>
        <p>Este trabalho está licenciado com uma Licença</p>
        <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"
        >Creative Commons - Atribuição-NãoComercial 4.0 Internacional </a
        >
      </footer>
    </Map>
  );
}

export default MapView;
