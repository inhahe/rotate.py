import sys
inp = ' '.join(sys.argv[1:])
if not inp:
  print("Translates an input phrase into a secret language. Gives up to 23 translations to choose from.")
  print('Usage: python rotate.py "Some input phrase."')
specials = []
inplen = 0
nonspecials = []
for i, x in enumerate(inp):
  if x.isalnum():
    nonspecials += [x]
  else:
    specials += [(i, x)]
lennon = len(nonspecials)
for o in range(-min(11, lennon//2), min(11, lennon//2)+lennon%2):
  output = list(x for x in nonspecials[-o:]+nonspecials[:-o] if x.isalnum())
  for i, x in specials:
    output.insert(i, x)
  for i, x in enumerate(inp):
    if x.isupper():
      output[i]=output[i].upper() 
    elif x.islower():
      output[i]=output[i].lower()
  print(''.join(output))

