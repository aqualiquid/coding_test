num_of_input = int(input())
list_numbers = list(map(int, input().split()))

sum_list = [0] * num_of_input
sum_list[0]= list_numbers[0]

for i in range(1, num_of_input):
    sum_list[i] = max(list_numbers[i], sum_list[i-1]+list_numbers[i])
print(max(sum_list))