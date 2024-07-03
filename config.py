#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - прокси без ссылки , 2 - прокси со ссылкой для смены ip
proxy_login = 'pludg74'
proxy_password = 'a2d0'
proxy_address = 'noxy.com'
proxy_port = '199'
proxy_changeIPlink = "h04"



#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 20 #минимальная 
timeoutMax = 70 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 10 #минимальная 
timeoutTehMax = 20 #максимальная



#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}
gas_kef=1.9 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.3 до 2
gas_price_kef=1.8 


conf = {'rpc': 'https://rpc.linea.build','type':2,'scan':'https://lineascan.build/tx/'}

conf.update({'eth': 'https://rpc.ankr.com/eth'})


