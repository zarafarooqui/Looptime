def test(n):
    iteration=0
    for i in range(0,n+1):
        iteration+=1
        print("when n is",n,"Iterations=",iteration)
test(10)
test(20)
test(40)
print("\n with every 'n' the time taken and iterations will not increase linearly ")
#time complaxity =0(n)
#average case

def printnumber(n):
    literation = 0
    print("the total number entered my user is",n)
    literation+=1
    print("total literation done by computer is",literation,"\n")
printnumber(10)
printnumber(200)
print("\n with any 'n' the time taken will not change")
#best case scenario
#time complexity = 0(1) Big 0 1

#while loop
def test(n):
    iteration=0
    while(iteration<n):
        iteration+=1
        print("when n is",n,"Iterations=",iteration)
test(10)
test(20)
test(40)
print("\n with every 'n' the time taken and iterations will not increase linearly ")
#less time taken
#time complexity = 0(n)