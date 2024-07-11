# from datetime import datetime
#
# h , m = input().split(":")
# h , m = int(h) , int(m)
# now = datetime.now()
# hour = now.hour
# minut = now.minute
# print(hour , minut)
# if hour > h:
#     if minut >= m:
#         print(f"{hour-h}:{minut-m}")
#     else:
#         print(f"{(hour-1)-h}:{(minut+60)-m}")
# elif hour == h:
#     if minut >= m:
#         print(f"{hour - h}:{minut - m}")
#     else:
#         print(f"{(23+hour)-h}:{(60+minut)-m}")
# else:
#     if minut >= m:
#         print(f"{(24+hour)-h}:{minut-m}")
#     else:
#         print(f"{(23+hour)-h}:{(60+minut)-m}")
#

# from datetime import datetime
# h , m = input().split(":")
# h , m = int(h) , int(m)
# now = datetime.now()
# hour = now.hour
# minut = now.minute
# S = (hour*60 + minut) - (h*60 + m)
# if S >= 0:
#     print(f"{S//60}:{S%60}")
# else:
#     S = S + 24*60
#     print(f"{S//60}:{S%60}")

# from time import time
#
# print(time())

# from datetime import  timezone
#
# print(timezone.utc)

import time

t = time.strftime("%I:%M:%p")

print(t)