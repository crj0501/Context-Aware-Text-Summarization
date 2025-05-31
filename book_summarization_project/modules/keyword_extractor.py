import re
import heapq
from collections import Counter

def extract_keywords(text, num_keywords=10):
    # Basic cleanup
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()

    # Remove stopwords (minimal list; can be extended)
    stopwords = set([
        'the', 'and', 'is', 'in', 'to', 'of', 'a', 'an', 'for', 'on', 'with','or','can','should','could','would','will','like',
        'as', 'by', 'this', 'that', 'it', 'from', 'at', 'be', 'are', 'was', 'were','1','2','3','4','5','6','7','8','9','0'
    ])
    filtered_words = [word for word in words if word not in stopwords]

    # Count and get most common
    word_freq = Counter(filtered_words)
    keywords = heapq.nlargest(num_keywords, word_freq, key=word_freq.get)

    return keywords
