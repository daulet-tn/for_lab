#1
import re 
da = r'ab*'
text = ["a", "ab", "abbb", "anbisnin", "abc", "abbbb"]
for i in text:
    match = re.fullmatch(da, i)
    print(bool(match))
#2
x = r'ab{2,3}'
for i in text:
    match = re.fullmatch(x, i)
    print(bool(match))
#3
text1 = "full_gol high_lou toyyyy"
z = r'[a-z]+_[a-z]+'
print(re.findall(z, text1))
#4
text2 = "Hello World Python RegEx test"
print(re.findall(r'[A-Z][a-z]+', text2))
#5
s = r'a.*b'
for i in text:
    print(re.fullmatch(s, i))

