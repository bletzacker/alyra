const Cogere = artifacts.require('./Cogere.sol')

contract('Cogere', function () {

  let instance
  let accounts

  beforeEach('Setup contract for each test', async function () {
    instance = await Cogere.deployed()
    accounts = await web3.eth.getAccounts()
  })

  it('return true when a organisator', async function () {
    assert.equal(await instance.estOrga(accounts[0]), true)
  })

  it('return false when not a organisator', async function () {
    assert.equal(await instance.estOrga(accounts[1]), false)
  })

  it('Un organisateur peut transmettre 75 parts', async function () {
    await instance.transfererOrga(accounts[1], 75,{from: accounts[0]})
    assert.equal(await instance.estOrga(accounts[1]), true)
    assert.equal(await instance.organisateurs(accounts[0]), 25)
  })

  it('Un organisateur peut transmettre toutes ses parts', async function () {
    await instance.transfererOrga(accounts[1], 25,{from: accounts[0]})
    assert.equal(await instance.estOrga(accounts[1]), true)
    assert.equal(await instance.estOrga(accounts[0]), false)
    assert.equal(await instance.organisateurs(accounts[0]), 0)
  })

})
