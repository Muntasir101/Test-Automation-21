from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)
formatted_date = current_date.strftime('%Y-%m-%d')
print(formatted_date)

future_date = current_date + timedelta(days=3)
print(future_date)
formated_future_date = future_date.strftime('%Y-%m-%d')
print(formated_future_date)

