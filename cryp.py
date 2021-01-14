#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Crypto
## File description:
## cryp
##

import hashlib

def origin(name):
    f = open(name, "r")
    arr = f.read().split('\n')
    return arr

def convert(name):
    f = open(name, "r")
    final = []
    arr = f.read().split('\n')
    for i in arr:
        final.append(hashlib.sha256(i.encode('utf-8')).hexdigest())
    return final

def main():
    origins = origin("phpbb.txt")
    text = convert("phpbb.txt")
    j = 0
    mdp = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"
   # h = hashlib.sha256(mdp.encode('utf-8'))
    for i in text:
        j+=1
        if mdp == i:
            print("found =", origins[j], "at line =", j)
main()