A, B = input().split()
A_min, A_max, B_min, B_max = "", "", "", ""

for i in A :
    A_min += "5" if i == "6" else i
    A_max += "6" if i == "5" else i

for i in B :
    B_min += "5" if i == "6" else i
    B_max += "6" if i == "5" else i

print(str(int(A_min) + int(B_min)) + " " + str(int(A_max) + int(B_max)))