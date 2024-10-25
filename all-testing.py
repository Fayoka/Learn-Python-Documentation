def testing():
    myList = [1, 2]
    # Using all() to check if all items are truthy (non-zero)
    return all(bool(listItem) for listItem in myList)

# Print the result of testing()
print(testing())  # This will print True if all elements are non-zero
