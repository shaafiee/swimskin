async function main() {

	const [deployer] = await ethers.getSigners();

	const startDate = Math.floor(+new Date() / 1000);

	console.log(
		startDate
	);

	console.log(
	"Deploying contracts with the account:",
	deployer.address
	);

	console.log("Account balance:", (await deployer.getBalance()).toString());

	//deployTransaction.gasLimit = 200000;
	const okaybeers = await ethers.getContractFactory("okaybeards");
	const contract = await okaybeers.deploy("Okay Beards", "OKB", 5555);

	console.log("Contract deployed at:", contract.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
	console.error(error);
	process.exit(1);
  });
