def arithmetic_arranger(problems,cond=None):
  foper = list()
  soper = list()
  oper = list()
  rslt= list()
  fline= ''
  sline= ''
  uline= ''
  rline= ''
  #print(f'len',len(problems))
  if len(problems) > 5:
    return ("Error: Too many problems")

  #Splitting the operands for problem in problems:
  for problem in problems:
    #problem.lstrip()
    #problem.rstrip()
    sproblem= problem.split()
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      return("Error: Numbers cannot be more than four digits")
    if not (sproblem[1]=='+' or sproblem[1]== '-'):
      return("Error: Operator must be '+' or '-'.")
    foper.append(sproblem[0])
    oper.append(sproblem[1])
    soper.append(sproblem[2])


  counter=0
  while counter< len(problems):
    try:
      x= int(foper[counter])
      y= int(soper[counter])
    except:
      return("Error: Numbers must only contain digits")
    #arithmetic operations
    if oper[counter]== '+':
      sumas=x+y
      rslt.append(sumas.__str__())
    elif oper[counter]=='-':
      restas=x-y
      rslt.append(restas.__str__())

    #Finding lenght of longest operand
    length=max(len(foper[counter]),len(soper[counter]))


    #first line
    for val in range((length+2)-len(foper[counter])):
      foper[counter]=' '+foper[counter]
    fline=fline+foper[counter]+'    '
    #second line
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
    #final output
  fline = fline.rstrip()
  sline = sline.rstrip()
  uline = uline.rstrip()
  rline = rline.rstrip()
  if cond==True:
    arranged_problems=(print(f"{fline}\n{sline}\n{uline}\n{rline}"))
  else:
    arranged_problems=(print(f"{fline}\n{sline}\n{uline}"))

  return arranged_problems

#Test:
arithmetic_arranger(['3801 - 2', '123 + 49'], True)
