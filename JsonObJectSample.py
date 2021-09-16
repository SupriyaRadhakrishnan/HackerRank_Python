def switchItUp(arg):
   sw_case = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday"
   }
   return sw_case.get(arg)

print(switchItUp(3))