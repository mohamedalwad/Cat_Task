set = []

for i in range(10):
    operation = input("enter operation, click Enter to end it")
    if operation == "":
        break
    else:
        set.append(operation)

result = 0
for operation in set:
    if operation == "++":
        result += 1
    elif operation == "--":
        result -= 1






print(result)