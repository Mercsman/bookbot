def word_count(text):
    count = text.split()
    return len(count)

def character_count(text):
    ch_counts = {}
    for char in text.lower():
        if char in ch_counts:
            ch_counts[char] += 1
        else:
            ch_counts[char] = 1
    return ch_counts