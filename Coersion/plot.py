# this pie chart represents the different reasons for students to take the covid vaccine and their percentages
# this chart is present on slide number 3 of the given pdf

import matplotlib.pyplot as plt
import numpy as np

#DATA
total=361
values=[8,9,48,21,33,242]
labels = ['Not taken','Pressured, for some other reason', 'Pressured to take, for education or work','Pressured to take, for travel',"Willingly, for others' health", 'Willingly, for own health']
colors=['#43BEC7','#FE6D01','#30A952','#FBBD00','#EB4031','#3F86F4']

custom_labels = [f'{label} ({round((size/total)*100,1)}%)' for label, size in zip(labels, values)]

# PLOTTING
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts = ax.pie(values, colors=colors, startangle=90,wedgeprops=dict(width=1, edgecolor='black'))
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)

kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), (1.3 if i>0 else 1.5)*y),
                horizontalalignment=horizontalalignment, **kw)
    
plt.title("Quantification of COVID-19 Vaccine Coercion in India: A Survey Study",y=1.2)
plt.show() 