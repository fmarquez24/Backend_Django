'''
This is to open the file open ('name_of file", 'permsions')
Permsions 'r' is to read, 'w' to write, 'a' to append(add at the end)
'r+' to read/write
files have to be in the same folder
'''

country_file = open('countries.txt', 'r')
'''
# This tells us if the file is readable:
print(country_file.readable())
'''

'''
# this read the first line and its sequential so the next time you execute this code it skips line
print(country_file.readline())
print(country_file.readline())
'''

'''
# this prints the entire content of the file as a list
print(country_file.readlines())
'''

'''
# this selects the specific value
print(country_file.readlines()[1])
'''

for file in country_file.readlines():
    print(f" I Would like to visit: {file}")



country_file.close()
