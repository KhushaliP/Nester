#This is a code to print items in a list
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
 ["Graham Chapman", ["Michael Palin", "John Cleese",
 "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#the function print_lil is a recursive function in order to
#find lists within lists and print them
def print_lil(the_list):
       for each_item in the_list:
              if isinstance(each_item, list):
                     print_lil(each_item)
              else:
                     print(each_item)


 	      


