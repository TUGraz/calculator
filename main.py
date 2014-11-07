#! /usr/bin/python

import sys

class Calculator(object):

  def __init__(self, input):
    self.input = input

  def is_number(self, value):
    try:
      int(value)
    except:
      return False
    return True

  def check_input_size(self):
    is_input_correct = False
    if len(self.input) >= 4:
      if (len(self.input) - 1) % 2 == 1: #2 + 3 + 3 sollten 3 zahlen sein!
        is_input_correct = True
      else:
        raise TypeError("ERROR: Wrongly formatted input!")
    else:
      raise Exception("ERROR: Minimum Input: Number Operator Number!")
    return is_input_correct

  def check_computability(self):
    is_input_number_OK = True
    is_input_operator_OK = True
    is_prev_operator_div = False
    counter = 1

    for argument in self.input[1:len(self.input)]:
      if counter % 2 == 1:
        if self.is_number(argument):
          if is_prev_operator_div == True:
            is_prev_operator_div == False
            if int(argument) == 0:
              raise ValueError("ERROR: Caught division by zero!")
            pass
        else:
          raise ValueError("ERROR: Input number could not be parsed!")
      else:
        if argument != "+" and argument != "-" and argument != "*" and argument != "/":
          raise TypeError("ERROR: Wrongly formatted input!")
        elif argument == "/":
          is_prev_operator_div = True
      counter += 1

  def calculation(self):
    overflow_number = 10000000.0
    finish_number = 0
    list_numbers = []
    list_operations = []
    counter = 1
    for argument in self.input[1:len(self.input)]:
      if counter % 2 == 1:
        list_numbers.append(int(argument))
      else:
        list_operations.append(argument)
      counter += 1
    
    finish_number = list_numbers[0]
    iterator_number = 1
    iterator_operator = 0
    while iterator_number < len(list_numbers):
      if list_operations[iterator_operator] == "+":
        finish_number = self.add(finish_number,list_numbers[iterator_number])
      elif list_operations[iterator_operator] == "-":
        finish_number = self.sub(finish_number,list_numbers[iterator_number])
      elif list_operations[iterator_operator] == "*":
        finish_number = self.mul(finish_number,list_numbers[iterator_number])
      elif list_operations[iterator_operator] == "/":
        finish_number = self.div(finish_number,list_numbers[iterator_number])

      if finish_number > overflow_number or finish_number < -overflow_number:
        raise Exception("ERROR: Result too large! Overflow encountered.")

      print(finish_number)

      iterator_number += 1
      iterator_operator += 1

  def add(self,x,y): 
    c = x + y
    return c
    
  def sub(self,x,y): 
    c = x - y
    return c
    
  def mul(self,x,y): 
    c = x * y 
    return c
    
  def div(self,x,y):
    c = x / y
    return c

  def process_input(self):
    self.check_input_size()
    self.check_computability()
    self.calculation()

  def __del__Calculator(self):
    print("Destruktor gestartet")

def main():
  x=Calculator(sys.argv)
  try:
    x.process_input()
    del x
    sys.exit(0)
  except Exception as err:
    print(err)
    del x
    sys.exit(-1)

if __name__ == "__main__":
  main()
