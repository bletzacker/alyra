pragma solidity ^0.4.25;

contract AvecMembres {

    struct Membre {
        address id;
        uint blame;
    }

    Membre[] membres;

    function estMembre(address utilisateur) public view returns (bool) {
        bool estMembre = false;
        for (uint i=0; i<membres.length; i++) {
            if (membres[i].id == utilisateur) {
                estMembre = true;
            }
        }
        return estMembre;
    }

    function rejoindre() public {
        membres.push(Membre(msg.sender,0));
    }
}
