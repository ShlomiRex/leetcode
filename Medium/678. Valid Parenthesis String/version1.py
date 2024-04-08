"""
Time limit exceeded, need to optimize. I think the solution is right though.


First use stack, pop, check element, if '*' we can go wild.

((*))
(*))

Counters: count '(', ')' and '*', use stack/counter to check valid parenthesis without '*'
if not valid we continue to check '*'

Next intuition: count '(', ')' and '*' at each character. 

Im just gonna do decision tree (backtracking / dp)
"""
def checkValidString(s: str) -> bool:
    def backtrack(curr_solution):
        found_star = False
        for i, c in enumerate(curr_solution):
            if c == '*':
                found_star = True
                if backtrack(curr_solution[:i] + '(' + curr_solution[i+1:]) or backtrack(curr_solution[:i] + ')' + curr_solution[i+1:]) or backtrack(curr_solution[:i] + '' + curr_solution[i+1:]):
                    return True
        if not found_star:
            # Check if string is valid
            open_counter = 0
            for c in curr_solution:
                if c == '(':
                    open_counter += 1
                else: # c == ')'
                    if open_counter > 0:
                        open_counter -= 1
                    else:
                        return False
            if open_counter == 0:
                return True
        return False

    return backtrack(s)

if __name__ == "__main__":
    assert checkValidString("()") == True
    assert checkValidString("(*)") == True
    assert checkValidString("()") == True
    assert checkValidString("(*))") == True