char_arr = [0] * 26

while True:
    try :
        text = input()
        for char in text : 
            if char != ' ' :
                char_arr[ord(char)-ord('a')] += 1
    except EOFError :
        break

max_freq = max(char_arr)

for i in range(26):
    if char_arr[i] == max_freq:
        print(chr(ord('a') + i), end="")