N, M = map(int, input().split())

print("NEWBIE!" if M <= 2 else ("OLDBIE!" if M > 2 and M <= N else "TLE!"))