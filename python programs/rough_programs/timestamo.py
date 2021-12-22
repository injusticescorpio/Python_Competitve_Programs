from datetime import datetime

## date1='Sun 10 May 2015 13:54:36 -0700'
# date2='Mon 29 Dec 2064 03:33:48 -1100'
t1='Fri 11 Feb 2078 00:05:21 +0400'
t2='Sun 10 May 2015 13:54:36 -0000'
date_object1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
date_object2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
# print(f"date_object1=={date_object1}")
# print(f"date_object2=={date_object2}")
print(int(abs(date_object1-date_object2).total_seconds()))





#
# date1='2 May 2015 19:54:36 +0530'
# date2='1 May 2015 13:54:36 -0000'





