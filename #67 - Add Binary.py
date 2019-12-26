from collections import deque

def addBinary(self, a: str, b: str) -> str:
    result = deque()
    carry = 0

    a = list(a)
    b = list(b)

    while(carry or a or b):
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        
        result.appendleft(str(carry % 2))

        carry = carry // 2
    
    return ''.join(result)

if __name__ == "__main__":
    print(addBinary(None,'11','1'))
