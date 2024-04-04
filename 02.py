k = int(input())
numbers = [int(i) for i in input().split()]
rare_num = []
for num in numbers:
    if num % k == 0 or num % k == 2:
        rare_num.append(num)
for num in rare_num:
    print(num, end=" ")