#!/usr/bin/env python3 

#def duplicate_count(text):
#    total = 0
#    count = []
#    for letter in text:
#        count = text.count(letter)
#        if count > 1:
#            total += count
#            break
#    if total > 0:
#        print(total)
#    elif total < 1:
#        print(total)

def duplicate_count(text):
    count = {}
    for letter in text:
      if letter in count:
        count[letter] += 1
      else:
        count[letter] = 0

    for key in count:
      if count[key] > 1:
          break
    
    total = sum(1 for i in count.values() if i >= 2)
    print(total)
        

def main():
    text = "abcdeee"
    duplicate_count(text)
    

if __name__ == "__main__":
    main()