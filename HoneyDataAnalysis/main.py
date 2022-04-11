# The data analyzed in this script can be found in the USDA Quick Stats Database (https://www.nass.usda.gov/Quick_Stats/)

import matplotlib.pyplot as plt
import pandas as pd

small_producers, medium_producers, large_producers = [], [], []
small_honey, medium_honey, large_honey = [], [], []
all_honey = []
all_states = []

medium_honey_threshold = 0
large_honey_threshold = 0

# === Clean data ===

df = pd.read_csv("HoneyDataAnalysis/honey.csv") # Return DataFrame from provided .csv file
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)

# Get list of unique states
unique_states = df['State'].unique()

# === Categorize Data ===

# Find thresholds for large and medium production categories
for state in unique_states:
  if (state == 'MISSISSIPPI'): # Mississippi data serves as threshold for medium production values
    medium_honey_threshold = df[df['State'] == state]['Value'].sum()

  elif (state == 'FLORIDA'): # Florida data serves as threshold for large production values
    large_honey_threshold = df[df['State'] == state]['Value'].sum()

# Determine if the state state falls into large, medium, or small honey production categories
for state in unique_states:
  state_sum = df[df['State'] == state]['Value'].sum()
  grouped_sum = df[df['State'] == state].groupby('Year')['Value'].sum() # Sum honey values for each state by year

  if (state_sum >= large_honey_threshold):
    large_honey.append(grouped_sum)
    large_producers.append(state)

  elif (state_sum < large_honey_threshold and state_sum >= medium_honey_threshold):
    medium_honey.append(grouped_sum)
    medium_producers.append(state)

  elif (state_sum < medium_honey_threshold):
    small_honey.append(grouped_sum)
    small_producers.append(state)
  
  all_honey.append(grouped_sum)
  all_states.append(state)

  print(state, grouped_sum) # Print sum of honey production for each state by year

honey_sums = grouped_sum
years = honey_sums.keys()
  
fig, (large_plot, med_plot, small_plot, all_plot) = plt.subplots(4) # Create 4 separate plots

"""Plot a subgroup of data. For example, plot all states with medium category honey production.

@param: state_list A list of states in the category
@param: honey_list A list of honey production values per year in the category
@param: group_plot The subplot that should be used
@param: name Title of the subplot

"""
def plot_subgroup(state_list, honey_list, group_plot, name):
  for i in range(len(state_list)): # Loop through a list of all states
    honey = honey_list[i]
    state = state_list[i]
    years = honey.keys() # Collect years from honey data
    group_plot.plot(years, honey, label=state) # Create plot of honey production vs. time
    group_plot.legend(loc=2, prop={'size': 6})

  group_plot.set_title(name)

# Plot all data
plot_subgroup(all_states, all_honey, all_plot, "All Honey Production")
plot_subgroup(small_producers, small_honey, small_plot, "Small-Scale Honey Production")
plot_subgroup(medium_producers, medium_honey, med_plot, "Medium-Scale Honey Production")
plot_subgroup(large_producers, large_honey, large_plot, "Large-Scale Honey Production")
plt.show()
