from acs import convert_decimal_to_other_system


abcs = [
    "abcdefghijklmnopqrstuvwxyz"
]

def add_abc(abc):
    abcs.append(abc)

def encode(word, iterations,abc):
    carry = word
    for i in range(iterations):
        c = carry
        carry = ""
        for j in range(len(c)):
            if c[j] in abc:
                carry += abc[int(convert_decimal_to_other_system(abc.index(c[j])+iterations // 20, 3, 10)) % len(abc)]
    return carry

def main():
    print("""
Hello!
This is a secret code engine.
There is no decoding here.
Enter options:

""")

    query = input("Enter the starting string: ").lower()
    iters = int(input("Enter the amount of iterations: "))
    for i in range (len(abcs)):
        print(i, "-", abcs[i])
    abc = int(input("Please enter the number that is shown next to the wished alphabet. "))
    print("engine is being called... ")
    print (encode(query, iters, abcs[abc]))

#take = int(convert_decimal_to_other_system(int(input("Enter a number: ")), 3, 10)) % 26
#print(take)

