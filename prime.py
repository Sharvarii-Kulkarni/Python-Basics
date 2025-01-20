# Define the range
start = 20
end = 50

# Initialize lists to store prime and non-prime numbers
prime_numbers = []
non_prime_numbers = []

# Loop through numbers in the range
for number in range(start, end + 1):
    if number < 2:  # Numbers less than 2 are not prime
        non_prime_numbers.append(number)
        continue

    # Assume the number is prime
    is_prime = True
    for i in range(2, number):
        if number % i == 0:  # If divisible by any number other than 1 and itself
            is_prime = False
            break

    # Append the number to the appropriate list
    if is_prime:
        prime_numbers.append(number)
    else:
        non_prime_numbers.append(number)

# Print the results
print("Prime numbers:", prime_numbers)
print("Non-prime numbers:", non_prime_numbers)
