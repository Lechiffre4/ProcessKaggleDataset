import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read the data
df = pd.read_csv('data.csv')
average = df["energy"].mean()
print(average)
