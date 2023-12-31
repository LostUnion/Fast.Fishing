import os

def floders_add(call_id):
    path_0 = 'Data/'
    if not os.path.exists(path_0):
        os.mkdir(path_0)
    else:
        pass
    
    path_1 = f'Data/{call_id}/'
    if not os.path.exists(path_1):
        os.mkdir(path_1)
    else:
        pass
    
    path_to_log = f'Data/{call_id}/Metabase/'
    if not os.path.exists(path_to_log):
        os.mkdir(path_to_log)
    else:
        pass
    return path_1, path_to_log

def govorun_floder_add(call_id):
    path_to_govorun = f'Data/{call_id}/Metabase/govorun'
    if not os.path.exists(path_to_govorun):
        os.mkdir(path_to_govorun)
    else:
        pass
    return path_to_govorun