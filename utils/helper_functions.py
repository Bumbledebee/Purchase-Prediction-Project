import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap 
import seaborn as sns
import plotly.graph_objs as go
color1='#4a86e8'
color2='#ffd966'
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', [color1,color2])
custom_cmap2 =  [color1,color2]


# checks for dupplicates, NaN & empty spaces
# and returns the number of duplicates, NaN & empty spaces
def check_data(data):
    duplications = data.duplicated().sum()
    nan_values = data.isna().sum()
    empty_spaces = data.eq(' ').sum()
    print(f"There are {duplications} duplicate rows, {nan_values.values.sum()} empty values and {empty_spaces.values.sum()} empty spaces")
    if duplications > 0:
        print()
        print("Duplicate Rows:")
        perc = str(round(duplications / len(data) * 100, 2))
        print(f"{perc}% of duplicated rows. View some of them below:")
        print(data[data.duplicated(keep=False)].sample(3))
    if nan_values.values.sum() > 0:
        print()
        print("NaN Rows:")
        for x in nan_values[nan_values > 0].index:
            perc = str(round(data[x].isna().sum() / len(data) * 100, 2))
            print(f"{perc}% of NaNs in the {x} column")
    if empty_spaces.values.sum() > 0:
        print()
        print("Empty Rows:")
        for x in empty_spaces[empty_spaces > 0].index:
            perc = str(round(data[x].eq(' ').sum() / len(data) * 100, 2))
            print(f"{perc}% of empty space in the {x} column")

# given a dataframe a function to create a subset of columns
def create_subset(data, columns):
    subset = data[columns]
    return subset

# create num and cat dataframes with threshold
# num, cat = separate_numerical_categorical(df, 18)
def separate_numerical_categorical(df, threshold=18):
    cat = df.select_dtypes(include="object")
    num = df.select_dtypes(include="number") 
    cat_num = num.loc[:, num.nunique() < threshold]  
    num = num.drop(columns=cat_num.columns)  
    cat = pd.concat([cat, cat_num], axis=1)  
    return num, cat

# Function to view distribuion and outliers of numerical columns
def create_distribution_plot(num,type):
    if type == 'distribution':
        nrows, ncols = 5,4 # how many subplots per row and column

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 12))

        axes = axes.flatten() #it converts the array from a shape of 2D (nrows, ncols) to a shape of 1D(nrows*ncols,)


        for i, ax in enumerate(axes): #i is getting the index, ax the axis object
            if i >= len(num.columns):  # avoids showing empty plots 
                ax.set_visible(False) 
                continue                
            ax.hist(num.iloc[:, i], bins=40, color=color2, edgecolor='black')
            ax.set_title(num.columns[i], fontsize=15)

        plt.tight_layout()
        plt.show()

    elif type == 'outliers':
        nrows, ncols = 5, 4
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 12))
        axes = axes.flatten()

        for i, ax in enumerate(axes):
            if i >= len(num.columns):
                ax.set_visible(False)
                continue
            ax.boxplot(
                num.iloc[:, i].dropna(), vert=False, patch_artist=True,
                boxprops={'facecolor': color1, 'color': 'black'},  # Correct usage here
                medianprops={'color': 'yellow'},
                whiskerprops={'color': 'black'},
                capprops={'color': 'black'},
                flierprops={'marker': 'o', 'color': 'red', 'markersize': 5}
            )
            ax.set_title(num.columns[i], fontsize=14)
            ax.tick_params(axis='x', labelsize=14)

        plt.tight_layout()
        plt.show()