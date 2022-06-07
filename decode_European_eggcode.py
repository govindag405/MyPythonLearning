# 1UK54321; BB 15/08
# Farming method: 0:Organic,1: Free range,2:Barn,3:Cage; UK: Country of Origin, BB: Best Before
def getCountryCode(filename):
    country_code = {}
    with open(filename) as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(',')
            country_code[line[0]] = line[1]
    return country_code
farming_methods={0:"Organic",1:"Free range",2:"Barn",3:"Cage"}
country_codes = getCountryCode("country_code.txt")
stamped_code = input("Please enter the code visible on the egg: ")
farming_method = int(stamped_code[0])
country_code = stamped_code[1:3]
farm_id = stamped_code[3:]
print(f"Farming method: {farming_methods[farming_method]}\nCountry of Origin: {country_codes[country_code]}\nFarm Id: {farm_id}")