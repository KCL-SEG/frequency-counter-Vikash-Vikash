"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for i in items:
        i = str(i)
        if i in frequencies:
            current = frequencies[i]
            current+=1
            frequencies[i]=current
        else:
            frequencies[i]=1

    return frequencies
