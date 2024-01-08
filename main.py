import os
import argparse
from handlers.database.database import db_start
from handlers.metabase.authentication import auth
from handlers.metabase.collection_by_call import collect_information
from handlers.metabase.creating_folders import floders_add
from handlers.metabase.convert_csv_to_xlsx import csv_to_xlsx
from handlers.metabase.download_log import govorun_download
from handlers.metabase.error_detection import search_errors
from handlers.metabase.formatting_the_data import format_data
from handlers.sip3_data.checking_the_date import check_date
from handlers.sip3_data.get_sip_data import sip
from handlers.loger.authorization import get_info

if __name__ == "__main__":
    os.system('cls')
    parser = argparse.ArgumentParser(description='Receiving call data')
    parser.add_argument('-c', '--call', type=str, help='Call ID')
    
    args = parser.parse_args()
    db_start()

    print('''__________                _____     _______________         ______  _____                  
___  ____/______ ___________  /_    ___  ____/___(_)___________  /_ ___(_)_______ _______ _
__  /_    _  __ `/__  ___/_  __/    __  /_    __  / __  ___/__  __ \__  / __  __ \__  __ `/
_  __/    / /_/ / _(__  ) / /_  ___ _  __/    _  /  _(__  ) _  / / /_  /  _  / / /_  /_/ / 
/_/       \__,_/  /____/  \__/  _(_)/_/       /_/   /____/  /_/ /_/ /_/   /_/ /_/ _\__, /  
                                                                                  /____/   ''')
    
    #Metabase
    auth()
    data_json, call_id = collect_information(args.call)
    path, path_to_log = floders_add(call_id)
    file_name, path, path_to_log, Started_At_Updates, Finished_At_Updates = format_data(path, path_to_log, data_json, call_id)
    print(f'[metabase] Call status {data_json[20]}')
    csv_to_xlsx(file_name, path, data_json[0])
    govorun_path = govorun_download(data_json[1], path, call_id)
    search_errors(govorun_path)
    
    #SIP3
    sip(data_json[5], path)

    #LOGS
    get_info(call_id, Started_At_Updates, Finished_At_Updates, path)
    
    