pragma solidity ^0.5.0;

contract Assemblee {

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
        for (uint i=0; i<membres.length; i++) {
            if (membres[i] == utilisateur) {
                return true;
            }
        }
    }

    function pasVote(uint indice) internal view returns (bool) {
        return ! decisions[indice].aVote[msg.sender];
    }

    function tempsVote(uint indice) internal view returns (bool) {
        return now < decisions[indice].start + 7 days;
    }

    modifier onlyMember() {
        require(estMembre(msg.sender), "L'adresse n'est pas membre.");
        _;
    }

    function proposerDecision(string memory decision) public onlyMember {
        decisions.push(Decision(decision,0,0,now));
    }

    function voter(uint indice, uint vote) public onlyMember {
        require(vote == 1 || vote == 0, "Sens du vote : 0 ou 1");
        require(pasVote(indice), "L'adresse a déjà voté.");
        require(tempsVote(indice), "L'adresse a dépassé le temps de vote.");
        if (vote == 1) {
            decisions[indice].votePour += 1;
        } else {
            decisions[indice].voteContre += 1;
        }
    }

    function comptabiliser (uint indice) public view returns (int) {
        return (int(decisions[indice].votePour) - int(decisions[indice].voteContre));
    }

}
