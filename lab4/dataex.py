#1
from datetime import datetime, timedelta 
now = datetime.now() # take time at the moment
fiveday= now - timedelta(days=5)
print(fiveday.strftime("%Y-%m-%d")) 
#2
print(now.strftime("%Y-%m-%d")) #print time like 2020-12-10
#3
yesterday = now - timedelta(days = 1)
print(yesterday.strftime("%Y-%m-%d"))
#4
tomorrow= now + timedelta(days = 1)
print(tomorrow.strftime("%Y-%m-%d"))
#5
nosec = now.replace(microsecond=0)
print(nosec)
#6
date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 18, 14, 30, 0)
difference = (date2 - date1).total_seconds()
print(difference)
