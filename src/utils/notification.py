def send_notification(contracts: list):
    for i in contracts:
        print('-'*100)
        print('Customer:', i.customer)
        print('\n')
        print('phone:', i.phone_charge(), '\ninternet:', i.internet_charge(), '\nTotal:', i.total_charge())
