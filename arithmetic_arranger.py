def arithmetic_arranger(problems, k=False):
  def SwitchExample(argument):
    switcher = {
      4: "------",
      3: "-----",
      2: "----",
      1: "---"
    }
    return switcher.get(argument, "")

  arranged_problems = ""
  f1 = ""
  f2 = ""
  f3 = ""
  f4 = ""
  if (len(problems) > 5):
    return "Error: Too many problems."
  b = problems
  for a in b:
    a = a.split(" ")
    # a[0]=int(a[0])
    # a[2]=int(a[2])
    if (a[1] != "+" and a[1] != "-"):
      return "Error: Operator must be '+' or '-'."
    elif ((not a[0].isdecimal()) or (not a[2].isdecimal())):
      return "Error: Numbers must only contain digits."
    elif (len(a[0]) > 4 or len(a[2]) > 4):
      return "Error: Numbers cannot be more than four digits."
  count = 1
  for a in b:
    a = a.split(" ")

    if (len(a[0]) > len(a[2])):
      if (count == len(b)):
        f1 = f1 + a[0].rjust(len(a[0]) + 2)
        f2 = f2 + a[1] + a[2].rjust(len(a[0]) + 1)
        f3 = f3 + SwitchExample(max(len(a[0]), len(a[2])))
        count += 1
      else:
        f1 = f1 + a[0].rjust(len(a[0]) + 2) + "    "
        f2 = f2 + a[1] + a[2].rjust(len(a[0]) + 1) + "    "
        f3 = f3 + SwitchExample(max(len(a[0]), len(a[2]))) + "    "
        count += 1
    else:
      if (count == len(b)):
        f1 = f1 + a[0].rjust(len(a[2]) + 2)
        f2 = f2 + a[1] + a[2].rjust(len(a[2]) + 1)
        f3 = f3 + SwitchExample(max(len(a[0]), len(a[2])))
        count += 1
      else:
        f1 = f1 + a[0].rjust(len(a[2]) + 2) + "    "
        f2 = f2 + a[1] + a[2].rjust(len(a[2]) + 1) + "    "
        f3 = f3 + SwitchExample(max(len(a[0]), len(a[2]))) + "    "
        count += 1

  arranged_problems = f1 + "\n" + f2 + "\n" + f3
  if (k == True):
    count2 = 1
    for a in b:
      a = a.split(" ")

      n1 = int(a[0])
      n2 = int(a[2])
      if (a[1] == "+"):
        result = str((n1 + n2))

      else:
        result = str((n1 - n2))
      if (count2 == len(b)):
        f4 = f4 + result.rjust(max(len(a[0]), len(a[2])) + 2)
      else:
        f4 = f4 + result.rjust(max(len(a[0]), len(a[2])) + 2) + "    "
        count2 = count2 + 1
    arranged_problems = f1 + "\n" + f2 + "\n" + f3 + "\n" + f4

  return arranged_problems
