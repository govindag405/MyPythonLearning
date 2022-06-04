#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
import sqlite3


def num_seq(seq_num):
    split_num = seq_num.split(',')
    print(split_num,"\n",tuple(split_num))

num_seq("34,67,55,33,12,98")
