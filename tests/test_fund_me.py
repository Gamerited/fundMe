import imp
from scripts.helpfull import getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deployFundMe
from brownie import network, accounts, exceptions
import pytest


def test_can_fundAndWithdraw():
    account = getAccount()
    fund_me = deployFundMe()
    entrace_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrace_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrace_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_onlyOwnerCanWithdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    # account = getAccount()
    fund_me = deployFundMe()
    badActor = accounts.add()
    # fund_me.withdraw({"from": badActor})
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": badActor})
