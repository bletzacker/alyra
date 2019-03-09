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

  it('function comptabiliser is OK', async function () {
    await instance.rejoindre({from: accounts[0]})
    await instance.proposerDecision("Propisition",{from: accounts[0]})
    await instance.voter(0, 1,{from: accounts[0]})
    await instance.voter(0, 0,{from: accounts[0]})
    await instance.voter(0, 0,{from: accounts[0]})
    assert.equal(await instance.comptabiliser(0), -1)
  })

})
