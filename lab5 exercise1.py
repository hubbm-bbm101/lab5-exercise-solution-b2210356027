N=int(input("Enter a number: "))
evensum=0
number_of_evens=0
oddsum=0
for i in range(1,N+1):
    if i%2==0:
        evensum = evensum + i
        number_of_evens += 1
    else:
        oddsum += i
average_of_evens = evensum / number_of_evens
print("the sum of odd numbers: ", oddsum)
print("the average of even numbers: ", average_of_evens)
