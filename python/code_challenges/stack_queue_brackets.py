from data_structures.stack import Stack


def multi_bracket_validation(input):
    print(f"input is {input}")
    stack = Stack()
    for i in input:
        print(f"checking {i}")
        if i == "{":
            stack.push("{")
        if i == "(":
            stack.push("(")
        if i == "[":
            stack.push("[")
            print(f"{stack.top.value} is the value on top of the stack")
        if i == "}":
            try: 
                if stack.top.value == "{":
                    stack.pop()
                else:
                    return False
            except:
                return False
        if i == ")":
            try: 
                if stack.top.value == "(":
                    stack.pop()
                else:
                    return False
            except:
                return False
        if i == "]":
            try: 
                if stack.top.value == "[":
                    stack.pop()
                else:
                    return False
            except:
                return False
    if stack.is_empty() == True:  
        return True
    else:
        return False 


