var Assemblee = artifacts.require("Assemblee");

module.exports = function(deployer) {
  deployer.deploy(Assemblee,"ONU");
};
