import datetime

def random_date(start_date, num_days):
    date_1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")

    return date_1 + datetime.timedelta(days=num_days) 
