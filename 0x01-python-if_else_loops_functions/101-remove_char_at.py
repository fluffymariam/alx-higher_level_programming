#!/usr/bin/python3

def remove_char_at(str, m):
    if m < 0:
        return (str)
    return (str[:m] + str[m+1:])
