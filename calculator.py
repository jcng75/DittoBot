from math import log, sqrt
from re import compile 
from utility import replace_function
from numpy import pi, e

def calc(string):
  fix_list = {"x":"*", "^": "**", "=": "=="}
  new_string = replace_function(string, fix_list)
  prog = compile(r"[a-zA-Z]+")
  check_list = prog.findall(new_string)
  suitable_words = ["log", "sqrt", "pi", "e"]
  for pattern in check_list:
    if pattern not in suitable_words:
      return "Invalid expression!"
  try:
    return eval(new_string)
  except:
    return "Invalid expression!"