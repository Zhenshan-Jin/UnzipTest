
import tempfile
import pathlib
import zipfile
import os

root_folder = tempfile.gettempdir()

def unzip_model(zip_model_path):
    p = pathlib.Path(zip_model_path)
    # root = str(p.parents[0])
    print(f'start unzip: {root_folder}')
    model_path = os.path.join(root_folder, os.path.splitext(os.path.basename(zip_model_path))[0] + '/')
    if not os.isdir(model_path):
        os.path.mkdir(model_path)
        with zipfile.ZipFile(zip_model_path, "r") as zip_ref:
            zip_ref.extractall(model_path)
        
    print(f"finish zipping model to {model_path}")
    return model_path

zip_file_path = "/pebble_tmp/tmp/test.zip"

def compute(i):
    model_path = unzip_model(zip_file_path)
    print(root_folder)
    return model_path


    