def filter_numbers(items):
    new_items = []
    for x in range(len(items)):
        if isinstance(items[x], int) == True and isinstance(items[x], bool) != True:
            new_items.append(items[x])
    return new_items