class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by slash, filtering out empty strings
        comps = [comp for comp in path.split('/') if comp]
        stack = []

        for comp in comps:
            if comp == '..':
                if stack:
                    stack.pop()
            elif comp != '.':
                # Only append if not current directory '.'
                stack.append(comp)

        return '/' + '/'.join(stack)


