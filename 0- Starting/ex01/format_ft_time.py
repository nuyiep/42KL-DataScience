
import datetime
from datetime import date
now = datetime.datetime.now()
# print(date.today())
print(now.strftime("%month-%d-%Y %H:%M:%S"))