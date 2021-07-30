'''Use you own infura PROJECT ID where it says PROJECT_ID in the url'''

from pprint import pprint
import pandas as pd
from web3 import Web3
import json
import time
from web3.auto import w3


infura_url = 'https://mainnet.infura.io/v3/PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))
is_connected = web3.isConnected()
def ethereum():
    while is_connected:
        latest_block_number = web3.eth.block_number
        # latest_block_details = web3.eth.get_block('latest')
        num = latest_block_number
        list_of_blocks = []
        tx_count_list = []

        for _ in range(3):
            block = web3.eth.get_block(num)
            tx_count = str(len(block['transactions']))
            list_of_blocks.append(block)
            tx_count_list.append(tx_count)

            num -= 1

        pending_block = web3.eth.getBlock(block_identifier='pending', full_transactions=True)
        pending_transactions = pending_block['transactions']
        df_pending_transactions = pd.DataFrame(pending_transactions, columns=['blockNumber', 'from', 'gas',
                                                                              'gasPrice', 'nonce', 'to',
                                                                              'transactionIndex', 'type', 'v', 'value'])


        df_list_of_blocks = pd.DataFrame(list_of_blocks, columns=['difficulty','gasLimit','gasUsed','hash','miner','nonce',
                                                                  'size','timestamp'])
        df_list_of_blocks.insert(8, 'transactions', tx_count_list, True)
        three_blocks_dataframe = df_list_of_blocks
        return df_list_of_blocks, df_pending_transactions
