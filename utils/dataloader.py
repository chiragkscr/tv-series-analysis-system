from transformers import pipeline
from nltk import sent_tokenize
import nltk
import torch
from glob import glob
import pandas as pd
import numpy as np


def load_subtitles_dataset(dataset_path):
    subtitles_paths = glob(dataset_path+'/*.ass')
    scripts = []
    episode_num= []
    
    for path in subtitles_paths:
        #Read lines
        with open(path, 'r') as file:
            lines = file.readlines()
            lines = lines[27:]
            lines = [",".join(line.split(',')[9:]) for line in lines]
        lines= [line.replace('\\N', ' ')for line in lines]
        script = " ".join(lines)

        episdoe = int(path.split('-')[-1].split('.')[0].strip())

        scripts.append(script)
        episode_num.append(episdoe)
    
    df = pd.DataFrame.from_dict({"episode":episode_num, "Scripts": scripts})
    return df

