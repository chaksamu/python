#< less than
#<= lesstha or equal to
#== equal to
#>= greaterthan or equal to
#> greaterthnan
#!=not equal to

def main():
    x=int(input("Enter the First NUmber: "))
    y=int(input("Enter the  Second NUmber: "))
    if x==y:
        print("Both are equal")
    if x<=y:
        print("x and y are same or x is less than y")
    if x<y:
        print("x is always less than y")
    if x>y:
        print("x is always greater than y")
    if x>=y:
        print("x and y are same or x is greater than y")
    if x!=y:
        print("x is not equal to y")


main()