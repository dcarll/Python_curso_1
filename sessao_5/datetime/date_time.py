from datetime import datetime, timedelta


# data = datetime.strptime('15/12/2021','%d/%m/%Y')
# print(data.timestamp())
# data1 = datetime.fromtimestamp(1639537200.0)
# print(data1)

d1 = datetime.strptime('17/12/2021 13:11:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('22/12/2021 15:11:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1

print(dif.seconds)
print(dif.total_seconds())
print(dif.days)
print(dif)
print(d1.time())
# data = data + timedelta(days=5, seconds=2*60*60)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))