import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap 
import seaborn as sns
from datetime import timedelta
color1='black'
color2='forestgreen'
color3='mediumblue'


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

# function to create a subset of columns given a dataframe
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

# function to view distribuion and outliers of numerical columns
def create_distribution_plot(num, plot_type, cap=1000):
    # define subplot configuration
    nrows, ncols = 3,1
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(50,40))
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        if i >= len(num.columns):  # avoiding empty plots
            ax.set_visible(False)
            continue
            
        # plot according to the given plot type
        column_data = num.iloc[:, i].dropna()
        ax.set_title(num.columns[i], fontsize=15)

        if plot_type == 'distribution':
            filtered_data = column_data[column_data <= cap]  # cap values at 1000
            ax.hist(filtered_data, bins=1000, color=color2, edgecolor=color1)          
        elif plot_type == 'outliers':
            ax.boxplot(
                column_data, vert=False, patch_artist=True,
                boxprops={'facecolor': color2, 'color': color1 }, 
                medianprops={'color': color2},
                whiskerprops={'color': 'black'},
                capprops={'color': 'black'},
                flierprops={'marker': 'o', 'color': color3, 'markersize': 5}
            )
            ax.tick_params(axis='x', labelsize=14)

    plt.tight_layout()
    plt.show()


# function to creat plots with double y axis
# y1 is a bar plot and y2 and y3 are line plots
def plot_dual_axis_bar_line(xticks, xtick_label, y1, y2, y3, x_label, y1_label, y2_label, title):
  
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Primary y-axis y1
    ax1.bar(y1.index, y1.values, color=color1, edgecolor='black', width=0.8, label='View', alpha=0.86)
    ax1.set_xlabel(x_label, fontsize=12)
    ax1.set_ylabel(y1_label, fontsize=12, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xtick_label, rotation=45)
    ax1.legend(loc='upper left')

    # secondary y-axis for y2 and y3
    ax2 = ax1.twinx()
    ax2.plot(y2.index, y2.values, color=color3, label='Purchase', linewidth=2)
    ax2.plot(y3.index, y3.values, color=color2, label='Cart', linewidth=2)
    ax2.set_ylabel(y2_label, fontsize=12, color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.legend(loc='upper right')

    # add title
    fig.suptitle(title, fontsize=14)
    plt.savefig(f"../images/{title.replace(' ', '_')}.png")
    plt.show()