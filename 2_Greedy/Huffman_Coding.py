import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None

    freq = Counter(text)
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]



def build_huffman_tree(text):
    if not text:
        return None
    
    freq = Counter(text):
    heap = [Node(char, f) for char, f in freq.items()]

    freq = Counter(text)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heap = heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappush(heap)
        
        merged = Node(None, left.freq + right.freq)



def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = dict()
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(text):
    root = build_huffman_tree(text)
    codebook = build_codes(root)
    encoded = ''.join(codebook[char] for char in text)
    return encoded, codebook

def huffman_decode(encoded, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded = []
    code = ""
    for bit in encoded:
        code += bit
        if code in reverse_codebook:
            decoded.append(reverse_codebook[code])
            code = ""
    return ''.join(decoded)

# Example usage
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    encoded, codebook = huffman_encode(text)
    print("Encoded:", encoded)
    print("Codebook:", codebook)
    decoded = huffman_decode(encoded, codebook)
    print("Decoded:", decoded)


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree():

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

def huffman_encode(text):
    root = build_huffman_tree(text):
    codebook = build_code()
    encoded = ''.join(codebook[char] for char in text)
