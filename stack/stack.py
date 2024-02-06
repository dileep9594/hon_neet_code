class Stack :

    def validParentheses(self):
        pass

    def minStack(self):
        pass

    def evaluateReversPolishNotation(self):
        pass

    def generateParentheses(self,n):
        stack = []
        res = []
        def backtrack(openN,closedN):
            if openN == closedN == n :
                res.append("".join(stack))
                return
            if openN < n :
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN :
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res


    def dailyTemprature(self):
        pass

    def carFleet(self):
        pass


    def largestRectangleInHistory(self):
        pass


if __name__ == '__main__':
    stack = Stack()
    print(stack.generateParentheses(3))
    print("Stack")