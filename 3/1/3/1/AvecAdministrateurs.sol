pragma solidity ^0.4.25;
import "./AvecMembres.sol";
import "./AvecDecisions.sol";

contract AvecAdministrateurs is AvecMembres, AvecDecisions {

    address[] administrateurs;

    function estAdministrateur(address utilisateur) public view returns (bool) {
        bool estAdministrateur = false;
        for (uint i=0; i<administrateurs.length; i++) {
            if (administrateurs[i] == utilisateur) {
                estAdministrateur = true;
            }
        }
        return estAdministrateur;
    }

    function nommerAdministrateur(address membre) public {
        require(estAdministrateur(msg.sender), "L'adresse n'est pas administrateur.");
        require(estMembre(membre), "L'adresse n'est pas membre.");
        administrateurs.push(membre);
    }

    function demissionnerAdministrateur() public {
        for (uint i=0; i<administrateurs.length; i++) {
            if (administrateurs[i] == msg.sender) {
                delete administrateurs[i];
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
              delete membres[i];
          }
      }
    }
}
