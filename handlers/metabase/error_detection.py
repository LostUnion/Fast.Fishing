import io

def search_errors(govorun_path):
    try:
        errors = [u'WARNING',
                  u'ERROR',
                  ]
        
        with io.open(f'{govorun_path}/general.log', encoding='utf-8') as general_log:
            for line in general_log:
                for error in errors:
                    if error in line:
                        print(line, end='\n')
    except:
        pass