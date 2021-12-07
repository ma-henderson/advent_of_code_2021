with open("day3_inputs.txt", "r") as f:
    data = []
    ln_cnt = 0
    # organize data into list of lists
    for line in f:
        data.append([int(digit) for digit in line if digit != '\n'])
        ln_cnt += 1

    output = data[0]
    for i in range(1, ln_cnt):
        for j in range(len(output)):
            output[j] += data[i][j]
    
    # Set up binary value of gamma/epsilon
    gamma   = [int(round(e / ln_cnt, 0)) for e in output]
    epsilon = [1 if e == 0 else 0 for e in gamma]
    
    print(f'{gamma}\n{epsilon}')
    print("line count: ", ln_cnt)

    # convert list into decimal
    # reverse the list for easier math code
    gamma.reverse()
    epsilon.reverse()
    gamma_val   = 0
    epsilon_val = 0
    for i in range(len(gamma)):
        gamma_val   += gamma[i] * pow(2, i)
        epsilon_val += epsilon[i] * pow(2, i)
        
    # Print the answer
    print(gamma_val * epsilon_val)
