# LayerZeroNFT
- Project is being developed in Remix, non-layerzero dependencies are imported from openzeppelin.
- @openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol is an interface for ERC721 tokens
that handles read/write for metadata URIs.
## Features
- standard ERC721 token
## Cross-Chain
- function crossChain is called by the Client to initiate a cross-chain transfer
- dstChainId can be found here https://layerzero.gitbook.io/docs/technical-reference/testnet/testnet-addresses for **testnet**
  - and here https://layerzero.gitbook.io/docs/technical-reference/mainnet/supported-chain-ids for **mainnet**
- the _destination for crossChain is the contract address of the NFT on the target/receiving chain 
- function lzReceive is called by the Oracle

### Deploy OERC721.sol
**Parameters**:
- _endpoint: the "endpoint" of the chain that you are deploying to: https://layerzero.gitbook.io/docs/technical-reference/testnet/testnet-addresses for **testnet** and \
https://layerzero.gitbook.io/docs/technical-reference/mainnet/supported-chain-ids for **mainnet** 
- _startId: usually 0 
- _MAX: maximum token supply 

**Note**:
The base uri is hardcoded in this example. \
The URI is the base uri + tokenId. \
Gas estimation is flawed and not ready for production, but this should be easy to fix. \
This code has been tested on Rinkeby and Binance Testnet. 

## How Cross-Chain works

1. Token is burned on chain1
2. Messaging protocol sends a payload to the oracle, containing the id and the address of the caller
3. Oracle forwards payload to chain2 
4. Token is minted again on chain2 
5. Transfer was successful



