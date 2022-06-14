import random as r
class GenerateIPMacaddress:
    def __init__(self):
        self.hexadecimal_digits=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        self.final_hexa = []
        self.mac_blocks = []
        self.ip4_list = []
        self.broken_url = []
    def IPV6(self):
        for hexa in range(8):
            each_block = ''
            for count in range(4):
                random_integer = r.randint(0,15)
                single_char = str(self.hexadecimal_digits[random_integer])
                each_block += single_char
            self.final_hexa.append(each_block)
        return ':'.join(self.final_hexa)

    def mac_address(self):
        for hexa in range(6):
            each_block = ''
            for count in range(2):
                random_integer = r.randint(0,15)
                single_char = str(self.hexadecimal_digits[random_integer])
                each_block += single_char
            self.mac_blocks.append(each_block)
        return ':'.join(self.mac_blocks)
    

    def ipv4(self):
        count = 1
        while count < 5:
            random_number = r.randint(0,255)
            self.ip4_list.append(str(random_number))
            count += 1
        return '.'.join(self.ip4_list)

    def split_url(self,url):
        split_uri = url.split('/')
        for i in split_uri:
            i = i.strip(':')
            if i != '':
                self.broken_url.append(i)
        return(f"Protocol: {self.broken_url[0]}\nDomain Name: {self.broken_url[1]}\nFolder Structure: {self.broken_url[2]}\nFile name: {self.broken_url[3]}")

generateIP = GenerateIPMacaddress()
print(f"IPV6: {generateIP.IPV6()}")
print(f"IPV4: {generateIP.ipv4()}")
print(f"Mac address: {generateIP.mac_address()}")
print(generateIP.split_url("https://example.com/folder/index.html"))