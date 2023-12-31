import time
from datetime import datetime

def time_now(f_time):
    time_today_data = datetime.strptime(datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
    time_today_unix = str(time.mktime(time_today_data.timetuple()))[:-2]
    
    time_created_date = datetime.strptime(f_time, "%Y/%m/%d %H:%M:%S")
    time_created_unix = str(time.mktime(time_created_date.timetuple()))[:-2]
    
    return int(time_today_unix) - int(time_created_unix)

def check_date(date):
    try:
        parsed_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        f_time = parsed_time.strftime("%Y/%m/%d %H:%M:%S")
    except:
        parsed_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        f_time = parsed_time.strftime("%Y/%m/%d %H:%M:%S")
        
    time_calculating = time_now(f_time)
    return time_calculating
    
    
