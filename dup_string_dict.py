#!/usr/bin/env python3 
def duplicate_count(text):
    text_lc = text.lower()
    count = {}
    for letter in text_lc:
      if letter in count:
        count[letter] += 1
      else:
        count[letter] = 1
    total = print(sum(1 for i in count.values() if i >= 1))
    return total
      
def main():
  text = "mississippiBB"
  duplicate_count(text)
  
if __name__ == "__main__":
    main()