pragma solidity ^0.5.4;
import "./cogere.sol";

contract CagnotteFestival is Cogere {

    mapping (address => bool) festivaliers;
    mapping (address => string) sponsors;
    uint maxSponsors = 3;

    function acheterTicket() public payable {
        require(msg.value >= 500 finney,"Place à 0,5 Ethers");
        festivaliers[msg.sender] = true;
    }

    function sponsoriser(string memory nom) public payable {
        require(msg.value >= 30 ether,"Sponsoring à 30 Ethers");
        require(maxSponsors > 0,"Maximum de sponsors atteint");
        sponsors[msg.sender] = nom;
        maxSponsors -= 1;
    }

    function payer(address payable destinataire, uint montant) public {
        require(estOrga(msg.sender));
        require(destinataire != address(0));
        require(montant > 0);
        destinataire.transfer(montant);
    }

    function nomSponsor(address adresse) public view returns (string memory) {
        return sponsors[adresse];
    }
}
