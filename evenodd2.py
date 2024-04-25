# num = int(input("Enter the number :- "))
# if num % 2 == 0:
#     print("Given number is Even")
# else:
#     print("Given number is odd")
def isEven(num):
    return not num&1
if __name__=="__main__":
    num = int(input("Enter the Number :- "))
    if isEven(num):
        print("Even")
    else:
        print("Odd")
