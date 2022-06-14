#Write a python program to generate and output:A random IPv4 address, A random IPv6 address, A random MAC address.
# IPv4: 128.223.85.239, IPv6: C96A:B805:15B7:E706:8213:AFC7:8CD6:0172
#Write a python program that asks the user to enter a URL. The program will then extract and output the following components of the URL:
# Protocol, Domain Name, Folder Structure, File name.

import random as r
hexadecimal_digits=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
def IPV6():
    #hexadecimal_digits=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    final_hexa = []
    for hexa in range(8):
        each_block = ''
        for count in range(4):
            random_integer = r.randint(0,15)
            single_char = str(hexadecimal_digits[random_integer])
            each_block += single_char
        final_hexa.append(each_block)
    return ':'.join(final_hexa)
ipv6_address = IPV6()

def mac_address():
    mac_blocks = []
    for hexa in range(6):
        each_block = ''
        for count in range(2):
            random_integer = r.randint(0,15)
            single_char = str(hexadecimal_digits[random_integer])
            each_block += single_char
        mac_blocks.append(each_block)
    return ':'.join(mac_blocks)
mac_address = mac_address()

def ipv4():
    ip4_list = []
    count = 1
    while count < 5:
        random_number = r.randint(0,255)
        ip4_list.append(str(random_number))
        count += 1
    return '.'.join(ip4_list)

ipv4_address = ipv4()


def split_url(url):
    split_uri = url.split('/')
    broken_url = []
    for i in split_uri:
        i = i.strip(':')
        if i != '':
            broken_url.append(i)
    return(f"Protocol: {broken_url[0]}\nDomain Name: {broken_url[1]}\nFolder Structure: {broken_url[2]}\nFile name: {broken_url[3]}")

split_url(u"https://example.com/folder/index.htm")



    