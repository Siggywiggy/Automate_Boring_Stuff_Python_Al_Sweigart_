import datetime

october_21st = datetime.datetime(2024, 10, 21, 16, 29, 0)

print(october_21st.strftime('%Y/%m/%d %H:%M:%S'))
print(october_21st.strftime(('%I:%M %p')))
print(october_21st.strftime(("%B of '%y")))