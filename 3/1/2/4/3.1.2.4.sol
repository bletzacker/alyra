pragma solidity ^0.4.25;

contract Assemblee{
    address[] membres;

    struct Decision {
        string description;
        uint votePour;
        uint voteContre;
        mapping(address => bool) aVote;
        uint start;
    }

    Decision[] decisions;

    function rejoindre() public {
        membres.push(msg.sender);
    }

    function estMembre(address utilisateur) public view returns (bool) {
        bool estMembre = false;
        for (uint i=0; i<membres.length; i++) {
            if (membres[i] == utilisateur) {
                estMembre = true;
            }
        }
        return estMembre;
    }

    function pasVote(uint indice) public view returns (bool) {
        return ! decisions[indice].aVote[msg.sender];
    }

    function tempsVote(uint indice) public view returns (bool) {
        return now < decisions[indice].start + 7 days;
    }

    function proposerDecision(string decision) public {
      require(estMembre(msg.sender), "L'adresse n'est pas membre.");
      decisions.push(Decision(decision,0,0,now));
    }

    function vote(uint indice, uint vote) public returns (bool) {
      require(estMembre(msg.sender), "L'adresse n'est pas membre.");
      require(pasVote(indice), "L'adresse a déjà voté.");
      require(tempsVote(indice), "L'adresse a dépassé le temps de vote.");
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
