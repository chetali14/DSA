class Solution(object):
    def countOfAtoms(self, formula):
        import collections

        stack = [collections.defaultdict(int)]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1
                num = 0

                while i < len(formula) and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                num = num or 1
                group = stack.pop()

                for atom in group:
                    stack[-1][atom] += group[atom] * num

            else:
                atom = formula[i]
                i += 1

                while i < len(formula) and formula[i].islower():
                    atom += formula[i]
                    i += 1

                num = 0
                while i < len(formula) and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                stack[-1][atom] += num or 1

        ans = ""

        for atom in sorted(stack[-1]):
            ans += atom
            if stack[-1][atom] > 1:
                ans += str(stack[-1][atom])

        return ans