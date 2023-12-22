def encode(string):
  encoded_list = []
  for char in string:
    ascii_code = ord(char)
    binary_code = bin(ascii_code)[2:]
    binary_code = binary_code.zfill(8)
    custom_code = binary_code.replace('1', 'H').replace('0', 'h')
    encoded_list.append(custom_code)
  return "".join(encoded_list)

input = input(">    ")
print(encode(input))