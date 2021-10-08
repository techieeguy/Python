"""
#Python Program to Convert Text into binary

text = input("Enter any Text: ")

print("The original string is : " + text)
  
binary = ' '.join(format(i, '08b') \
for i in bytearray(text, encoding ='utf-8'))

print("Text after binary conversion : ", binary)

# Follow @techieeguy for more.

"""
def BinaryToDecimal(binary): 
    string = int(binary, 2) 
    return string

binary_num = input("Enter Binary Numbers: ")
   
print("The binary value is:", binary_num)
   
str_data =' '
   
for i in range(0, len(binary_num), 7):
    temp_data = binary_num[i:i + 7]
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data) 
  
print("The Binary value after string conversion is:", str_data)
