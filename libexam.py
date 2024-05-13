import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import string
import time

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]

def iv():
    """
    The initialization vector to use for encryption or decryption.
    It is ignored for MODE_ECB and MODE_CTR.
    """
    return chr(0) * 16

class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """

    def __init__(self, key):
        self.key = key
        #self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')

class question:
    def __init__(self, qtype, qproblem, qoption1, qoption2, qoption3, qoption4):
        qtype = self.qtype
        qproblem = self.qproblem
        qoption1 = self.qoption1
        qoption2 = self.qoption2
        qoption3 = self.qoption3
        qoption4 = self.qoption4


class libexam:
    mode = 0
    mode_set = 0

    username = ""
    questions = []
    password = -1

    def setmode(modein):
        mode=modein
        modeset=1
        print(f"Mode set to: {mode}\n") #1: client 2: admin
        return 0

    def status():
        return f"""Mode: {mode}
        Username: {username}\n"""


    def setuser(user):
        username=user
        print(f"Username set to: {user}\n")
        return 0

    def setadmin():
        passwordf = open("password.txt", "r")
        password = passwordf.readline()
        print(f"Read password: {password}\n")
        return 0

    def readquestions():
        sha256=hashlib.sha256()

        questiondocs = open("question.txt", "r")
        n = questiondocs.readline()
        sha256.update(n)

        print(f"n={n}\n")

        counter=n
        while(True):#hash check
            temp = questiondocs.readline()
            if(temp=="chk"):
                sha256.update(temp)

                rhash = sha256.digest() 
                ehash = questiondocs.readline()

                if(rhash==ehash):
                    print(f"Hashes match: {rhash}\n")
                    break
                else:
                    print(f"Hashes does not match !\nExpected: {ehash}\nGot: {rhash}\n")
                    return 1
            sha256.update(temp)

        questiondocs.close()
        questiondocs = open("question.txt", "r")
        temp = questiondocs.readline()



        while(True):
            temp = questiondocs.readline()
            if(temp=="chk"):
                break
            qtype = temp

            temp = questiondocs.readline()
            temp = temp.split("|")

            questions.append(question(qtype,temp[0],temp[1],temp[2],temp[3],temp[4]))
        
        
        
    def writeanswer(qn,ans)
        if(username=""){
            print(f"Username not set!\n")
            return 1
        }


        
        md5 = hashlib.md5()
        md5.update(username)
        filename = md5.digest()
        print(f"MD5 hash of {user}: {filename}")
        
        sha256 = hashlib.sha256()
        

        datadocs = open(f"{filename}.txt", "r")
        n = datadocs.readline()
        sha256.update(n)

        while(True):#hash check
            temp = data.readline()
            if(temp=="chk"):
                sha256.update(temp)

                rhash = sha256.digest() 
                ehash = data.readline()

                if(rhash==ehash):
                    print(f"Hashes match: {rhash}\n")
                    break
                else:
                    print(f"Hashes does not match !\nExpected: {ehash}\nGot: {rhash}\n")
                    return 1
            sha256.update(temp)


        datadocs.close()
        datadocs = open(f"{filename}.txt", "r+")
        
        timestamp = hex(int(time.time()))#part c of a line according to docs
        while(len(timestamp) != 16):
            timestamp = "0" + timestamp
        
        cd = timestamp + ans

        bhash = hashlib.sha256()
        bhash.update(cd)
        b = bhash.digest()

        print(f"Timestamp: {timestamp}\nAnswer: {ans}\nPart B Hash: {b}")

        userhash = hashlib.sha256()
        userhash.update(username)
        key = userhash.digest()#generated key for encryption

        print(f"Key generated: {key}\n")

        bcd = AESCipher(key).encrypt(b + cd) #encrypt

        print(f"Parts B C D Encrypted: {bcd}\n")

        ahash = hashlib.sha256()
        ahash.update(bcd)
        a = ahash.digest()

        print(f"Parts A Hash: {a}\n")
        print(f"Data to write: {a + bcd}\n")  

        # read a list of lines into data
        data = datadocs.readlines()

        # now change the answer line, note that you have to add a newline
        data[qn] = a + bcd

        # and write everything back
        datadocs.writelines(data)
        datadocs.close()


        datadocs = open(f"{filename}.txt", "r+")
        n = datadocs.readline()
        sha256.update(n)

        while(True):#calculate hash
            temp = data.readline()
            if(temp=="chk"):
                sha256.update(temp)
                targethash = data.readline()
                break
            sha256.update(temp)
        
        print(f"New hash generated: {targethash}\n")
        

        # read a list of lines into data
        data = datadocs.readlines()

        # now change the answer line, note that you have to add a newline
        data[1+n] = targethash

        # and write everything back
        datadocs.writelines(data)
        datadocs.close()

        return 0
