
def calPoints(ops):
    record = []
    for op in ops:
        print(record)
        if op.isnumeric():
            record.append(int(op))
        elif op == "C":
            record.pop()
        elif op == "D":
            record.append(record[-1] * 2)
        elif op == "+":
            record.append(record[-1] + record[-2])
        elif "-" in op:
            record.append(int(op))
    return sum(record)


ops = ["5","-2","4","C","D","9","+","+"]
score = calPoints(ops)
print(score)
