pragma solidity ^0.5.0;

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
