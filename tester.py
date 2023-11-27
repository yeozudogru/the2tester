from the2 import check_month

resultList = []
theList = []
with open('results.txt', 'r') as results:
    for line in results:
        line = line.strip('\n')
        result = eval(line)
        resultList.append(result)
with open('test.txt', 'r') as test:
    for line in test:
        line = line.strip('\n').split(' ')
        theResult = check_month(line)
        theList.append(theResult)

for i in range(len(resultList)):
    if isinstance(resultList[i], list) and isinstance(theList[i], list):
        if resultList[i].sort() != theList[i].sort():
            print(f'Test Case {i + 1} Failed.')
            continue
    elif isinstance(resultList[i],int) and isinstance(resultList[i],int):
        if resultList[i] != theList[i]:
            print(f'Test Case {i + 1} Failed.')
            continue
    else:
        print(f'Test Case {i + 1} Failed.')
