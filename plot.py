from __future__ import print_function
import numpy
import math
import random
import csv
#import matplotlib.pyplot as plt
from sklearn import mixture

import csv

x = []
y = []

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for i, row in enumerate(spamreader):
        if i != 0:
            x.append(int(row[0].split("_")[-1]))
            y.append(int(row[2]))

# you have to set this manually to weed out all the noise. Every bit of noise should be below it.
threshold = 0
rightLimit = 200

# unravelling histogram into samples.
samples = []
for no, value in enumerate([int(round(i)) for i in y]):
    if value > threshold and no < rightLimit:
        for _ in range(value):
            samples.append(no)

# total number of reads
totalAmp = len(samples)

# reshaping numpy arrays to indicate that we pass a lot of samples, not a lot of features.
xArray = numpy.array(x).reshape(1, -1)
samplesArray = numpy.array(samples).reshape(-1, 1)

# learning a gaussian mixture model.
gmm2 = mixture.BayesianGaussianMixture(n_components=2).fit(samplesArray)

# getting the mean of each gaussian
means = [x[int(round(i[0]))] for i in gmm2.means_]

# rounding errors
roundErr = [i[0] - int(round(i[0])) for i in gmm2.means_]

# getting the coverage of each gaussian
weights = gmm2.weights_

plt.bar(x, y)

plt.show()

#plt.savefig("adams_tool.png")

with open("adam_tool_data", "w") as f:
    print(means, file=f)
    print("roundErr", file=f)
    print(roundErr, file=f)
    print("weights", file=f)
    print(weights, file=f)
