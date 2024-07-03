import decimal
from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
from config import conf
import fun
from fun import *




current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

random.shuffle(keys_list)
i=0
for private_key in keys_list:
    string_list = private_key.split("	")
    private_key = string_list[0]
    wallet_out = string_list[1] if len(string_list) > 1 else ""
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    try:
        web3 = Web3(Web3.HTTPProvider(conf['rpc'], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address    
        balance = web3.eth.get_balance(wallet)
        balance_decimal = float(Web3.from_wei(balance, 'ether'))
    except Exception as error:
        log_error(f'Ошибка подключения в ноде: {error}')   

    log(f"I-{i}: Начинаю работу с {wallet}")



    to = web3.to_checksum_address("0xB8DD4f5Aa8AD3fEADc50F9d670644c02a07c9374")
    amount = web3.to_wei("0.0001", 'ether')
    # value = int(amount)
    value = 0
    data = "0xa22cb465000000000000000000000000b8dd4f5aa8ad3feadc50f9d670644c02a07c93740000000000000000000000000000000000000000000000000000000000000001"

    try:
        gasPrice = web3.eth.gas_price

        transaction = {
            "chainId": web3.eth.chain_id,
            'from': wallet,
            'to': to,
            'value':value,
            'gasPrice': gasPrice,
            'nonce': web3.eth.get_transaction_count(wallet),
            'data': data
        }
        gasLimit = int(web3.eth.estimate_gas(transaction))
        transaction['gas'] = gasLimit
        if conf['type']:
            maxPriorityFeePerGas = int(web3.eth.max_priority_fee * config.gas_price_kef)
            fee_history = web3.eth.fee_history(10, 'latest', [10, 90])
            baseFee=round(mean(fee_history['baseFeePerGas']))
            maxFeePerGas = maxPriorityFeePerGas + round(baseFee * config.gas_price_kef)

            del transaction['gasPrice']
            transaction['maxFeePerGas'] = maxFeePerGas
            transaction['maxPriorityFeePerGas'] = maxPriorityFeePerGas



        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_txn.rawTransaction))
        tx_result = web3.eth.wait_for_transaction_receipt(txn_hash)

        if tx_result['status'] == 1:
            log_ok(f'send OK: {conf["scan"]}{txn_hash}')
        else:
            log_error(f'send false: {conf["scan"]}{txn_hash}')
        


    except Exception as error:
        fun.log_error(f'send false: {error}')
        save_wallet_to("send_false_pk", private_key)
        # keys_list.append(private_key)



    timeOut()
    

    
log("Ну типа все, кошельки закончились!")