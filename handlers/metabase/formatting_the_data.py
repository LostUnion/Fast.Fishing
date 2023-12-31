import csv
from datetime import datetime

def formatted_time(original_time):
    try:
        parsed_time = datetime.strptime(original_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        return parsed_time.strftime("%Y/%m/%d %H:%M")
        
    except:
        parsed_time = datetime.strptime(original_time, "%Y-%m-%dT%H:%M:%SZ")
        return parsed_time.strftime("%Y/%m/%d %H:%M")

def format_data(path, path_to_log, data_json):
    
    times = [data_json[15], data_json[16], data_json[17], data_json[18], data_json[19], data_json[24]]
    
    index = 0
    for timestamp in times:
        if timestamp is not None:
            times[index] = formatted_time(timestamp)
        else:
            times[index] = None
        index += 1
        
    Created_At_Updates = times[0]
    Updated_At_Updates = times[1]
    Started_At_Updates = times[2]
    Finished_At_Updates = times[3]
    Billed_At_Updates = times[4]
    Speaker_Finished_At_Updates = times[5]
    
    header_names = [
        ['ID', data_json[0]], 
        ['Link to Log', data_json[1]],
        ['Bot ID', data_json[2]],
        ['Dialog ID', data_json[3]],
        ['Company ID', data_json[4]],
        ['External ID', data_json[5]],
        ['Number', data_json[6]],
        ['Caller ID', data_json[7]],
        ['Timezone', data_json[8]],
        ['Variables', data_json[9]],
        ['Duration', data_json[10]],
        ['Previous Bot lds', data_json[11]],
        ['Is Redirected', data_json[12]],
        ['Total Cost ($)', data_json[13]],
        ['Reseller Total Cost ($)', data_json[14]],
        ['Created At', Created_At_Updates],
        ['Updated At', Updated_At_Updates],
        ['Started At', Started_At_Updates],
        ['Finished At', Finished_At_Updates],
        ['Billed At', Billed_At_Updates],
        ['Status', data_json[20]],
        ['Speaker Finished At', Speaker_Finished_At_Updates],
        ['Record Path', data_json[25]],
        ['Parts Agg', data_json[26]],
        ['Hung Up By Bot', data_json[27]],
        ['Is Incoming', data_json[28]],
        ['Region ID', data_json[29]],
        ['Auto Call Candidate ID', data_json[30]],
        ['Is Call Efficiency', data_json[31]],
        ['Auto Call ID', data_json[32]],
        ['Current Bot Settings ID', data_json[33]],
        ['Bot Settings ID History', data_json[34]],
        ['Client External ID', data_json[35]],
        ['Log Path', data_json[36]],
    ]
    
    ready_mate = [
        ['ID', data_json[0]], 
        ['Link to Log', data_json[1]],
        ['Bot ID', data_json[2]],
        ['Dialog ID', data_json[3]],
        ['Company ID', data_json[4]],
        ['External ID', data_json[5]],
        ['Number', data_json[6]],
        ['Caller ID', data_json[7]],
        ['Timezone', data_json[8]]
    ]
    
    file_name = f'{path_to_log}/{data_json[0]}.csv'
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in header_names:
            writer.writerow(row)
            
    ready_mate_data = f'{path}/ready_mate_data.csv'
    with open(ready_mate_data, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in ready_mate:
            writer.writerow(row)
    
    return ready_mate_data, path, path_to_log, Started_At_Updates, Finished_At_Updates