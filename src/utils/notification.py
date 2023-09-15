def send_notification(contracts: list):
    for i in contracts:
        print('-'*100)
        print('Customer:', i.customer)
        print('\n')
        print('Plan:', i)
        print('phone:', f'{i.phone_charge():,}', '\ninternet:', f'{i.internet_charge():,}', '\nTotal:', f'{i.total_charge():,}')
