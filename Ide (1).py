
import re
strr = "The rain in twenty four dollar ddd ghhhh triple A and jkjk double B"
x = re.findall("twenty four", strr)

def listToString(x):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(x)) 
        
        
# Driver code    
uu=listToString(x)

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["seven billion one hundred million thirty one thousand three hundred thirty sevenand"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
zz =  text2int(uu)
print(zz)
index = strr.find('twenty four')
output_line = strr[:index] + str(zz) + strr[index:]

print(output_line)
vv=output_line.replace("twenty four","")
bb=vv.replace("dollar","$")
print(bb)
def move_word(bb, word, pos):
   split = bb.split()
   split.insert(pos, split.pop(split.index(word)))
   return ' '.join(split)
nn=move_word(bb, '$', 3)

hu=re.sub(r'(?:(?<=\$) | (?=\/))','',nn)

for idd, www in enumerate(hu.split()):
    if www=="triple":
        az=hu.split()[idd+1]*3
        addd=listToString(az)
        arr=hu.replace("triple A",az)
        print(arr)
    if www=="double":
        ae=hu.split()[idd+1]*2
        fhh=hu.replace("double B",ae)
        print(fhh)
        
     
