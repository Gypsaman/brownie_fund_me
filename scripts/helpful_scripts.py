from brownie import accounts,network,config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200_000_000_000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS= ["mainnet-fork-dev"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks(_account):
        
        print(f"The active network is {network.show_active()}")
        print(f"Deploying Mocks...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from":_account})
        print("Mocks Deployed!")

        