# @cikey 834c2e6fa9c10fdc8929a92de4d69a3d
# @sid 20251174010006
# @aid V6.2


#begin_inputs
n = int(input())

#end_inputs


for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
