pragma solidity ^0.4.25;

contract AvecDecisions {

    struct Decision {
        string description;
        uint votePour;
        uint voteContre;
        uint start;
        bool open;
        mapping(address => bool) aVote;
    }

    Decision[] decisions;
}
