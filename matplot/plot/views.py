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
    plt.savefig('image/barchart.png')
    return render(request,'barchart.html')




#from: https://projectsplaza.com/how-to-create-bar-chart-image-with-matplotlib-in-django/