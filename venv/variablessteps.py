#reserved words
#and del for is raise
#assert elif from lamdba return
#break else global not try
#class except if or while
#continue exec import pass yield
#del finally in print

#x=3 Assignment statement
#x=x+3 Assignment with expression
#print print statement

# = is assignment operator

# +  Add
# - Sub
# * Mutiply
# /  Division
# **  Power
# %  Remainder
#paranthesis has most prioority and Multipy and Addition

def main():

    x=5
    y=2
    z=2.0
    name='chakri'
    print('Addition:', x+y)
    print('Subtraction',x-y)
    print('Multipy',x*y)
    print('Division',x/y)
    print('Power',x**y)
    print('Remainder',x%y)
    print('Complex',(x*y)+((y+x)/2)-x**y+x%y)
    print('Hello'+' World')   #concatenate the strings operator type inform python what need to done
    print(type(name))
    print(type(x))
    print(id(name))
    print(id(x))
    print(id(2))
    print(type(z))
    print(float(x)+y)
    

main()
