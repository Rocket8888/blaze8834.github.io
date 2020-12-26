import urllib
(fn,hd) = urllib.urlretrieve('https://blaze8834.github.io/games/basic.py')
execfile(fn)
x = "a"
input("I suck at python. Do you?")
answer = x
if x == "yes":
  print("Good, I'm not alone!")
if x == "no":
  print("I'm lonely...")
