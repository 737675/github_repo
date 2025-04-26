#Reverse Counting Problem 1000 to 1

def reverse_counting(n):
    if n < 1:
        return
    print(n)
    reverse_counting(n-1)

(reverse_counting(1000))
