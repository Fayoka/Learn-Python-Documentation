# Without using `iter()`
for num in [1, 2, 3]:
    print(num)

# With `iter()` explicitly
numbers = [1, 2, 3]
numbers_iterator = iter(numbers)
while True:
    try:
        # Get the next item
        num = next(numbers_iterator)
        print(num)
    except StopIteration:
        # If there are no more items, break out of the loop
        break
