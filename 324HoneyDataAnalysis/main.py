from cgitb import small
from tokenize import group
import matplotlib.pyplot as plt
import pandas as pd

small_producers, medium_producers, large_producers = [], [], []
small_honey, medium_honey, large_honey = [], [], []

medium_honey_threshold = 0
large_honey_threshold = 0

# Clean data
df = pd.read_csv("324HoneyDataAnalysis/honey.csv") # Return DataFrame from provided .csv file
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)

# Get list of unique states
unique_states = df['State'].unique()

for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']

  if (state == 'MISSISSIPPI'):
    medium_honey_threshold = df[df['State'] == state]['Value'].sum()

  elif (state == 'FLORIDA'):
    large_honey_threshold = df[df['State'] == state]['Value'].sum()

all_honey = []
all_states = []

for state in unique_states:
  state_sum = df[df['State'] == state]['Value'].sum()
  grouped_sum = df[df['State'] == state].groupby('Year')['Value'].sum()

  if (state_sum >= large_honey_threshold):
    large_honey.append(grouped_sum)
    large_producers.append(state)

  elif (state_sum < large_honey_threshold and state_sum >= medium_honey_threshold):
    medium_honey.append(grouped_sum)
    medium_producers.append(state)

  elif (state_sum < medium_honey_threshold):
    small_honey.append(grouped_sum)
    small_producers.append(state)

  honey_data = df[df['State'] == state].groupby('Year')['Value'] # Create array of honey values by year for current state
  # print (state, honey_data.sum()) # Display honey values by year for current state.
  all_honey.append(grouped_sum)
  all_states.append(state)

  print(state, state_sum)

honey_sums = grouped_sum
years = honey_sums.keys()

# Without grouping
# for state in unique_states:
#   honey_data = df[df['State'] == state]['Value'] # Create array of honey values for current state
#   print (state, honey_data.sum()) # Display sum of honey values for current state
#   all_honey.append(honey_data.sum())
#   all_states.append(state)
  
fig, (large_plot, med_plot, small_plot, all_plot) = plt.subplots(4)
# fig, all_prod = plt.subplots()

# With grouping
# for state in unique_states:
#   honey_data = df[df['State'] == state].groupby('Year')['Value'] # Create array of honey values by year for current state
#   # print (state, honey_data.sum()) # Display honey values by year for current state.
#   all_honey.append(honey_data.sum())
#   all_states.append(state)

def plot_subgroup(state_list, honey_list, group_plot, name):
  for i in range(len(state_list)): # Loop through a list of all states
    honey = honey_list[i]
    state = state_list[i]
    years = honey.keys() # Collect years from honey data
    group_plot.plot(years, honey, label=state) # Create plot of honey production vs. time

  group_plot.set_title(name)

plot_subgroup(all_states, all_honey, all_plot, "All Honey Production")
plot_subgroup(small_producers, small_honey, small_plot, "Small-Scale Honey Production")
plot_subgroup(medium_producers, medium_honey, med_plot, "Medium-Scale Honey Production")
plot_subgroup(large_producers, large_honey, large_plot, "Large-Scale Honey Production")

# Large threshold = sum of florida
# med threshold = Mississippi

# Create plot labels and legend
# all_prod.set_ylabel('Honey Production')
# all_prod.set_xlabel('Year')
# all_prod.set_title('Honey Production by State')
# all_prod.legend()
plt.show()

# # a322_electricity_trends.py
# # This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# # Then it will use the matplotlib module to plot comparative line graphs 

# import matplotlib.pyplot as plt
# import pandas as pd

# # choose countries of interest
# my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]

# # Load in the data with read_csv()
# df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# # get a list unique countries
# unique_countries = df['Entity'].unique()

# # Plot the data on a line graph
# for c in unique_countries:
#   if c in my_countries:
    
#     # match country to one of our we want to look at and get a list of years
#     years = df[df['Entity'] == c]['Year']

#     # match country to one of our we want to look at and get a list of electriciy values
#     sum_elec = df[df['Entity'] == c]['Access']

#     plt.plot(years, sum_elec, label=c)

  
# plt.ylabel('Percentage of Country Population')
# plt.xlabel('Year')
# plt.title('Percent of Population with Access to Electricity')
# plt.legend()
# plt.show()
