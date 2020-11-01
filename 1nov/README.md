# 1 November (Hackerrank) [14th Day]
## based on stacks

1. [simple text editor](https://www.hackerrank.com/challenges/simple-text-editor/problem)

### A simple text editor

in order to solve the question we need two things first the current strings and second one a stack for saving the previous strings
> we must use a stack to save the past strings we can't acheive this by just using a string var for storing past string becuaase it stores just one past string but need all for undo functios

```python
n=int(input())

string=""
st=[]

for i in range(n):
    v=[x for x in input().strip().split()]
    if v[0]=='1':
        st.append(string)
        string +=v[1]
    elif v[0]=='2':
        pos=len(string)-int(v[1])
        st.append(string)
        string=string[0:pos]
    elif v[0]=='3':
        pos=int(v[1])-1
        print(string[pos])
    else:
        string =st.pop()
```

2. [Largest rectangle problem](https://www.hackerrank.com/challenges/largest-rectangle/problem)

3. [poisonous plants](https://www.hackerrank.com/challenges/poisonous-plants/problem)
