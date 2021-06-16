jobs = [int(x) for x in input().split(', ')]
index_to_execute = int(input())
cycles = 0
jobs_to_check = []
for index, x in enumerate(jobs):
    temp_list = []
    temp_list.append(x)
    temp_list.append(index)
    jobs_to_check.append(temp_list)
for x in sorted(jobs_to_check):
    cycles += x[0]
    if x[1] == index_to_execute:
        break
print(cycles)