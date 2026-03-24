import sys
def help():
  print("Translates an input phrase into a secret language. Gives up to N translations to choose from.")
  print("Usage: python rotate.py <text to translate> [number of translations to give]")
  print("number of translations to give defaults to 23.")
  exit()
if len(sys.argv)==1:
  help()
else:
  inp = sys.argv[1]
  if len(sys.argv)==3:
    try:
      n = int(sys.argv[2])
    except:
      help()
  elif len(sys.argv)>3:
    help()
  elif len(sys.argv)==2:
    n = 23    
specials = []
inplen = 0
nonspecials = []
for i, x in enumerate(inp):
  if x.isalnum():
    nonspecials += [x]
  else:
    specials += [(i, x)]
lennon = len(nonspecials)
mn = -min(n//2, lennon//2)
mx = min(-mn+n%2, lennon)
for o in range(mn, mx):
  output = list(x for x in nonspecials[-o:]+nonspecials[:-o] if x.isalnum())
  for i, x in specials:
    output.insert(i, x)
  for i, x in enumerate(inp):
    if x.isupper():
      output[i]=output[i].upper() 
    elif x.islower():
      output[i]=output[i].lower()
  print(''.join(output))

