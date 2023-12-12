import heapq
from collections import defaultdict
from Main import text

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    # Добавляем метод для сравнения узлов по их частоте
    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(symbol_frequencies):
    priority_queue = [Node(symbol=char, frequency=freq) for char, freq in symbol_frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)

        merged_node = Node(frequency=node1.frequency + node2.frequency)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node.symbol:
        code_dict[node.symbol] = code
    else:
        generate_huffman_codes(node.left, code + "0", code_dict)
        generate_huffman_codes(node.right, code + "1", code_dict)

    return code_dict

def huffman_encode(text, symbols_to_encode):
    symbol_frequencies = defaultdict(int)
    for char in text:
        if char in symbols_to_encode:
            symbol_frequencies[char] += 1

    root = build_huffman_tree(symbol_frequencies)
    codes = generate_huffman_codes(root)

    # Сортируем коды по убыванию частоты символов
    sorted_codes = sorted(codes.items(), key=lambda x: symbol_frequencies[x[0]], reverse=True)

    encoded_text = ''.join(codes[char] for char, _ in sorted_codes if char in symbols_to_encode)

    return encoded_text, sorted_codes

# Пример использования
input_text = text
symbols_to_encode = '0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,:;- ('

encoded_result, huffman_codes = huffman_encode(input_text, symbols_to_encode)

print("Исходный текст:", input_text)
print("Закодированный текст:", encoded_result)
print("Коды символов Хаффмана:", huffman_codes)