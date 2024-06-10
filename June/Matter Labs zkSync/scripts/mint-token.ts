
import {ethers} from "ethers";

// Address of the ERC20 token contract
const TOKEN_CONTRACT_ADDRESS = "0x741D45f2a0b829De2B7Dd65670b8EBf41194C680";
// Wallet that will receive tokens
const RECEIVER_WALLET = "0x1Bf1C49Cff8AE3CFc63B36496dA32d9bC7F90366";
// Amount of tokens to mint in ETH format, e.g. 1.23
const TOKEN_AMOUNT = "50";

(async () => {
  try {
    
// Note that the script needs the ABI which is generated from the compilation artifact.
  // Make sure contract is compiled and artifacts are generated
  const artifactsPath = `browser/contracts/artifacts/TestToken.json` // Change this for different path
  console.log(artifactsPath)

  const metadata = JSON.parse(await remix.call('fileManager', 'getFile', artifactsPath))

  const signer = (new ethers.providers.Web3Provider(web3Provider)).getSigner(0)

  // initialise token contract with address, abi and signer
  const tokenContract= new ethers.Contract(TOKEN_CONTRACT_ADDRESS, metadata.abi, signer);

  console.log("Minting tokens...");
  const tx = await tokenContract.mint(RECEIVER_WALLET, ethers.utils.parseEther(TOKEN_AMOUNT));
  console.log(`Mint transaction is ${tx.hash}`)
  await tx.wait();
  console.log("Success!");

  const balance = tokenContract.balanceOf(RECEIVER_WALLET)
  
  console.log(`The account ${RECEIVER_WALLET} now has ${balance} tokens`)

  } catch (e) {
    console.log(e.message)
  }
})()
