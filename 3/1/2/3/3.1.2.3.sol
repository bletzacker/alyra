pragma solidity ^0.4.25;

contract Assemblee{
    address[] membres;

    string[] public descriptionsDecisions;
    uint[] public votePour;
    uint[] public voteContre;

    function rejoindre() public {
        membres.push(msg.sender);
    }

    function estMembre(address utilisateur) public view returns (bool) {
        for (uint i=0; i<membres.length; i++) {
            if (membres[i] == utilisateur) {
                return true;
            } else {
                return false;
            }
        }
    }

    function proposerDecision(string decision) public {
      if (estMembre(msg.sender)) {
        descriptionsDecisions.push(decision);
        votePour.push(0);
        voteContre.push(0);
      }
    }

    function vote(uint indice, uint vote) public returns (bool) {
      if (vote == 1) {
          votePour[indice] += 1;
          return true;
      } else if (vote == 0) {
          voteContre[indice] += 1;
          return true;
      } else {
          return false;
      }
    }

    function comptabiliser (uint indice) public view returns (int) {
        return (int(votePour[indice]) - int(voteContre[indice]));
    }
}
