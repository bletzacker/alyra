pragma solidity ^0.5.0;
import "./AvecMembres.sol";
import "./AvecDecisions.sol";

contract AvecAdministrateurs is AvecMembres, AvecDecisions {

    address[] administrateurs;

    function estAdministrateur(address utilisateur) public view returns (bool) {
        for (uint i=0; i<administrateurs.length; i++) {
            if (administrateurs[i] == utilisateur) {
                return true;
            }
        }
    }

    function nommerAdministrateur(address membre) public {
        require(estAdministrateur(msg.sender), "L'adresse n'est pas administrateur.");
        require(! estAdministrateur(membre), "L'adresse est déjà administrateur");
        require(estMembre(membre), "L'adresse n'est pas membre.");
        administrateurs.push(membre);
    }

    function demissionnerAdministrateur() public {
        for (uint i=0; i<administrateurs.length; i++) {
            if (administrateurs[i] == msg.sender) {
                administrateurs[i] = administrateurs[administrateurs.length - 1];
                delete administrateurs[administrateurs.length - 1];
                administrateurs.length--;
            }
        }
    }

    function fermerDecision(uint indice) public {
        require(estAdministrateur(msg.sender), "L'adresse n'est pas administrateur.");
        decisions[indice].open = false;
    }

    function donnerBlame(address utilisateur) public {
      require(estAdministrateur(msg.sender), "L'adresse n'est pas administrateur.");
      for (uint i=0; i<membres.length; i++) {
          if (membres[i].id == utilisateur) {
              membres[i].blame += 1;
          }
          if (membres[i].blame == 2) {
            membres[i] = membres[membres.length - 1];
            delete membres[membres.length - 1];
            membres.length--;
          }
      }
    }
}
