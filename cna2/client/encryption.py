

def encode1(s):
    
    ans=""
    
    for i in s:
        if(i.isalnum()):
            if(ord(i)>=97):
                ans+=chr((ord(i)-97 +5)%26+97)
            elif(ord(i)>64):
                ans+=chr((ord(i)-65 +5)%26+65)
            else:
                ans+=chr((ord(i)-48 +5)%10+48)
        else:
            ans+=i
    return ans
    


def decode1(s):
    
    ans=""
    
    for i in s:
        if(i.isalnum()):
            if(ord(i)>=97):
                ans+=chr((ord(i)-97 -5)%26+97)
            elif(ord(i)>64):
                ans+=chr((ord(i)-65 -5)%26+65)
            else:
                ans+=chr((ord(i)-48 -5)%10+48)
        else:
            ans+=i
    return ans
    


def transpose(s):
    if len(s)==0:
        return ""
    if s.isspace():
        return s
    l=s.split()
    if len(l)==0:
        return ""
    if len(l)==1:
        return s[::-1]
    
    ans=""
    
    for i in l:
        ans+=i[::-1]+" "
    return ans[0:len(ans)-1]


