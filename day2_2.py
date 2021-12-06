with open('day2_inputs.txt', 'r') as f:
    d_diff = 0
    fwd = 0
    aim = 0
    for cmd in f:
        d   = cmd.split(" ")[0]
        amt  = int(cmd.split(" ")[1])
        if d == "down":
            aim += amt 
        elif d == "up":
            aim -= amt
        else:
            fwd += amt
            d_diff += amt * aim

    print("total d_diff: ", d_diff)
    print("total amt fw: ", fwd)
    print("answer: ", d_diff * fwd)
