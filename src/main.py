from models.customer import Customer
from models.contract.basic import Basic
from models.contract.data_fix import DataFix
from models.contract.data_free import DataFree
from utils.notification import send_notification

customer = Customer('Daniel', '335003', 'HCM')

basic = Basic(customer)
basic.set_call_time(100)
basic.set_data_used(2250)

data_fix = DataFix(customer)
data_fix.set_call_time(100)
data_fix.set_data_used(2250)

data_free = DataFree(customer, 3000, 30000)
data_free.set_call_time(100)
data_free.set_data_used(2250)


send_notification([basic, data_fix, data_free])

