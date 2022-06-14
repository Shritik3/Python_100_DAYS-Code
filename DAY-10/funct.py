def format_name(f_name,l_name):
    fn=f_name.title()
    ln=l_name.title()
    # print(f"{fn}{ln}")
    return f"{fn} {ln}"
# s=format_name("ShrITik","RAJ")
# print(s)
print(format_name("ShrITik","RAJ"))
out=len("Shritik")
print(out)


def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "Not valid inputs."
    fn=f_name.title()
    ln=l_name.title()
    return f"Result: {fn} {ln}"
print(format_name(input("Enter first name? "),input("Enter last name? ")))






def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  l=is_leap(year)
  if l==True:
    month_days[1]=29
  else:
    month_days[1]=28
  return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




# Docstrings
def format_name(f_name,l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name=="" or l_name=="":
        return "Not valid inputs."
    fn=f_name.title()
    ln=l_name.title()
    return f"Result: {fn} {ln}"






