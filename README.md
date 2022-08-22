# LayerZeroNFT
- Project is being developed in Remix, non-layerzero dependencies are imported from openzeppelin.
- @openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol is an interface for ERC721 tokens \
that handles read/write for metadata URIs.
## Features
- standard ERC721 token \
## Cross-Chain
- function crossChain is called by the Client to initiate a cross-chain transfer \
- dstChainId can be found here https://layerzero.gitbook.io/docs/technical-reference/testnet/testnet-addresses for **testnet** \
  - and here https://layerzero.gitbook.io/docs/technical-reference/mainnet/supported-chain-ids for **mainnet** \
- the _destination for crossChain is the contract address of the NFT on the target/receiving chain \
- function lzReceive is called by the Oracle \

### Deploy OERC721.sol
**Parameters**:
- _endpoint: the "endpoint" of the chain that you are deploying to: https://layerzero.gitbook.io/docs/technical-reference/testnet/testnet-addresses for **testnet** and \
https://layerzero.gitbook.io/docs/technical-reference/mainnet/supported-chain-ids for **mainnet** \
- _startId: usually 0 \
- _MAX: maximum token supply \

**Note**:
The base uri is hardcoded in this example. \
The URI is the base uri + tokenId. \
Gas estimation is flawed and not ready for production, but this should be easy to fix. \
This code has been tested on Rinkeby and Binance Testnet. \

## How Cross-Chain works

1. Token is burned on chain1 \
2. Messaging protocol sends a payload to the oracle, containing the id and the address of the caller \
3. Oracle forwards payload to chain2 \
4. Token is minted again on chain2 \
5. Transfer was successful


## Roadmap
- Issues
1. gas fee estimation - status: resolved
2. chains don't know when token minted on other chains
  - option 1: use messaging protocol to notify on mint => not realtime, so this will cause problems for sure !
  - option 2 (preferred): use startID and maxID to make sure every NFT on every Chain is unique and split the collection up.
  note: not every NFT can be minted on every chain, example: \
    Ids 0-100 can be minted on Binance only!, \
    Ids 101-200 can be minted on Ethereum only!, \
    ... this is a limitation caused by blockchains not being able to communicate in real time and could only  theoretically be solved \
    by advanced cross-chain synchronization.

- Milestone 1
setup a Flask webserver with X dummy URIs \
that returns JSON to opensea and other Dapps \
Status: TBD by 25th of August \

- Milestone 2
write a mint contract that owns the NFT contract \
build dummy website with "mint" button in Flask html - recycle defl8 code \
website can call mint contract => fee is paid for minting \

- Milestone 3
migrate to IPFS

- Milestone 4
deploy to all testnets and make sure everything works as expected.

- Milestone 5
add functionality to website (e.g. cross-chain transfers) \
improve website design

- Launch
...
