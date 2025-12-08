nums = [1, 2, 3, 4, 5, 6, 7, 8]

# for even number normal loop
even = []
for x in nums:
    if x % 2 == 0:
        even.append(x)

        # OR

evens = [x for x in nums if x % 2 == 0]

# for squared numbers
squared = []
for x in nums:
    squared.append(x * x)

    # OR

squareds = [x * x for x in nums]

# for x greater than 4
greater_than_four = []
for x in nums:
    if x > 4:
        greater_than_four.append(x)

        # OR

greater_than_fours = [x for x in nums if x > 4]


print(even)
print(evens)
print(squared)
print(squareds)
print(greater_than_four)
print(greater_than_fours)
