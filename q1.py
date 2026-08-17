# Q1
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

# Calculate slop 
mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)

# Calculate slop
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator = numerator + (X[i]-mean_x)*(Y[i]-mean_y)

    denominator = denominator +(X[i]-mean_x)**2

m = numerator/denominator

# Calculate intercept
c = mean_y - (m*mean_x)

print("Mean of X =",mean_x)
print("Mean of Y =",mean_y)
print("Slop(m) =",m)
print("Intercept(c)=",c)
print("Regression Equation:")
print("Y =",m,"X +",c)

x = 6
predicted_y = m * x + c

print("Predicted Y for X = 6:",predicted_y)

