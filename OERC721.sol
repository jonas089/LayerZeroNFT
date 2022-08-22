//SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;
// ERC721
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
// Types
import "@openzeppelin/contracts/utils/Strings.sol";
// URI interface
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
// LayerZero
import "./ILayerZeroEndpoint.sol";
import "./ILayerZeroReceiver.sol";

contract OmniChainNFT is ERC721URIStorage, Ownable, ILayerZeroReceiver {
    uint256 counter = 0;
    uint256 nextId = 0;
    uint256 MAX = 100;
    uint256 gas = 350000;

    ILayerZeroEndpoint public endpoint;
    event ReceiveNFT(
        uint16 _srcChainId,
        address _from,
        uint256 _tokenId,
        uint256 counter
    );
    constructor(
        address _endpoint,
        uint256 startId,
        uint256 _max
    ) ERC721("TestNFT", "TEST") {
        endpoint = ILayerZeroEndpoint(_endpoint);
        nextId = startId;
        MAX = _max;
    }

    // get URI by tokenid
    function getUri(
        uint256 tokenId
    ) external view returns (string memory tokenuri){
        return tokenURI(tokenId);
    }

    // get gas estimate
    function externalEstimateFees(
        uint256 tokenId,
        uint16 _dstChainId
    ) external view returns (string memory maybeFee){
        bytes memory payload = abi.encode(msg.sender, tokenId);
        // encode adapterParams to specify more gas for the destination
        uint16 version = 1;
        bytes memory adapterParams = abi.encodePacked(version, gas);
        (uint256 messageFee, ) = endpoint.estimateFees(
            _dstChainId,
            address(this),
            payload,
            false,
            adapterParams
        );
        return Strings.toString(messageFee);
    }
    // mint token with dummy URI for showcasing
    function mint() external payable {
        // check availability
        require(nextId + 1 <= MAX, "Exceeds supply");
        // pay mint fee
        address recipient = 0x665c6761868f26FfB3ad1934C5E6AfE83CF990F4;
        // fee hardcoded for testing, use uniswap for stable fee in the future.
        uint256 amt = 1000000000000000;
        require(msg.value >= amt, "Value too low for this transaction.");
        (bool success, ) = recipient.call{value:amt}("");
        require(success, "Could not pay fees.");
        // fee paid, continue minting process
        nextId += 1;
        _safeMint(msg.sender, nextId);
        _setTokenURI(nextId, string(abi.encodePacked("http://baseurl/",' ',string(Strings.toString(nextId)))));
        counter += 1;
    }
    // Layerzero functions
    function crossChain(
        uint16 _dstChainId,
        bytes calldata _destination,
        uint256 tokenId
    ) public payable {
        require(msg.sender == ownerOf(tokenId), "Not the owner");
        // burn NFT
        _burn(tokenId);
        counter -= 1;
        bytes memory payload = abi.encode(msg.sender, tokenId);
        // encode adapterParams to specify more gas for the destination
        uint16 version = 1;
        bytes memory adapterParams = abi.encodePacked(version, gas);
        (uint256 messageFee, ) = endpoint.estimateFees(
            _dstChainId,
            address(this),
            payload,
            false,
            adapterParams
        );
        require(
            msg.value >= messageFee,
            Strings.toString(messageFee)
        );
        endpoint.send{value: msg.value}(
            _dstChainId,
            _destination,
            payload,
            payable(msg.sender),
            address(0x0),
            adapterParams
        );
    }
    function lzReceive(
        uint16 _srcChainId,
        bytes memory _from,
        uint64,
        bytes memory _payload
    ) external override {
        require(msg.sender == address(endpoint));
        address from;
        assembly {
            from := mload(add(_from, 20))
        }
        (address toAddress, uint256 tokenId) = abi.decode(
            _payload,
            (address, uint256)
        );
        // mint the tokens
        _safeMint(toAddress, tokenId);
        string(abi.encodePacked("http://baseurl/",' ',string(Strings.toString(nextId))));
        _setTokenURI(nextId, string(abi.encodePacked("http://baseurl/",' ',string(Strings.toString(nextId)))));
        counter += 1;
        emit ReceiveNFT(_srcChainId, toAddress, tokenId, counter);
    }
    // Endpoint.sol estimateFees() returns the fees for the message
    function estimateFees(
        uint16 _dstChainId,
        address _userApplication,
        bytes calldata _payload,
        bool _payInZRO,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee, uint256 zroFee) {
        return
            endpoint.estimateFees(
                _dstChainId,
                _userApplication,
                _payload,
                _payInZRO,
                _adapterParams
            );
    }
}
