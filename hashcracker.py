#!/usr/bin/python
import os
import hashlib
import platform

def crack_md5(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.md5()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.md5(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

def crack_sha256(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.sha256()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.sha256(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

def crack_sha224(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.sha224()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.sha224(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

def crack_sha512(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.sha1()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.sha1(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

def crack_sha384(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.sha512()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.sha512(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

def crack_sha1(_hash,fpath):
    with open(fpath, 'r') as file:
        last_line = file.readlines()
        file.close()
    with open(fpath,'r') as  file:
        # print(last_line[-1])
        for line in file.readlines():
            m = hashlib.sha1()
            m.update(line[:-1].encode())
            guess = m.hexdigest()
            last_line_hash = hashlib.sha1(last_line[-1].encode())
            last_hash = last_line_hash.hexdigest()
            if _hash == guess:
                print("Password Cracked : ", line)
                break
            elif _hash == last_hash:
                print("Password Cracked : ", last_line[-1])
                break
            else:
                print("Password Not Found !")

if "Window" in platform.platform():
    os.system("cls")
else:
    os.system("clear")
print("PASSWORD CRACKER IN PYTHON")
print("CODED BY HUZEFA\n")
files = input("Enter file path (leave empty if you want to use default list): ")
if files == "":
    filepath = "password.txt"
else:
    if os.path.exists(files):
        filepath = files
    else:
        print("Invalid path!")
        exit(-1)
choice = int(input("\nChoose Hash type : \n1. MD5\n2. SHA1\n3. SHA256\n4. SHA384\n5. SHA224\n6. SHA512\n\nEnter your choice : "))
_hash = str(input("\nEnter hash to crack : "))
if choice == 1:
    crack_md5(_hash,filepath)
elif choice == 2:
    crack_sha1(_hash,filepath)
elif choice == 3:
    crack_sha256(_hash,filepath)
elif choice == 4:
    crack_sha384(_hash,filepath)
elif choice == 5:
    crack_sha224(_hash,filepath)
elif choice == 6:
    crack_sha512(_hash,filepath)
else:
    print("Invalid Choice !")