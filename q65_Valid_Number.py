import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input)
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input
        if currentState not in [3,5,8,9]:
            return False
        return True

    def isNumber1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except:
            return False
        return True

    def isNumber2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if re.match("[\s\.+-]*\d+", s)==None:
            return False
        pattern = "\s*[+-]?\d*\.?\d*(e)?(?(1)[+-]?\d+\s*$|\s*$)"
        return re.match(pattern, s)!=None


    def isInteger(self, s):
        if s:
            if s[0] == '-' or s[0] == '+':
                return self.isPureInteger(s[1:])
            else:
                return self.isPureInteger(s)
        else:
            return False

    def isPureInteger(self, s):
        if s:
            for c in s:
                if c not in set("0123456789"):
                    return False
            return True
        else:
            return False

    def isFloat(self, s):
        if not s: return False

        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if not s: return False
        if s == '.': return False

        pos_dot = -1

        for (i, c) in enumerate(s):
            if c in set("0123456789"):
                pass
            elif c == '.':
                if pos_dot >= 0:
                    return False
                else:
                    pos_dot = i
            else:
                return False
        return True

    def isNumber3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()

        n = len(s)
        if n == 0: return False

        pos_e = -1
        for (i, c) in enumerate(s):
            if c == 'e':
                if pos_e >= 0:
                    return False
                else:
                    pos_e = i

        if pos_e >= 0:
            return self.isFloat(s[:pos_e]) and self.isInteger(s[pos_e + 1:])
        else:
            return self.isFloat(s)


