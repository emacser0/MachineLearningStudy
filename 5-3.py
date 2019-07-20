import math
import functools
import numpy
X = numpy.matrix("1 1; 2 3; 3 3")
XT = X.T
I = numpy.eye(2)
y = numpy.matrix("3.0; 7.0; 8.8")
lambda_value = 0.25
print("Lambda Value = 0.25")
print(((XT * X) + 2 * lambda_value * I).I @ XT @ y)
lambda_value = 0.1
print("Lambda Value = 0.1")
print(((XT * X) + 2 * lambda_value * I).I @ XT @ y)
lambda_value = 0.5
print("Lambda Value = 0.5")
print(((XT * X) + 2 * lambda_value * I).I @ XT @ y)
