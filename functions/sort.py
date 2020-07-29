def bubble_sort(values: list):
    for i in range(len(values)-1):
        for j in range(i+1, len(values)):
            if values[j] < values[i]:
                values[j], values[i] = values[i], values[j]