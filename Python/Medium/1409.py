
def processQueries(queries, m):
    permutation = [i for i in range(1,m+1)]
    output = []
    for num in queries:
        for i in range(len(permutation)):
            if permutation[i] == num:
                output.append(i)
                permutation.pop(i)
                permutation.insert(0,num)
                break
    return output




queries = [7,5,5,8,3]
m = 8
processed = processQueries(queries,m)
print(processed)
