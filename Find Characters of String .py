def mixString(s1, s2):
  resultString = s1[:1] + s2[:1] + s1[int(len(s1) /2):int(len(s1) /2)+1] +s2[int(len(s2) /2):int(len(s2) /2)+1] +s1[len(s1)-1] + s2[len(s2)-1]
  print("Mix String is ", resultString)
  
s1 = "America"
s2 = "Japan"
mixString(s1, s2)
