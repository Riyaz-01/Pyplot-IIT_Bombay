import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# PARSING
data_by_year = defaultdict(list)
def cummulative_sum(arr):
    result_sequence = []
    current_sum = 0

    for number in arr:
        current_sum += number
        result_sequence.append(current_sum)

    return result_sequence

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
  
    for row in reader:
        year = int(row['year'])
        week = int(row['week'])
        value = int(row['value'])
        data_by_year[year].append((week, value))

for year, data in data_by_year.items():
    data_by_year[year] = sorted(data, key=lambda x: x[0])
      

#PLOTTING
for year,data in data_by_year.items():
    x=[item[0] for item in data]
    y=[item[1] for item in data]
    y=cummulative_sum(y)
    plt.plot(x,y,label=year)

plt.plot(range(55),[0]*55,label='Baseline',linestyle='--',color='grey')

plt.xlabel('Week number')
plt.ylabel('Excess deaths')
plt.legend()
plt.grid(axis='y')
plt.box(None)
plt.legend(loc='upper left', ncols=4)
plt.title('Excess deaths in Europe')

plt.show()