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
        bool estMembre = false;
        for (uint i=0; i<membres.length; i++) {
            if (membres[i] == utilisateur) {
                estMembre = true;
            }
        }
        return estMembre;
    }

    function proposerDecision(string decision) public {
        require(estMembre(msg.sender), "L'adresse n'est pas membre.");
        descriptionsDecisions.push(decision);
        votePour.push(0);
        voteContre.push(0);
    }

    function vote(uint proposition, uint vote) public returns (bool) {
        require(estMembre(msg.sender), "L'adresse n'est pas membre.");
        if (vote == 1) {
            votePour[proposition] += 1;
            return true;
        } else if (vote == 0) {
            voteContre[proposition] += 1;
            return true;
        } else {
            return false;
        }
    }
}
