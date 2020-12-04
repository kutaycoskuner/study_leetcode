import argparse

# :: nth prime number calculator
def nthPrime(n):
    current_num, iterator, counter = 2, 2, 0
    while n > counter:
        isPrime = True
        # :: control if its prime
        while current_num/2 >= iterator:
            if current_num % iterator == 0:
                isPrime = False
            iterator += 1

        # :: prime ise counter arttir
        if isPrime == True:
            counter += 1

        # :: counter n e esit ise don
        if counter == n:
            return current_num
        # :: degilse siradaki sayiya gec
        else: 
            current_num += 1

def Main():
    # :: Argparser usage block
    parser = argparse.ArgumentParser()
    # >> positional (mandatory) argument  
    parser.add_argument("num", help="Give an <n> number to calculate nth prime number.", type=int)
    # >> mutually exclusive argument
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose", action="store_true")
    group.add_argument("-q","--quiet", action="store_true")
    # >> optional argument
    parser.add_argument("-o","--output", help="Output result to a file", action="store_true")
    # >> parser variable
    args = parser.parse_args()

    # :: implementation on our code
    result = nthPrime(args.num)

    if args.verbose:
        print("the " + str(args.num) + ". prime number is " + str(result))
    elif args.quiet:
        print(result)
    else:
        print("Prime(" + str(args.num) + ") = " + str(result))

    if args.output:
        f = open("database/primes.txt", "a") ## >> a for add
        print("result is saved in database/primes.txt")
        f.write(str(result)+'\n')


if __name__ == "__main__":
    Main()

# :: 10 un katlarinda giden primelar hep 9 ile bitiyor
        