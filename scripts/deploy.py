from brownie import fundMe, config, network, MockV3Aggregator
from scripts.helpfull import getAccount, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def deployFundMe():
    account = getAccount()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = fundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract has been Deplyoed to {fund_me.address}")
    return fund_me


def main():
    deployFundMe()
