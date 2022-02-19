from scripts.utils import get_account
from brownie import interface, config, network
from web3 import Web3

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": Web3.toWei(0.1, 'ether')})
    tx.wait(1)
    print("Received 0.1 WETH")

def main():
  get_weth()
