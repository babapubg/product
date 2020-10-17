pro=1
n=int(input("Enter the total numbers to be multiplied : "))
i=1
while i <= n:
    a = int(input("Enter the number at "+str(i)+" position : "))
    pro= pro * a
    i = i+1
print("Product of " + str(n) +" numbers = ",pro)
