def roman_to_int(s: str) -> int:
    roman_num = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }
    ans = 0
    i = 0
    while i < len(s) - 1:
        num1 = roman_num[s[i]]
        num2 = roman_num[s[i + 1]]
        if num1 >= num2:
            ans += num1
            if i == len(s) - 2:
                ans += num2
            i += 1
        else:
            ans += num2 - num1
            i += 2
            if i == len(s) - 1:
                ans += roman_num[s[-1]]
            print(i)
    return ans
