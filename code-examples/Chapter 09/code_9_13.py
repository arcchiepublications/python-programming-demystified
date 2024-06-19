from collections import Counter

text = "a quick brown fox jumps over the lazy dog a quick brown dog"
word_counts = Counter(text.split())

for word, count in word_counts.most_common(3):
    print(f"Word: '{word}', Frequency: {count}")
