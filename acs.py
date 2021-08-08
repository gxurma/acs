abcs = [
    " abcdefghijklmnopqrstuvwxyz1234567890?()+*''.:,;§$%&!^°",
]

digits = [
    [" ",
    "|",
    "–",
    "/",
    "\\"]
]


def add_abc(inp):
    """Add a custom alphabet to the system."""
    abcs.append(inp)

def add_digits(inp):
    """Adds a custom charset for digits."""
    digits.append(inp)

def convert_decimal_to_other_system(num, system, max_length):
    """This is a custom converter which converts a decimal into a string that constains a number of the desired system.
    It could even be used for other projects as well."""
    
    final = ""
    carry = num
    for i in range(0, max_length).__reversed__():
        exp = system**i
        number = carry // exp
        rest = carry % exp
        carry = rest
        final += str(number)

    return final


def convert_to_dec(num:str, system:int):
    """This function converts a string number e.g '000031'(quintential) to decimal e.g (16)"""
    carry = 0
    for i in range(len(num)):
        carry += system**i * int(num[(len(num)-i-1)])
    return carry

def convert_to_quint(num, digits):
    """It converts a string number to the quintential number system value. Digits is a list of characters, So it is not recommended to be used for other projects."""
    carry = ""
    for i in num:
        carry += digits.index(i).__str__()
    return carry


def decode(inp, abc, digits):
    """This function is responsible for decoding the ascii letter. It does this by getting the index of the character in each line. Then the new number is converted
    into the quintential number system. Then this number can be used as the index of the initial letter."""
    final = ""
    for i in inp:
            number = convert_to_quint(i, digits)
            number = convert_to_dec(number, 5)
            final += abc[number % len(abc)]
    return final

def export(name, result):
    with open(name, "w+") as f:
        for i in result:
            f.write(i)
            f.write("\n")

def encode(inp, abc, digits):
    """This is the encoder, which converts the index of the letter into a quintential number system to index in the 'digits' list.
    Unknown characters are converted to an empty line."""
    final = []
    for i in inp:
        if i in abc:
            line = ""
            number = convert_decimal_to_other_system(abc.index(i), 5, 6)
            for i in number:
                line += digits[int(i)]
            final.append(line)
        else:
             final.append("______")
    return final

def main():
    print("""
Hello,
this is acs, which is an ascii-art based encoding.
Enter a mode, then the input.
special characters are not encoded.

1 - encoding
2 - decoding
""")
    inout = input("Enter a mode: ")
    if inout == "1":
        query = input("Enter the string you want to modify (non-destructive): ")
    elif inout == "2":
        answer = input("Do you want to decode a file? Y/N ").lower()
        if answer == "n":
            length = int(input("Enter the amount of lines the encoded message has that you got from the encoder: "))
            query = []
            for i in range(length):
                query.append(input("Please copy the line(!) here: "))
        elif answer == "y":
            query = []
            name = input("Please enter the filename then: ")
            with open(name) as f:
                for i in f.readlines():
                    query.append(i.replace("\n", ""))
    print("Enter an index of an alphabet.")
    for i in range(len(abcs)):
        print(i, "-", abcs[i])
    abc = int(input())
    print("Enter an index of a digit-set.")
    for i in range(len(digits)):
        print(i, "-", digits[i])
    digit = int(input())
    if inout == "1":
        print("calling encoder...")
        result = encode(query.lower(), abcs[abc], digits[digit])
        for i in result:
            print(i)
        answer = input("Do you want to export this message as a file? Y/N ").lower()
        if answer == "y":
            name = input("Please enter the name of the file. ")
            export(name, result)
        else:
            pass
    elif inout == "2":
        print("calling decoder...")
        result = decode(query, abcs[abc], digits[digit])
        print(result)
