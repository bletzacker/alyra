pragma solidity ^0.4.25;
import "./AvecAdministrateurs.sol";

contract Assemblee is AvecAdministrateurs {

    string public nomAssemblee;

    constructor(string nom) public {
        nomAssemblee = nom;
        membres.push(Membre(msg.sender,0));
        administrateurs.push(msg.sender);
    }

    function pasVote(uint indice) public view returns (bool) {
        return ! decisions[indice].aVote[msg.sender];
    }

    function tempsVote(uint indice) public view returns (bool) {
        return now < decisions[indice].start + 7 days;
    }

    function voteOuvert(uint indice) public view returns (bool) {
        return decisions[indice].open;
    }

    function proposerDecision(string decision) public {
      require(estMembre(msg.sender), "L'adresse n'est pas membre.");
      decisions.push(Decision(decision,0,0,now,true));
    }

    function vote(uint indice, uint vote) public returns (bool) {
      require(estMembre(msg.sender), "L'adresse n'est pas membre.");
      require(pasVote(indice), "L'adresse a déjà voté.");
      require(tempsVote(indice), "L'adresse a dépassé le temps de vote.");
      require(voteOuvert(indice), "La proposition est fermée.");
      if (vote == 1) {
          decisions[indice].votePour += 1;
          decisions[indice].aVote[msg.sender] = true;
          return true;
      } else if (vote == 0) {
          decisions[indice].voteContre += 1;
          decisions[indice].aVote[msg.sender] = true;
          return true;
      } else {
          return false;
      }
    }

    function comptabiliser (uint indice) public view returns (int) {
        return (int(decisions[indice].votePour) - int(decisions[indice].voteContre));
    }
}
