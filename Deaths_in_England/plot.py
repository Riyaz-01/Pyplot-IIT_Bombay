import csv
import matplotlib.pyplot as plt

# PARSING
y_deaths=[]
x_period=[]
edge_colors=['red','#4C1C24','#98704D','#4284f3']
month_abbreviations = {
    'January': 'Jan',
    'February': 'Feb',
    'March': 'Mar',
    'April': 'Apr',
    'May': 'May',
    'June': 'Jun',
    'July': 'Jul',
    'August': 'Aug',
    'September': 'Sep',
    'October': 'Oct',
    'November': 'Nov',
    'December': 'Dec'
}

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')

    counter=0
    period_sum=0
    start_month=''

    for row in reader:
        year = row['year']
        month = row['month']
        value = int(row['total'])
        counter+=1
        period_sum+=value
        if counter==1:
            start_month=month
        if counter==3:
            label=month_abbreviations.get(start_month)+'-'+month_abbreviations.get(month)+' '+year
            x_period.append(label)
            y_deaths.append(period_sum)
            counter=0
            period_sum=0


# PLOTTING 
bar_colors=['#4284f3']* (len(x_period)-3)+['red','#4C1C24','#98704D']
plt.bar(x_period,y_deaths,color=bar_colors,edgecolor=edge_colors,linewidth=2,capstyle='round', joinstyle='round')

# Add text annotations over the bars
for i, value in enumerate(y_deaths):
    plt.text(i, value +6999, str(value), ha='center',va='bottom', fontsize=8,color=bar_colors[i])

plt.title('Germany Birth-Rate Decline')
plt.ylabel('Number of Births in Germany')
plt.grid(axis='y')
plt.ylim(0,250000)
plt.gca().set_axisbelow(True)
plt.xticks(rotation=90) 
plt.box(None)
plt.legend()

plt.show()
    
