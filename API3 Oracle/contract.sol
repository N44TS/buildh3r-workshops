// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

//contract address = 0xD43e8ceE8475D2d5a3c7a209e447B0961cE6E13B
//deployed on eth sepolia https://sepolia.etherscan.io/address/0xD43e8ceE8475D2d5a3c7a209e447B0961cE6E13B

import "@api3/contracts/api3-server-v1/proxies/interfaces/IProxy.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PriceFeedV1 is Ownable {
    address public anyPriceFeed;

    constructor ()Ownable(msg.sender) {}

    function AnyFeed(address _anypriceFeed) external onlyOwner {
        anyPriceFeed = _anypriceFeed;
    }

//show price of any pairing you can go and  get the address to input from market.api3.org/ethereum-sepolia-testnet
    function readAnyDataFeed() public view returns (uint256, uint256) {
        (int224 value, uint256 timestamp) = IProxy(anyPriceFeed).read();
        uint256 price = uint224(value);
        return (price, timestamp);
    }

//show price of eth/usd pairing
    function EthDataFeed() public view returns (int224 value, uint32 timestamp) {
    (value, timestamp) = IProxy(0x3AB6F598d0A986E86af68E4776C4e9Ca215064fC).read();
    }

//show price of btc/usd pairing
    function BtcDataFeed() public view returns (int224 value, uint32 timestamp) {
    (value, timestamp) = IProxy(0x48b37e0491BF54a989e9E83ec45464E472B94A59).read();
    }

}

