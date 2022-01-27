#This allows you edit file information
# if you enter a file name that doesnt exist it creates it

country_file = open("countries_new.txt", 'w')
country_file.write("francia")

country_file = open("countries_new.txt", 'a')
country_file.write("\nGhana")