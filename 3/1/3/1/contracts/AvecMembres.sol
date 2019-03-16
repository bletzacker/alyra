pragma solidity ^0.5.0;

contract AvecMembres {

    struct Membre {
        address id;
        uint blame;
    }

    Membre[] membres;

    function estMembre(address utilisateur) public view returns (bool) {
        for (uint i=0; i<membres.length; i++) {
            if (membres[i].id == utilisateur) {
                return true;
            }
        }
    }

    function rejoindre() public {
        membres.push(Membre(msg.sender,0));
    }


}
