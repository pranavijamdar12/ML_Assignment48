X = [1,2,3,4,5]
Y = [3,4,2,4,5]

m = 0.4
c = 2.4

predicated = []

for x in X:
    predicated.append(m * x + c)
print("Predicated Values:",predicated)

# MES
error_sum = 0
for i in range(len(Y)):
    error = Y[i]-predicated[i]
    error_sum = error_sum+error**2
mse = error_sum/len(Y)

# R2 Score
mean_y = sum(Y)/len(Y)

ss_total = 0
ss_residual = 0

for i in range(len(Y)):
    ss_total = ss_total +(Y[i]-mean_y)**2
    ss_residual = ss_residual + (Y[i]-predicated[i])**2

r2 = 1 - (ss_residual/ss_total)

print("MSE =",mse)
print("R2 Score =",r2)

