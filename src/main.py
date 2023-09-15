from models import *
from utils import send_notification

customer = Customer('Daniel', '335003', 'HCM')

basic = Basic(customer)
basic.call_time = 100
basic.data_used = 2250

data_fix = DataFix(customer)
data_fix.call_time = 100
data_fix.data_used = 2250

data_free = DataFree(customer, 3000, 30000)
data_free.call_time = 100
data_free.data_used = 2250

if __name__ == '__main__':
    send_notification([basic, data_fix, data_free])

