s = 'askdas24'

print(s[2:4]) #menghasilkan “kd”, sama dengan s[2:4:1]
print(s[2:6:2]) #menghasilkan “ka”
print(s[::]) #menghasilkan “askdas24”, sama dengan s[0:len(s):1]
print(s[::-1]) #menghasilkan “42sadksa”, sama dengan s[-1:-(len(s)+1):-1]
print(s[4:1:-2]) #menghasilkan “ak”
