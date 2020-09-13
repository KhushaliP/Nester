"""This is a code to print items in a list"""


def print_lil(the_list, indent):
       """ the function print_lil is a recursive function in order to
       find lists within lists and print them"""  
       for each_item in the_list:
             if isinstance(each_item, list):
                    print_lil(each_item, indent + 1)

             else:
                     for tab_stop in range(indent):
                            print("\t", end='')
                     print(each_item)

                            
                     



 	      


