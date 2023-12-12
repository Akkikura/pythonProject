from Main import text
from pprint import pprint
import math


class node:
    def __init__(self) -> None:
        # for storing symbol
        self.sym = ''
        # for storing probability or frequency
        self.pro = 0.0
        self.arr = [0] * 20
        self.top = 0


p = [node() for _ in range(50)]

def calculate_probabilities(text, symbols_to_encode):
    row = 2
    filtered_text = ''.join(char for char in text if char in symbols_to_encode)

    symbol_frequencies = [(symbol, filtered_text.count(symbol)) for symbol in set(filtered_text)]
    symbol_frequencies = sorted(symbol_frequencies, key=lambda x: x[1], reverse=True)

    total_characters = len(filtered_text)
    probabilities = {}
    for symbol, frequency in symbol_frequencies:
        probabilities[symbol] = frequency/total_characters
    # probabilities_2 = [(symbol, frequency / total_characters) for symbol, frequency in symbol_frequencies]
    # probabilities_2 = [(symbol, frequency / total_characters) for symbol, frequency in symbol_frequencies]

    # for i in probabilities:
    #     value_1 = i[0]
    #     value_2 = i[1]
    #     cell = ws.cell(row=row,column=1)
    #     cell.value = value_1
    #     cell_2 = ws.cell(row=row,column=2)
    #     cell_2.value = value_2
    #     row+=1

    return probabilities


def calculate_entropy(probabilities):
    entropy = -sum(prob * math.log2(prob) for prob in probabilities.values())
    return entropy


def shannon_fano_average_length(codes, probabilities):
    avg_length = sum(len(codes[char]) * probabilities[char] for char in codes)
    return avg_length


def is_prefix(code, other_code):
    return code.startswith(other_code) or other_code.startswith(code)


def check_decoding_uniqueness(codes):
    for code1, symbol1 in codes.items():
        for code2, symbol2 in codes.items():
            if code1 != code2 and (code1.startswith(code2) or code2.startswith(code1)):
                return False
    return True


def shannon(l, h, p):
    pack1 = 0;
    pack2 = 0;
    diff1 = 0;
    diff2 = 0
    if ((l + 1) == h or l == h or l > h):
        if (l == h or l > h):
            return
        p[h].top += 1
        p[h].arr[(p[h].top)] = 0
        p[l].top += 1
        p[l].arr[(p[l].top)] = 1

        return

    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1):
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 1

        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 0

        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


# Function to sort the symbols
# based on their probability or frequency
def sortByProbability(n, p):
    temp = node()
    for j in range(1, n):
        for i in range(n - 1):
            if ((p[i].pro) > (p[i + 1].pro)):
                temp.pro = p[i].pro
                temp.sym = p[i].sym

                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym

                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


# function to display shannon codes
def display(n, p):
    fin = {}
    for i in range(n - 1, -1, -1):
        code = ''
        for j in range(p[i].top + 1):
            code += str(p[i].arr[j])
        fin[p[i].sym] = code
    print()
    print(fin)



# Driver code
total = 0
s = '0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;- ('
# Input number of symbols
print("Enter number of symbols\t: ", end='')
n = 42
print(n)
i = 0
# Input symbols
for symb in probabilities.keys():
    print("Enter symbol", i + 1, " : ", end="")
    print(symb)
    # Insert the symbol to node
    p[i].sym += symb
    i += 1

# Input probability of symbols
x = calculate_probabilities(text)
for i in range(n):
    print("\nEnter probability of", p[i].sym, ": ", end="")
    print(x[i])

    # Insert the value to node
    p[i].pro = x[i]
    total = total + p[i].pro

    # checking max probability
    if (total > 1):
        print("Invalid. Enter new values")
        total = total - p[i].pro
        i -= 1

i += 1
p[i].pro = 1 - total
# Sorting the symbols based on
# their probability or frequency
sortByProbability(n, p)

for i in range(n):
    p[i].top = -1

# Find the shannon code
shannon(0, n - 1, p)

# Display the codes
display(n, p)

print()
print(p[0].top)