import nltk
from nltk.corpus import wordnet as wn
import tempfile

root_folder = tempfile.gettempdir()
nltk.download('wordnet', download_dir=root_folder) # download the package to specific directory
nltk.data.path.append(root_folder) # add the directory to the nltk data loading path
nltk.download('omw-1.4', download_dir=root_folder) # download the package to specific directory

def compute(test):
    return {"result": [i.name() for i in wn.synsets("same")]}

    