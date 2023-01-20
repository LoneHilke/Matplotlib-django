from django.shortcuts import render
import random
# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
# Pie Chart
def barchart(request):
    objects = ['12/10/2019','12/11/2020','15/10/2020']
    y_pos = np.arange(len(objects))
    qty = [10,20,25]
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Quantity')
    plt.title('Sales')
    plt.savefig('media/barchart.png')
    return render(request,'barchart.html')




#from: https://projectsplaza.com/how-to-create-bar-chart-image-with-matplotlib-in-django/