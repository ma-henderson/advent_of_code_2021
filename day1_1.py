with open('day1_1inputs.txt', 'r') as inputs:
    inc_count = 0
    previous = 191
    for current in inputs:
        current = int(current)
        if previous < current:
            inc_count += 1
        previous = current
        
    print(inc_count)