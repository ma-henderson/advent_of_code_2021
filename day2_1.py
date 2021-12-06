with open('day2_inputs.txt', 'r') as f:
    d_diff = 0
    fwd = 0
    for cmd in f:
        d   = cmd.split(" ")[0]
        amt = int(cmd.split(" ")[1])
        if d == "down":
            d_diff += amt 
        elif d == "up":
            d_diff -= amt
        else:
            fwd += amt

    print("total d_diff: ", d_diff)
    print("total amt fw: ", fwd)
    print("answer: ", d_diff * fwd)
