with open('day1_1inputs.txt', 'r') as inputs:
    inc_count = 0
    data = [int(current) for current in inputs]
    previous = data[0] + data[1] + data[2]
    for i in range(1, len(data) - 2):
        temp = data[i] + data[i + 1] + data [i + 2]
        if temp > previous:
            inc_count += 1
        previous = temp

    print(inc_count)