#for non-overlapping substring you can simply count the number of occurances using:
#string.count(substring, start(optional), end(optional)

#for overlapping substring:

def overlapCount(string, sub_string):
  count = 0
  string_len = len(string)
  sub_string_len = len(sub_string)
  
  for i in range(string_len):
    if string[i: i+sub_string_len] == sub_string:
      count += 1
      
  return count
