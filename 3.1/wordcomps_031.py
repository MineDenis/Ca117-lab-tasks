import sys

def most_e(line):
    words_with_e = [i for i in line if 'e' in i]
    most_es = 0
    for i in line:
        if most_es < i.count('e'):
            most_es = i.count('e')
    return [i for i in line if i.count('e') == most_es]

def vowels(l):
   new = []
   final = []
   vow = "aeiou"
   for word in line:
      count = 0
      for char in word:
         if char.lower() in vow:
            count += 1
            vow = vow.replace(char.lower(), "", 1)
      new.append(count)
      vow = "aeiou"
   for value in range(len(new)):
      if new[value] == 5:
         final.append(l[value].strip())
   return final

def main():
    global line
    line = []
    for lines in sys.stdin:
        line.append(lines.strip())

    print("Words containing 17 letters: {}".format([i for i in line if len(i) == 17]))
    print("Words containing 18+ letters: {}".format([i for i in line if len(i) > 17]))
    print("Shortest word containing all vowels: {}".format(min((x.strip() for x in vowels(line) if x.strip()), key=len)))
    print("Words with 4 a's: {}".format([i for i in line if i.lower().count('a') == 4]))
    print("Words with 2+ q's: {}".format([i for i in line if i.lower().count('q') >= 2]))
    print("Words containing cie: {}".format([i for i in line if "cie" in i]))
    print("Anagrams of angle: {}".format([i for i in line if sorted('angle') == sorted(i.lower()) and i != "angle"]))
    print("Words ending in iary: {}".format(len([i for i in line if "iary" in i])))
    print("Words with most e's: {}".format(most_e(line)))

if __name__ == "__main__":
    main()
