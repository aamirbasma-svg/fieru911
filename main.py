# python code

def main(num):
    ans = num * num
    # print(ans)
    return ans
while True:
    number = int(input("Enter a number: "))
    if (number < 0):
         break
    else:
        ans = main(number)
        print(ans)  

