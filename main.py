
import tempfile
import pathlib
import zipfile
import os

# root_folder = tempfile.gettempdir()
root_folder = "/tmp"

def unzip_model(zip_model_path):
    p = pathlib.Path(zip_model_path)
    # root = str(p.parents[0])
    print(f'start unzip: {root_folder}')
    model_path = os.path.join(root_folder, os.path.splitext(os.path.basename(zip_model_path))[0] + '/')
    print(os.listdir("/tmp"))
    if not os.path.isdir(model_path):
        print("no directory")
        print(f'create: {model_path}')
        os.mkdir(model_path)
        print(f"unzip from {zip_model_path} to {model_path}")
        with zipfile.ZipFile(zip_model_path, "r") as zip_ref:
            zip_ref.extractall(model_path)
    else:
        print("has directory")
    print(f"finish zipping model to {model_path}")
    return model_path

zip_file_path = "/pebble_tmp/tmp/test.zip"

def compute(i):
    model_path = unzip_model(zip_file_path)
    print(root_folder)
    return model_path


    