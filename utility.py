# The replace function replaces the inputted string with the values in the inputted hastable(fL == fixList)
def replace_function(string, fL):
  checked_string = ""
  for i in range(len(string)):
    if string[i] in fL:
      checked_string += fL[string[i]]
    else:
      checked_string += string[i]
  return checked_string


