from timeit import default_timer as timer
#string ordered,immutable
my_string="Hello World"
char=my_string[0]
print(char)
substring=my_string[:5]
print(substring)

greeting="Hello"
for x in greeting:
    print(x)
    
if "e" in greeting:
    print("yes")
else:
    print("no")
    
spastring="    hi    "
spastring=spastring.strip()
print(spastring)
print(greeting.find("l"))

list=["a"]*60000

start=timer()
mystring=''
for i in list:
    mystring+=i
stop=timer()
print(stop-start)
start=timer()
mystring=''.join(list)
stop=timer()
print(stop-start)


var="sam"
mystring="the honored one is %s" %var
print(mystring)

var=3.14
var2=7
mystring="The variables are {:.2f} and {}".format(var,var2)
print(mystring)

mystring=f"The variables are {var} and {var2}"
print(mystring)