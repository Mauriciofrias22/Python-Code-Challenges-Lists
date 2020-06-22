#function append_sum has a list as a parameter
def append_sum(lst):

#The function add the last two elements of lst together
#and append the result to lst

  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])

#then the function returns lst

  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
