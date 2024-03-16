class Solution:
    def decodeString(self, s: str) -> str:
        # make a stack
        stack = []
        for char in s:
            # if the char is NOT encounter ']', then, just STACKing the char(s).
            if char != ']':
                stack.append(char)
            # if the char is eventually encounter ']',
            else:
                substr = ''
                # poping from the stak until encountering '['
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                # fetching a number from the stack
                k = " "
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # stack.pop()

                stack.append(substr * int(k))

        return ''.join(stack)


a