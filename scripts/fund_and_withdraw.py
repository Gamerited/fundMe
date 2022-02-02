from brownie import fundMe, config, network, MockV3Aggregator
from scripts.helpfull import getAccount


def fund():
    fund_me = fundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = fundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
