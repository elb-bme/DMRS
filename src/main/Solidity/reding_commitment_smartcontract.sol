// Example in Solidity for Ethereum
pragma solidity ^0.8.0;

contract MeterReadingCommitments {
    struct ReadingCommitment {
        string meterId;
        uint256 timestamp;
        string commitment;
    }

    ReadingCommitment[] public commitments;

    function addCommitment(string memory meterId, string memory commitment) public {
        commitments.push(ReadingCommitment(meterId, block.timestamp, commitment));
    }

    function getCommitment(uint index) public view returns (ReadingCommitment memory) {
        require(index < commitments.length, "Index out of bounds.");
        return commitments[index];
    }
}