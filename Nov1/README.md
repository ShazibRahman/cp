# 1 November (Hackerrank) [14th Day]
## based on stacks

---

### [1. A simple text editor](https://www.hackerrank.com/challenges/simple-text-editor/problem)

in order to solve the question we need two things first the current strings and second one a stack for saving the previous strings
> we must use a stack to save the past strings we can't acheive this by just using a string var  becuaase it stores just one past strings but need all the past strings for multiple  undo functions

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

---


### [2.  Largest-rectangle](https://www.hackerrank.com/challenges/largest-rectangle/problem)

> * Maintain a stack
> * If stack is empty or value at index of stack is less than or equal to value at current  index, push this into stack.
> * Otherwise keep removing values from stack till value at index at top of stack is  less than value at current index.
> * While removing value from stack calculate area
> * if stack is empty
> * it means that till this point value just removed has to be smallest element
> * so area = input[top] * i
> * if stack is not empty then this value at index top is less than or equal to
> * everything from stack top + 1 till i. So area will
> * area = input[top] * (i - stack.peek() - 1);
> * Finally maxArea is area if area is greater than maxArea.

```python
def largestRectangle(h):
    st=[]
    area=0
    i=0
    max_area=0


    while i < len(h):
        if not st or h[st[-1]] < h[i]:
            st.append(i)
            i+=1


        else:
            top=st.pop()

            if not st:
                area=h[top]*i

            else:
                area= h[top]*(i-st[-1]-1)
        if area > max_area:
            max_area=area


    while st :
        top=st.pop()
        if not st:
            area= h[top]*i
        else:
            area=h[top] * (i-st[-1]-1)
        if area > max_area:
            max_area=area
    return max_area
```
---

###  [3. Poisonous Plants](https://www.hackerrank.com/challenges/poisonous-plants/problem)



> * Maintain a Stack
> * Intially the alive days for every plants will be one
> * If stack is empty push the days of plant and plant index to the stack.
> * else if the stack is not empty , it will check all the plants in the stack [all left to it ]
> * pop the element in the stack if it has more pesticides than the current plant and increase the Alive day till we either reach end of the stack or the plants having less pesticides
> * check if the Alive day of this plant is maximum if not continue else update the value and append this plant and its alive days to Stack


```python
def poisonousPlants(plants):
    stack = []
    maxDays = -math.inf

    for plant in plants:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)

        if not stack:
            days = 0

        maxDays = max(maxDays, days)
        stack.append((plant, days))

    return maxDays

```
