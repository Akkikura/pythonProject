from Main import text
from pprint import pprint


class Node:
    def __init__(self, symbol=None, probability=None):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None


def calculate_probabilities(text, symbols_to_encode):
    filtered_text = ''.join(char for char in text if char in symbols_to_encode)

    symbol_frequencies = [(symbol, filtered_text.count(symbol)) for symbol in set(filtered_text)]
    symbol_frequencies = sorted(symbol_frequencies, key=lambda x: x[1], reverse=True)

    total_characters = len(filtered_text)
    probabilities = [(symbol, frequency / total_characters) for symbol, frequency in symbol_frequencies]

    return probabilities


def build_shannon_fano_tree(probabilities):
    if len(probabilities) == 1:
        return Node(symbol=probabilities[0][0], probability=probabilities[0][1])

    total_probability = sum(symbol[1] for symbol in probabilities)
    cumulative_probability = 0
    split_index = 0

    for i, symbol in enumerate(probabilities):
        cumulative_probability += symbol[1]
        if cumulative_probability * 2 >= total_probability:
            split_index = i
            break

    left_branch = build_shannon_fano_tree(probabilities[:split_index + 1])
    right_branch = build_shannon_fano_tree(probabilities[split_index + 1:])

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
    root = build_shannon_fano_tree(probabilities)
    codes = generate_shannon_fano_codes(root)

    encoded_text = ''.join(codes[symbol] for symbol in text if symbol in symbols_to_encode)

    return encoded_text, codes
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

huge_text = text
symbols_to_encode = '0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;- ('

encoded_result, codes = shannon_fano_encode(huge_text, symbols_to_encode)
probabilities = calculate_probabilities(text, symbols_to_encode)

# pprint(f'Исходный текст: {huge_text}')
# pprint(f'Закодированный текст: {encoded_result}')
# pprint(f'Коды символов: {codes}')
#
# decoded_result = shannon_fano_decode(encoded_result, codes)
# pprint(f'Декодированный текст: {decoded_result}')

pprint(probabilities)