def is_interweaving(s, x, y):
    lx, ly = len(x), len(y)
    comparisons = 0

    while (lx + ly) <= len(s):
        # initialize dp table
        dp = [[False] * (ly+1) for _ in range(lx+1)]

        for i in range(lx+1):
            for j in range(ly+1):
                # two empty strings have an empty string
                # as interleaving
                if (i == 0 and j == 0):
                    dp[i][j] = True
    
                # x is empty
                elif (i == 0):
                    if (y[j - 1] == s[j - 1]):
                        dp[i][j] = dp[i][j - 1]
                
                # y is empty
                elif (j == 0):
                    if (x[i - 1] == s[i - 1]):
                        dp[i][j] = dp[i - 1][j]
                
                # Current character of s matches with
                # current character of x, but doesn't match
                # with current character of y
                elif (x[i - 1] == s[i + j - 1] and
                    y[j - 1] != s[i + j - 1]):
                    dp[i][j] = dp[i - 1][j]
    
                # Current character of s matches with
                # current character of y, but doesn't match
                # with current character of x
                elif (x[i - 1] != s[i + j - 1] and
                    y[j - 1] == s[i + j - 1]):
                    dp[i][j] = dp[i][j - 1]
    
                # Current character of s matches with
                # that of both x and y
                elif (x[i - 1] == s[i + j - 1] and
                    y[j - 1] == s[i + j - 1]):
                    dp[i][j] = (dp[i - 1][j] or dp[i][j - 1])
        if dp[lx][ly]:
            return True
        s = s[1:]

    return False
