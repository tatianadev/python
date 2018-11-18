import json
import os
import sys

file_name = "data.txt"
header_encrypted = b'\x8b\xad\xf0\x0d'
header_not_encrypted = b'\xca\xfe\xba\xbe'
data_json = {}


def check_if_file_encrypted(header):
    if header == header_encrypted:
        file_encrypted = True
    elif header == header_not_encrypted:
        file_encrypted = False
    else:
        print("Header of file is not correct!")
        sys.exit()

    return file_encrypted


def decrypt_data(data):
    decrypted_data = bytearray()
    for i in data:
        decrypted_data.append(255 - i)
    return decrypted_data


name = input("Please enter your name: ")
age = input("Please enter your age:")
profession = input("Please enter your profession:")

encrypt_file_sign = input("Do you want to encrypt your data[Y/n]?")

if os.path.isfile(file_name):
    with open(file_name, 'rb') as f:
        file_data = f.read()

    if check_if_file_encrypted(file_data[:4]):
        data_from_file = decrypt_data(file_data[4:])
    else:
        data_from_file = file_data[4:]

    # data_from_file.decode() - decode converts from bytes to str type
    data_json = json.loads(data_from_file.decode())  # type of data_json: dict

if encrypt_file_sign.upper() == 'Y':
    encrypt_sign = True
    file_header = header_encrypted
else:
    encrypt_sign = False
    file_header = header_not_encrypted

data_json[name] = {"age": age, "profession": profession}

data_json_bytes = json.dumps(data_json, indent=4).encode('utf-8')  # type of data_json_bytes: bytes

# add header to bytearray
data_for_file = bytearray()
for i in file_header:
    data_for_file.append(i)

# add dict data to bytearray
if encrypt_sign:
    for i in data_json_bytes:
        data_for_file.append(255 - i)
else:
    for i in data_json_bytes:
        data_for_file.append(i)

print("Data for file: {}".format(data_for_file))
with open(file_name, 'wb') as fp:
    fp.write(data_for_file)
