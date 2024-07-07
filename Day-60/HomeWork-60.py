# 8 kyu

#1.

def invert(lst):
    return [-x for x in lst]

#2.

def smash(words):
    return " ".join(words)

#3.

def between(a, b):
    return list(range(a, b + 1))

#4.

def between(a, b):
    return list(range(a, b + 1))

#5.

def get_grade(s1, s2, s3):
    average_score = (s1 + s2 + s3) / 3
    
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

#6.

def dna_to_rna(dna):
    return dna.replace('T', 'U')


#7 kyu

#1.
def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

#2.

def stray(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

#3.

