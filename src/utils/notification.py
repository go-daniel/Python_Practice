def send_notification(contracts: list):
    for i in contracts:
        print('-'*100)
        print('Customer:', i.get_customer())
        print('\n')
        print('phone:', i.phone_charge(), '\ninternet:', i.internet_charge(), '\nTotal:', i.totalCharge())
