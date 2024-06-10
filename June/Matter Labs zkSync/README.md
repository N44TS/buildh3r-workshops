### Technical Overview

- **ZeekMessages Contract Deployment**
  - Deployed the [ZeekMessages contract here](https://sepolia.explorer.zksync.io/address/0x6BeEEB67b89ac18F95959c369c5a3221DfA36e5E) on zkSync Sepolia network using Remix, enabling message sending functionality.

- **TestToken Contract Deployment**
  - Deployed the [TestToken contract here](https://sepolia.explorer.zksync.io/address/0x741D45f2a0b829De2B7Dd65670b8EBf41194C680) to create the 'Buildh3r' token, with the symbol 'h3r'.
  - Remix does not support zksync-ethers, so when running the `mint-token.ts` script, it did log minting tokens, however this wasn't the case when checking on block explorer.
  - Minted 50 'h3r' tokens directly using Remix, sent to [this address](https://sepolia.explorer.zksync.io/address/0x1Bf1C49Cff8AE3CFc63B36496dA32d9bC7F90366).

- **zkSync Testnet Paymaster**
  - Using Atlas to interact with the testnet paymaster contract provided by zkSync, was able to send a transaction paid for by the newly created token 'h3r' instead of using ETH. As shown in the log here ![consolelog](<Screenshot 2024-06-08 at 01.50.40.png>). 
  - The `paymaster-transaction .ts` script was deployed to send this transaction and a message saying 'this tx cost me no Eth'. 