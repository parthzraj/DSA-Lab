expression = input("enter the postfix expression: ")
stack = []

def arithemetic_expression(expression):
    i = 0
    

    while i < len(expression):
        ch = expression[i]

        if expression[i] == " ":
                    i += 1
                    continue

        if ch == "+" or ch == "-" or ch == "/" or ch == "*":

            a = stack[-1]
            stack.pop()

            b = stack[-1]
            stack.pop()

            if ch == '+':
                stack.append(b + a)

            elif ch == '-':
                stack.append(b - a)

            elif ch == '/':
                stack.append(b / a)

            elif ch == "*":
                stack.append(b * a)

            print(stack)

        else:
            no = ""

            while i < len(expression) and expression[i] != " ":
                no = no + expression[i]
                i = i + 1

            stack.append(int(no))
            print(stack)

        i = i + 1


arithemetic_expression(expression)