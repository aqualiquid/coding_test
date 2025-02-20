class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        # remove =[]
        remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    # add the index number into remove
                    # remove.append(i)
                    remove.add(i)
        # remove.extend(stack)
        remove = remove.union(set(stack))
        return ''.join([char for i, char in enumerate(s) if i not in remove])