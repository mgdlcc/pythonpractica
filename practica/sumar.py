final_sum = 0
n = int(input("How many numbers?: "))
for i in range (0,n):
    s = float(input("Enter number: "))
    final_sum = final_sum + s    #or use final_sum += s

print(f'La suma final es: {final_sum}')


