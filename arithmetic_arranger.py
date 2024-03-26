def arithmetic_arranger(problems,cond=None):
  '''
  @DESCRIPTION:  This function takes a list of arithmetic problems as strings and an optional boolean argument cond. The function performs the following tasks:
  It splits the arithmetic problems into operands and operators.
  It checks for errors in the problems, such as numbers having more than four digits or the operator not being "+" or "-".
  It performs the requested arithmetic operations and formats the results into a neat layout.
  It returns a string containing the arithmetic problems, each on a separate line, with the operands right-aligned, the operator left-aligned, and a line of dashes beneath the operands. If cond is True, it also includes an additional line with the results of the operations.
  In case errors are found in the problems or if there are more than five problems, the function returns a corresponding error message

  '''
  #Initialize variables 
  foper = list()
  soper = list()
  oper = list()
  rslt = list()
  fline= ''
  sline= ''
  uline= ''
  rline= ''

  #Define ERROR: TOO MANY PROBLEMS
  if len(problems) > 5:
    return ("Error: Too many problems.")

  #Splitting the operands for problem in problems:
  for problem in problems:
    sproblem= problem.split()
    #Define ERROR: DIGITS QUANTITY
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      return("Error: Numbers cannot be more than four digits.")
    #Define ERROR: OPERATOR DIFFERENT TO "+" OR "-"
    if not (sproblem[1]=='+' or sproblem[1]== '-'):
      return("Error: Operator must be '+' or '-'.")
    #Adding the operands and operators to the proper list: foper=upper value, oper=operator and soper=lower value
    foper.append(sproblem[0])
    oper.append(sproblem[1])
    soper.append(sproblem[2])

  #Set the counter as 0 to stablish it as index first position
  counter=0
  while counter< len(problems):
    #Define ERROR: ONLY INT DIGITS
    try:
      x= int(foper[counter])
      y= int(soper[counter])
    except:
      return("Error: Numbers must only contain digits.")
    #Arithmetic operations
    if oper[counter]== '+':
      sumas=x+y
      rslt.append(str(sumas))
    elif oper[counter]=='-':
      restas=x-y
      rslt.append(str(restas))

    #Finding lenght of longest operand
    length=max(len(foper[counter]),len(soper[counter]))


    #first line: uper values
    for val in range((length+2)-len(foper[counter])):
      foper[counter]=' '+foper[counter]
    fline=fline+foper[counter]+'    '
    #second line: second value and operator 
    for val in range((length+1)-len(soper[counter])):
      soper[counter]=' '+soper[counter]
    sline=sline+oper[counter]+soper[counter]+'    '
    #underscore line
    for val in range (length+2):
      uline=uline+'-'
    uline=uline+'    '
    #result line
    for val in range((length+2)-len(rslt[counter])):
      rslt[counter]=' '+rslt[counter]
    rline=rline+rslt[counter]+'    '
    counter=counter+1

  #final output: strip the last values of each line from the right spaces
  fline = fline.rstrip()
  sline = sline.rstrip()
  uline = uline.rstrip()
  rline = rline.rstrip()

  #condition to show result line
  if cond==True:
    arranged_problems=fline+'\n'+sline+'\n'+uline+'\n'+rline
  else:
    arranged_problems=fline+'\n'+sline+'\n'+uline

  return arranged_problems

#Test:
arithmetic_arranger(['3801 - 2', '123 + 49'], True)
