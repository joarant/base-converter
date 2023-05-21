def validateNumberField(number: str, FromBase: str):
    try:
        float(number)
        numberCopy = number        
        if "." in number:
            numberCopy = numberCopy.replace('.', '')
        if "-" in number:
            numberCopy = numberCopy.replace('-', '')
        for num in numberCopy:
            if int(num) >= int(FromBase):
                return False
            
        return True
    except:
        return False
    

def validateBase(number: str):

    try:
        if int(number) > 1 and "." not in number:
            return True
        else: 
            return False
    except:
        return False
    