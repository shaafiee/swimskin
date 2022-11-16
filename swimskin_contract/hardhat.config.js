/**
 * @type import('hardhat/config').HardhatUserConfig
 */
require("@nomiclabs/hardhat-waffle");

module.exports = {
  networks: {
    ropsten: {
      //url: 'http://localhost:18545',
      url: 'https://magical-practical-sea.quiknode.pro/39b28feab3034038d882963bd793b1892250ff06/',
      //url: 'https://speedy-nodes-nyc.moralis.io/9f0f16131df267d7415fe3fc/eth/ropsten',
      //url: 'https://speedy-nodes-nyc.moralis.io/9f0f16131df267d7415fe3fc/eth/ropsten',
      //url: 'https://speedy-nodes-nyc.moralis.io/9f0f16131df267d7415fe3fc/eth/rinkeby',
      //url: 'https://ropsten.infura.io/v3/449f7070f7b24d26aa9293edfed73436',
      //accounts: ['0x16553f520b12ad99d68c492f6968d97c5f5beecf928508006d2d907532641754'],
      accounts: ['0x9c2b6fd4d820436acac5015173fe9b7b9bdebda69cd08e8596631bb10b384808'],
      //accounts: ['0x6c859fadd3e5c5784c95eb62cd967685b71fc1c60d71664493b59feb09585a6f'],
      //accounts: ['0x344238b19d8dd6b8e7c340dd0de69e15590b0dbd7e67657971d374f3a501ab08'],
    }
  },
  solidity: {
    version: "0.8.0",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  }
};
