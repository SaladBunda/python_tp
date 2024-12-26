def est_palindrome(s):
    i = 0
    while(i < len(s)/2):
        print(s[i],s[len(s) - i - 1])
        if(s[i] == s[len(s) - i - 1]):
            i+=1
        else:
            return False
    return True

print(est_palindrome("a"))