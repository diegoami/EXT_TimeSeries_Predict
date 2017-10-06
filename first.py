root_dir = '/media/diego/QData/datasets/passengers/'

import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv(root_dir+'international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()