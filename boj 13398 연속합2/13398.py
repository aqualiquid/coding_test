num_of_input = int(input())
list_numbers = list(map(int, input().split()))

sum_not_remv = [0] * num_of_input
sum_remv     = [0] * num_of_input

sum_not_remv[0] = list_numbers[0]
sum_remv[0]     = -float('inf')

for i in range(1, num_of_input):
    sum_not_remv[i] = max(list_numbers[i], sum_not_remv[i-1]+ list_numbers[i])
    sum_remv[i] =     max(sum_not_remv[i-1], sum_remv[i-1]+ list_numbers[i])

print(max(max(sum_not_remv), max(sum_remv)))
