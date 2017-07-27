import numpy
import math
import random
import matplotlib.pyplot as plt
from sklearn import mixture

# generate a gaussian
def gaussian(x, amp, cen, wid):
    return amp * math.exp(-(x - cen) ** 2 / wid)

# the height of peaks of read 1 and read 2
read1 = 12
read2 = 20

# that's our x data, i.e. reference
x = range(1, 101)

# that's our y data, i.e. reads
y = [int(round(gaussian(i, 20000, read1, 0.5) + gaussian(i, 20000, read2, 10) + random.gauss(200, 90))) for i in x]

# that's our data printed in pairs (x_i, y_i)
print([z for z in zip(x, y)])

# you have to set this manually to weed out all the noise. Every bit of noise should be below it.
threshold = 1000

# unravelling histogram into samples.
samples = []
for no, value in enumerate([int(round(i)) for i in y]):
    if value > threshold:
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

print("means")
print(means)
print("roundErr")
print(roundErr)
print("weights")
print(weights)

plt.show()
