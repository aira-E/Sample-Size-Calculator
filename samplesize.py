# Sample Size Calculator
confidence_level = int (input ("Confidence Level (in percentage form): "))
precision = float (input ("Precision (in decimal form): "))
if confidence_level == 90:
    z_value = 1.645
elif confidence_level == 95:
    z_value = 1.96
elif confidence_level == 99:
    z_value = 2.576
m = 0.05
sample_size = ( z_value * z_value ) * precision * ( 1 - precision ) / (m * m)
print (f"sample size: {sample_size}")
