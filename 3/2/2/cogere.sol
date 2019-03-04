pragma solidity ^0.5.4;

contract Cogere {

    mapping (address => uint) organisateurs;

    constructor() public {
        organisateurs[msg.sender] = 100;
    }

    function transfererOrga(address orga, uint parts) public {
        require(parts < organisateurs[msg.sender]);
        organisateurs[orga] += parts;
        organisateurs[msg.sender] -= parts;
    }

    function estOrga(address orga) public view returns (bool) {
        bool estOrga = false;
        if (organisateurs[orga] > 0) {
            estOrga = true;
        }
        return estOrga;
    }

    function partsOrga(address orga) public view returns (uint) {
        return organisateurs[orga];
    }
}
