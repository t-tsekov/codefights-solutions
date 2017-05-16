def amendTheSentence(s):
   res = ""
   for i in range(len(s) - 1):
      res += s[i].lower()
      if s[i+1].isupper():
         res += " "
   res += s[-1].lower()
   return res