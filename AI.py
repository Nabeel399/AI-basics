pizzasize = {'sdiam': 8, 'mdiam': 12, 'ldiam': 16}  # X
pizzaprice = {'sprice': 10, 'mprice': 15, 'lprice': 20}  # Y

# Calculate means
meanX = sum(pizzasize.values()) / len(pizzasize)
meanY = sum(pizzaprice.values()) / len(pizzaprice)

# Calculate deviations
deviX = [diam - meanX for diam in pizzasize.values()]
deviY = [price - meanY for price in pizzaprice.values()]

# Calculate product of deviations
productD = sum(deviX[i] * deviY[i] for i in range(len(deviX)))

# Calculate squares of deviations
deviXsq = sum(devi ** 2 for devi in deviX)

# Calculate slope (m) and y-intercept (b)
m = productD / deviXsq
b = meanY - (m * meanX)

print("Slope (m):", m)
print("Y-intercept (b):", b)

# Now, you can predict the price for a given pizza size (diameter)
given_diameter = input("Enter Your New pizza size in inches to know its price: ")  # Example diameter for prediction
predicted_price = m * float(given_diameter) + b
print("Predicted price for diameter {}: {}".format(given_diameter, round(predicted_price)))