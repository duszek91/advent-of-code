import hashlib

stan = ""
x = 0
while stan != "000000":
    str2hash = "bgvyzdsv"
    x+=1
    str2hash = str2hash+str(x)
    result =  (hashlib.md5(str2hash.encode())).hexdigest()
    stan = result[:6]
    print(result[:6])
    if stan == "000000":
        print(result)
        print(x)
