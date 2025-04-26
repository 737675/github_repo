#Text Analysis with Constraints

from collections import Counter, defaultdict

# Define stop words
stop_words = {'the', 'is', 'at', 'on', 'in', 'and'}

def preprocess(text):
    words = text.lower().split()
    cleaned_words = [word.strip('.,!?') for word in words if word.strip('.,!?') not in stop_words]
    return cleaned_words

def build_frequency(words):
    return Counter(words)

def build_prefix_map(frequencies):
    prefix_map = defaultdict(list)
    for word, freq in frequencies.items():
        for i in range(1, len(word)+1):
            prefix_map[word[:i]].append((word, freq))
    for prefix in prefix_map:
        prefix_map[prefix].sort(key=lambda x: (-x[1], x[0]))
    return prefix_map

def query(prefix_map, prefix, top_n=3):
    return [word for word, _ in prefix_map.get(prefix, [])[:top_n]]

# Example Usage
text = """
The quick brown fox jumps over the lazy dog. 
The fox was quick and smart. The dog was lazy but cute. 
"""

words = preprocess(text)
frequencies = build_frequency(words)
prefix_map = build_prefix_map(frequencies)

# Query Example
print(query(prefix_map, 'qu'))   # top 3 words starting with 'qu'
print(query(prefix_map, 'do'))   # top 3 words starting with 'do'
