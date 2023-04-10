import hashlib
def encryption(password):
    result = hashlib.sha256(password.encode())
    print("Encrypted password :", result.hexdigest())
    print("Algo Name : sha256")
    
    result = hashlib.sha384(password.encode())
    print("Encrypted password :", result.hexdigest())
    print("Algo Name : sha384")
    
password, namedParam = input("Enter two values: ").split();
if(namedParam == "algo"):
    encryption(password)
elif (namedParam == "text"):
    print(password)
elif(namedParam == "length"):
    print (len(password))
