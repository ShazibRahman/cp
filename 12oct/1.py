char_stack=[]
mapper={"(":")","[":"]","{":"}"}

def func(a):
  for char in a:
    if char in mapper:
       char_stack.append(char)
    else:
       if not char_stack or mapper[char_stack.pop()]!=char:
          return False
  return not char_stack

print(func('[{}]'))
