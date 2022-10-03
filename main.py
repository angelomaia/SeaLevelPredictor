import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    #plt.plot(np.unique(df['Year']), np.poly1d(np.polyfit(df['Year'], df['CSIRO Adjusted Sea Level'], 1))(np.unique(df['Year'])))

    # Create first line of best fit
    years = np.arange(1880, 2050, 1)
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = [slope*xi + intercept for xi in years]
    plt.plot(years, line, 'r')

    # Create second line of best fit
    years2 = np.arange(2000, 2050, 1)
    df2 = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    line2 = [slope2*xi + intercept2 for xi in years2]
    plt.plot(years2, line2, 'y')

    # Add labels and title
    plt.ylabel('Sea Level (inches)')  
    plt.xlabel('Year')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()