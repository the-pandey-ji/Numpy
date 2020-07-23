import numpy as np
st1="My name is Sonu Pandey"
st2="He is your Dad"

print(np.char.add(st1,st2))
print(np.char.lower(st1))
print(np.char.center(st1,100,fillchar="*"))
print(np.char.split(st1))
print(np.char.splitlines("sonu\npandey"))
print(np.char.split(st1,"is"))
print(np.char.join(["@",""],[st1,st2]))
print(np.char.replace(st2,"Dad","DAD"))
print(st2)
print(np.char.not_equal("a","a"))
print(np.char.count(st1,"a"))
print(np.char.find(st1,"iss"))