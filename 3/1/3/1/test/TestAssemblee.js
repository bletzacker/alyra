const Assemblee = artifacts.require('./Assemblee.sol')

contract('TestAssemblee', function () {

  let instance
  let accounts

  beforeEach('Setup contract for each test', async function () {
    instance = await Assemblee.deployed()
    accounts = await web3.eth.getAccounts()
  })

  it('return false when not a member', async function () {
    assert.equal(await instance.estMembre(accounts[1]), false)
  })

  it('return true when a member has joined', async function () {
    await instance.rejoindre({from: accounts[1]})
    assert.equal(await instance.estMembre(accounts[1]), true)
  })

  it('function comptabiliser is OK', async function () {
    await instance.rejoindre({from: accounts[1]})
    await instance.proposerDecision("Proposition",{from: accounts[1]})
    await instance.rejoindre({from: accounts[2]})
    await instance.rejoindre({from: accounts[3]})
    await instance.voter(0, 1,{from: accounts[1]})
    await instance.voter(0, 0,{from: accounts[2]})
    await instance.voter(0, 0,{from: accounts[3]})
    assert.equal(await instance.comptabiliser(0), -1)
  })

  it('Celui qui déploie le smart contract est le premier administrateur', async function () {
    assert.equal(await instance.estAdministrateur(accounts[0]), true)
  })

  it('Il peut nommer un administrateur', async function () {
    await instance.nommerAdministrateur(accounts[1],{from: accounts[0]})
    assert.equal(await instance.estAdministrateur(accounts[1]), true)
  })

  it('Un administrateur peut démissionner', async function () {
    await instance.nommerAdministrateur(accounts[3],{from: accounts[0]})
    assert.equal(await instance.estAdministrateur(accounts[3]), true)
    await instance.demissionnerAdministrateur({from: accounts[3]})
    assert.equal(await instance.estAdministrateur(accounts[3]), false)
  })

})
