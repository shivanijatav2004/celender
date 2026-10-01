##function definition ka use is liye karte h taki redundant km ho jaye
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(34, 23)

calc_sum(31,21)

calc_sum(23, 56)

#example
def clac_sun(a, b): ##parameters
    return a + b
sum = calc_sum(1,2) ##function call ; argument
print(sum)


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

##function koi value return nhi karta us ke liye none value aayegi
def print_hello():
    print("hello")
output = print_hello()
print(output) ##none value