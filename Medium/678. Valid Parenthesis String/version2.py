"""
Time limit exceeded
"""
def checkValidString(s: str) -> bool:
    def backtrack(curr_solution):
        found_star, open_counter = False, 0
        for i, c in enumerate(curr_solution):
            if c == '*':
                found_star = True
                if backtrack(curr_solution[:i] + '(' + curr_solution[i+1:]) or backtrack(curr_solution[:i] + ')' + curr_solution[i+1:]) or backtrack(curr_solution[:i] + '' + curr_solution[i+1:]):
                    return True
            elif c == '(':
                open_counter += 1
            else: # c == ')'
                if open_counter > 0:
                    open_counter -= 1
                else:
                    return False
        if open_counter != 0:
            return False
        return True

    return backtrack(s)

if __name__ == "__main__":
    assert checkValidString("()") == True
    assert checkValidString("(*)") == True
    assert checkValidString("()") == True
    assert checkValidString("(*))") == True