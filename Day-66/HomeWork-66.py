# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def valid_braces(string):
    stack = []
    matching_braces = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != matching_braces[char]:
                return False
    return not stack


# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    return ' '.join(str(ord(char) - 96) for char in text.lower() if char.isalpha())


# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python




#  https://www.codewars.com/kata/61c78b57ee4be50035d28d42/train/python



