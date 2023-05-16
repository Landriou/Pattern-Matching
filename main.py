from patternmaching import *
from matchingalgorythms import *
print("Ejercicio 1")
print(existChar("Hola","o"))
print(existChar("Hola","f"))
print("Ejercicio 2")
print(isPalindrome("a colima va mi loca"))
print(isPalindrome("anitalavalatina"))
print(isPalindrome("radar"))
print(isPalindrome("holo"))

# print("")
# ss = stringCompresor("aabcccccaaa")
# print(ss)
# s2 = stringCompresor("abc")
# print(s2)
# print("")
print("Ejercicio 3")
s1 = "ossooooossso"
s3 = "holaaaaa"
print(mostRepeatedChar(s1))
print(mostRepeatedChar(s3))
print("Ejercicio 4")
print(getBiggestIslandLen("cdaaaaaasssbbb"))

print("Ejercicio 5")
print(isAnagram("hola","ah1l"))

print(isAnagram("hola","ahol"))
print("Ejercicio 6")
print(verifyBalancedParentheses("(ccc(ccc)cc((ccc(c))))"))
print(verifyBalancedParentheses(")ccc(ccc)cc((ccc(c)))("))

print("Ejercicio 7")
print(reduceLen("aaabccddd"))

print("Ejercicio 8")
print(isContained("aaafffmmmarillzzzllhooo","amarillo"))
print(isContained("aaafffmmmarrrilzzzhooo","amarillo"))
print(isContained("aaaaillllfffzzzhrmmmooo","amarillo"))
print("Ejercicio 9")
print(isPatternContained("cabccbacbacab","ab#ba#c","#"))




print(Compute_Prefix("ababaca"))
print(KMPMatcher("bacbabababacabbbbbb","ababaca"))

print(KMPMatcherSinSolap("bacbabacabacabbbbbb","aba"))

Imprimirmatriz(TransitionFunction("ababaca","abababacaba"))
print(AEFMatcher("abababacaba","ababaca"))
print(Rabin_Karp("abababacaba","ababaca"))