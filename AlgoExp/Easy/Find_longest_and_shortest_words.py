# Time Worst - O(n * m) where n is len of string and m is len of chars
# Time Avg - O(n)
# Space - O(n + m) if local O(n) if passed 
def short_and_log(string):
    currentLong = ''
    currentShort = string
    chars = ['!', '@', '#', '$', '%', '?', ',', '.', ' ']
    # itterate through the string and find the longest and shortest words
    word = ''
    for i in range(0, len(string)):
        ch = string[i]
        print(ch, i, len(string))
        if ch in chars:
            if len(word) >= len(currentLong):
                currentLong = word
            if len(word) <= len(currentShort):
                currentShort = word
            word = ''
            continue
        if i == len(string) - 1:
            word = word + ch
            if len(word) >= len(currentLong):
                currentLong = word
            if len(word) <= len(currentShort):
                currentShort = word
            break
        word = word + ch
    return [currentLong.lower(), currentShort.lower()]

# Test using pytest
def test_001():
    assert short_and_log("hello worlds") == ['worlds', 'hello']

def test_002():
    assert short_and_log('HELLO WORLDS') == ['worlds', 'hello']

def test_003():
    assert short_and_log('') == ['', '']

def test_004():
    assert short_and_log("Hello worlds!") == ['worlds', 'hello']
