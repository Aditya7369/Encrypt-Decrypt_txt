import string
import random
import os

# Encrypt =====================================
def encrypt(file):
    if os.path.exists(f"{file}"):
        #---------------------------------------
        s=string.ascii_letters + string.digits
        #---------------------------------------
        l=[i for i in s]
        random.shuffle(l)
        #---------------------------------------
        key="".join(l)
        #---------------------------------------
        d={i:j for i,j in zip(s,key)}
        #---------------------------------------
        with open(f"{file}" , "r") as tf:
            text=tf.read()
            tf.close()
        #---------------------------------------
        etext=""
        for i in range(len(text)):
            if text[i] in d:
                etext = etext + d[text[i]]
            else:
                etext = etext + str(text[i])
        #---------------------------------------
        with open(f"{file}" , "w") as tf:
            tf.write(etext)
            tf.close()
        #---------------------------------------
        with open(f"{file}.key" , "w") as tf:
            tf.write(key)
            tf.close()
        #---------------------------------------
        print("[+] Encrypted Success\n")
        #---------------------------------------
    else:
        print("[Error] file not found ")
    

# Decrypt ======================================
def decrypt(file):
    if os.path.exists(f"{file}"):
        #---------------------------------------
        if os.path.exists(f"{file}.key"):
            with open(f"{file}.key" , "r") as tf:
                key=tf.read()
                tf.close()
            os.remove(f"{file}.key")
            #---------------------------------------
            s=string.ascii_letters + string.digits 
            #---------------------------------------
            d={i:j for i,j in zip(key,s)}
            #---------------------------------------
            with open(f"{file}" , "r") as tf:
                etext=tf.read()
                tf.close()
            #---------------------------------------
            dtext=""
            for i in range(len(etext)):
                if etext[i] in d:
                    dtext = dtext + d[etext[i]]
                else:
                    dtext = dtext + str(etext[i])
            #---------------------------------------
            with open(f"{file}" , "w") as tf:
                tf.write(dtext)
                tf.close()
            #---------------------------------------
            print("[+] Decrypted Success\n")
            #---------------------------------------
        else:
            print("[Error] key not found ")
    else:
        print("[Error] file not found ")
    

# encrypt_or_decrypt =================================
def encrypt_or_decrypt():
    while True:
        print("\n[+] Enter 1 for Encryption\n[+] Enter 2 for Decryption\n[+] Enter exit for exit")
        x=(input("[-] Enter choice : ")).lower()
        if x=='1':
            file=input("[-] file : ")
            if file.endswith(".txt"):
                encrypt(file)
            else:
                print("[Error] Enter proper file ")
        elif x=='2':
            file=input("[-] file : ")
            if file.endswith(".txt"):
                decrypt(file)
            else:
                print("[Error] Enter proper file ")
        elif x in ["exit"]:
            print()
            break
        else:
            print("[+] Enter proper Entry")

# "__main__" ===========================================
if __name__ == "__main__" :
    def e_d():
        encrypt_or_decrypt()
    e_d() 
