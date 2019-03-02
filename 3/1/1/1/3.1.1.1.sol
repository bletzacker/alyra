pragma solidity ^0.4.25;
contract SceneOuverte {

  uint constant artistesMaximum = 12;
  string[artistesMaximum] passagesArtistes;
  uint artistesInscrits;
  uint tour;

  function sInscrire(string nomDArtiste) public {
    if (artistesInscrits < artistesMaximum) {
      passagesArtistes[artistesInscrits] = nomDArtiste;
      artistesInscrits += 1;
    }
  }

  function passerArtisteSuivant() public {
    if (tour < artistesInscrits) {
      tour += 1;
    }
  }

  function artisteEnCours() public constant returns (string) {
    if (tour < artistesInscrits) {
      return passagesArtistes[tour];
    }
    else {
      return "FIN";
    }
  }
}
