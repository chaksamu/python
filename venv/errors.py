## Complile error -> Syntax Errors (missing :, wrong  print
##logical errors --> not expected o/p or correct o/p
##Runtime errors --> divide 6/0 is not possible
a=4
b=5
print(a/b)

a=0
b=4
try:
    print(a/b)
except Exception:
    print("Hey, You cant Divide by zero")

print("BYE")

a=4
b=0
try:
    print(a/b)
except Exception as e:
    print("Hey, You cant Divide by zero", e)


a=4
b=4
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Hey, You cant Divide by zero", e)

finally:
    print("resource closed")


a=4
b=4
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter your favourite number"))
    print(k)
except Exception as e:
    print("Hey, You cant Divide by zero", e)

finally:
    print("resource closed")




a=4
b=0
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter your favourite number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannt divide by zero")
except ValueError as e:
    print("Hey Input is invalid")
except Exception as e:
    print("Hey, You cant Divide by zero", e)

finally:
    print("resource closed")