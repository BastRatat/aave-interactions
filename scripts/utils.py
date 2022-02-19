from brownie import accounts, network, config

LOCAL_ENV = ["development", "ganache-local", "mainnet-fork-dev", "mainnet-fork"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        accounts.load(id)
    if network.show_active() in LOCAL_ENV:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
