from django.shortcuts import render
import random
# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
# Pie Chart
def barchart(request):
    objects = ['morgen','eftermiddag','ferie']
    y_pos = np.arange(len(objects))
    qty = [29,46,39]
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('modul')
    plt.title('antal')
    plt.savefig('image/barchart.png', dpi=100)
    return render(request,'barchart.html')




# Pie Chart
def piechart(request):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Sale', 'Purchase'
    #labels = 'morgen','eftermiddag','ferie'
    sizes = [random.randint(10,30), random.randint(30,50)]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #explode = (29,46,39)

    fig1, ax1 = plt.subplots()
    
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('image/sale_purchase_peichart.png',dpi=100)
    return render(request,'piechart.html')




#from: https://projectsplaza.com/how-to-create-bar-chart-image-with-matplotlib-in-django/