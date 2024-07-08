import pandas as pd
from .embeddings_compression import final_vector
import os

def vector_query(path):
    print(os.getcwd())
    df = pd.read_csv("../dataset/statistics.csv")
    vector = [a.item() for a in final_vector(path)]
    target_means, target_stds = [], []
    
    for col in df.columns:
        target_means.append(df[col][1])
        target_stds.append(df[col][2])
    
    scaled_vector = []
    
    for val,target_mean,target_std in zip(vector, target_means, target_stds):
        scaled_vector.append((val*target_std)+target_mean)

    return scaled_vector

