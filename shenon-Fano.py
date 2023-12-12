from Main import text
from pprint import pprint
import math

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None


def calculate_probabilities(text, symbols_to_encode):
    filtered_text = ''.join(char for char in text if char in symbols_to_encode)

    total_characters = len(filtered_text)
    symbol_frequencies = {char: filtered_text.count(char) / total_characters for char in set(filtered_text)}

    return symbol_frequencies


def calculate_entropy(probabilities):
    entropy = -sum(prob * math.log2(prob) for prob in probabilities.values())
    return entropy


def shannon_fano_average_length(codes, probabilities):
    avg_length = sum(len(codes[char]) * probabilities[char] for char in codes)
    return avg_length


def build_shannon_fano_tree(symbols):
    if len(symbols) == 1:
        return Node(symbol=symbols[0][0], frequency=symbols[0][1])

    total_frequency = sum(symbol[1] for symbol in symbols)
    cumulative_frequency = 0
    split_index = 0

    for i, symbol in enumerate(symbols):
        cumulative_frequency += symbol[1]
        if cumulative_frequency * 2 >= total_frequency:
            split_index = i
            break

    left_branch = build_shannon_fano_tree(symbols[:split_index + 1])
    right_branch = build_shannon_fano_tree(symbols[split_index + 1:])

    node = Node()
    node.left = left_branch
    node.right = right_branch

    return node


def generate_shannon_fano_codes(node, code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node.symbol:
        code_dict[node.symbol] = code
    else:
        generate_shannon_fano_codes(node.left, code + "0", code_dict)
        generate_shannon_fano_codes(node.right, code + "1", code_dict)

    return code_dict


def shannon_fano_encode(text, symbols_to_encode):
    probabilities = calculate_probabilities(text, symbols_to_encode)
    root = build_shannon_fano_tree(sorted(probabilities.items(), key=lambda x: x[1], reverse=True))
    codes = generate_shannon_fano_codes(root)

    encoded_text = ''.join(codes[symbol] for symbol in text if symbol in symbols_to_encode)

    return encoded_text, codes, probabilities


def shannon_fano_decode(encoded_text, codes):
    reverse_codes = {code: symbol for symbol, code in codes.items()}

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text


# Пример использования
huge_text = "..."  # Ваш огромный текст здесь
symbols_to_encode = "0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;-"

encoded_result, codes, probabilities = shannon_fano_encode(huge_text, symbols_to_encode)

entropy = calculate_entropy(probabilities)
avg_length = shannon_fano_average_length(codes, probabilities)

huge_text = text
symbols_to_encode = '0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;- ('

encoded_result, codes, probabilities = shannon_fano_encode(huge_text, symbols_to_encode)

entropy = calculate_entropy(probabilities)
avg_length = shannon_fano_average_length(codes, probabilities)

# pprint(f'Исходный текст: {huge_text}')
# pprint(f'Закодированный текст: {encoded_result}')
# pprint(f'Коды символов: {codes}')
#
# decoded_result = shannon_fano_decode(encoded_result, codes)
# pprint(f'Декодированный текст: {decoded_result}')

print("Коды символов Шеннона-Фано:", codes)
print("Энтропия текста:", entropy)
print("Среднее количество двоичных разрядов:", avg_length)