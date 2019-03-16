pragma solidity ^0.5.0;
import "./AvecAdministrateurs.sol";

contract Assemblee is AvecAdministrateurs {

    string public nomAssemblee;

    constructor(string memory nom) public {
        nomAssemblee = nom;
        membres.push(Membre(msg.sender,0));
        administrateurs.push(msg.sender);
    }

    function pasVote(uint indice) internal view returns (bool) {
        return ! decisions[indice].aVote[msg.sender];
    }

    function tempsVote(uint indice) internal view returns (bool) {
        return now < decisions[indice].start + 7 days;
    }

    function voteOuvert(uint indice) internal view returns (bool) {
        return decisions[indice].open;
    }

    modifier onlyMember() {
        require(estMembre(msg.sender), "L'adresse n'est pas membre.");
        _;
    }

    function proposerDecision(string memory decision) public onlyMember {
      decisions.push(Decision(decision,0,0,now,true));
    }

    function voter(uint indice, uint vote) public onlyMember {
        require(vote == 1 || vote == 0, "Sens du vote : 0 ou 1");
        require(pasVote(indice), "L'adresse a déjà voté.");
        require(tempsVote(indice), "L'adresse a dépassé le temps de vote.");
        require(voteOuvert(indice), "La proposition est fermée.");
        if (vote == 1) {
            decisions[indice].votePour += 1;
            decisions[indice].aVote[msg.sender] = true;
        } else {
            decisions[indice].voteContre += 1;
            decisions[indice].aVote[msg.sender] = true;
        }
    }

    function comptabiliser (uint indice) public view returns (int) {
        return (int(decisions[indice].votePour) - int(decisions[indice].voteContre));
    }

}
