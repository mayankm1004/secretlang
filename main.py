def load_gloss():
  temp1 = []
  temp2 = []
  with open('gloss.txt') as f:
      temp1 = f.readlines()
      f.close()
  for each in temp1:
      each = each[0:-1].split(' ')
      temp2.append(each)
  return temp2        

def load_words(x):
  words = []
  for each in x:
      words.append(each[0])
  return words

while 1:
  lines = load_gloss()
  words = load_words(lines)
  print('''
What would you like to translate?''')
  translate = input('  > ')
  translate = translate.lower()
  translate = list(translate)
  translate = ''.join(c for c in translate if c in 'abcdefghijklmnopqrstuvwxyz ')
  translate_temp = translate
  translate = translate.split(' ')
  finished = []
  for each in translate:
      if each in words:
          pass
      else:
          expand = input('  Translate "' + each + '" > ')
          with open("gloss.txt", "a") as myfile:
              myfile.write(each + ' ' + expand + ' \n')
              myfile.close()
          lines = load_gloss()
          words = load_words(lines)
  for each in translate:
      for every in lines:
          if each == every[0]:
              finished.append(every[1])
          else:
              pass
  finished = ' '.join(c for c in finished)
  print('  > ' + translate_temp)
  print('  > ' + finished)