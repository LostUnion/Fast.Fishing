import wget
import tarfile
from src.metabase.creating_folders import govorun_floder_add

def govorun_download(Link_to_Log, path, call_id):
    try:
        download_file = wget.download(str(Link_to_Log), path)
        print("\n[metabase] Govorun log has been downloaded\n")
        file_name = download_file
        zipfile_path = f'{file_name}'
        path_to_govorun = govorun_floder_add(call_id)

        if zipfile_path.endswith("tar.gz"):
            tar = tarfile.open(zipfile_path, "r:gz")
        elif zipfile_path.endswith("tar"):
            tar = tarfile.open(zipfile_path, "r:")

        tar.extractall(f'{path_to_govorun}')
        tar.close()
        return path_to_govorun
    except:
        print("[metabase] The govorun log has not been downloaded\n")