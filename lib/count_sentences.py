#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self._value = value
  
  def set_value(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")
    
  def get_value(self):
    return self._value
    
  value = property(get_value, set_value)
    
  def is_sentence(self):
    return True if self._value.endswith('.') else False

  
  def is_question(self):
    return True if self._value.endswith('?') else False

  
  def is_exclamation(self):
    return True if self._value.endswith('!') else False
  
  def count_sentences(self):
    i = 0
    for val in self._value.split():
      if val.endswith('.') or val.endswith('!') or val.endswith('?'):
        i += 1
    return i
    
