import datetime

print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '19", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))