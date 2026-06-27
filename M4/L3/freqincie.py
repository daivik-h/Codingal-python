word_counts = {'Codingal': 3,'is': 2,'best': 2,'for': 2,'Coding': 1}

print("The og dictnorie  : " +  str(word_counts))
   
K = 2
  
res = 0
for key in word_counts:
    if word_counts[key] == K:
        res = res + 1
      
print("Frequency of K is : " + str(res))

