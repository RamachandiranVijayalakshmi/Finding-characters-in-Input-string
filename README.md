## Mix string in the characters
- We actually Given 2 strings, s1, and s2 
- Return a new string made of the first, middle and last char each input string
## Sample code to check First,Middle,Last characters in The input string
```sh
  resultString = s1[:1] + s2[:1] + s1[int(len(s1) /2):int(len(s1) /2)+1] +s2[int(len(s2) /2):int(len(s2) /2)+1] +s1[len(s1)-1] + s2[len(s2)-1]
  print("Mix String is ", resultString)
 ```
 ## Expected Output
 Mix String is  AJrpan
 
