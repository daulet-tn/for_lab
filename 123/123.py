# fdsFdfSd - fds_fdf_sd
# 3+-today
# 2, 8
import re
from datetime import datetime, timedelta 
x = input()
s = re.findall(r'_[a-z]', x) 
z =  len(s) + 1
a = datetime.now()
print(a - timedelta(days= z))
print(a + timedelta(days= z ))