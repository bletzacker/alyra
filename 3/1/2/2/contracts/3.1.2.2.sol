pragma solidity ^0.5.0;

contract Assemblee {

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
            }
        }
    }

    modifier onlyMember() {
        require(estMembre(msg.sender), "L'adresse n'est pas membre.");
        _;
    }

    function proposerDecision(string memory decision) public onlyMember {
        descriptionsDecisions.push(decision);
        votePour.push(0);
        voteContre.push(0);
    }

    function voter(uint proposition, uint vote) public onlyMember {
        require(vote == 1 || vote == 0, "Sens du vote : 0 ou 1");
        if (vote == 1) {
            votePour[proposition] += 1;
        } else {
            voteContre[proposition] += 1;
        }
    }

}
