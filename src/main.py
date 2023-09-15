from models.customer import Customer
from models.contract.basic import Basic
from models.contract.data_fix import DataFix
from models.contract.data_free import DataFree
from utils.notification import send_notification

c = Customer('Daniel', '335003', 'HCM')

b = Basic(c)
b.set_call_time(100)
b.set_data_used(2250)

d_fix = DataFix(c)
d_fix.set_call_time(100)
d_fix.set_data_used(2250)

d_free = DataFree(c, 3000, 30000)
d_free.set_call_time(100)
d_free.set_data_used(2250)


send_notification([b, d_fix, d_free])

