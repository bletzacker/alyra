const Assemblee = artifacts.require('./Assemblee.sol')

contract('TestAssemblee', function () {

  let instance
  let accounts

  beforeEach('Setup contract for each test', async function () {
    instance = await Assemblee.deployed()
    accounts = await web3.eth.getAccounts()
  })

  it('return false when not a member', async function () {
    assert.equal(await instance.estMembre(accounts[0]), false)
  })

  it('return true when a member has joined', async function () {
    await instance.rejoindre({from: accounts[0]})
    assert.equal(await instance.estMembre(accounts[0]), true)
  })

})
