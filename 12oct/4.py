class Solution:
    def decodeString(self, s: str) -> str:

        num_stack, num = [], 0
        str_stack = ['']
        for char in s:
            if char == "[":
                num_stack.append(num)
                str_stack.append('')
                num = 0
            elif char == "]":
                decoding = num_stack.pop() * str_stack.pop()
                str_stack[-1] += decoding
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                str_stack[-1] += char

        return str_stack[-1]
