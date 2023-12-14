import matplotlib.pyplot as plt

#DATA
total=361
values=[8,9,48,21,33,242]
labels = ['Not taken','Pressured, for some other reason', 'Pressured to take, for education or work','Pressured to take, for travel',"Willingly, for others' health", 'Willingly, for own health']
colors=['#43BEC7','#FE6D01','#30A952','#FBBD00','#EB4031','#3F86F4']

custom_labels = [f'{label} ({round((size/total)*100,1)}%)' for label, size in zip(labels, values)]


plt.pie(values, labels = custom_labels, colors=colors, startangle=90,wedgeprops=dict(width=1, edgecolor='black'))
plt.show() 