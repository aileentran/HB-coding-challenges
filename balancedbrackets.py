"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    # code thoughts 
    # input: a string
    # output: boolean. true - balanced AND in the right order OR no brackets; false otherwise 

    # do a bunch of false conditions
    # else true? 

    # stack?? or just a plain old list 

    # how do I look at it? look at beginning and end. loop with 
    # first bracket i encounter at the beginning should be the first at the end. vis versa 
    # two unnested for loops? 
    # ooorrrr one loop and somehow point at both beginning and end at the same time? 

    # do two nested for loops for now. 

    for idx,char in enumerate(phrase):
      print('idx', idx)
      
      last = phrase[-(idx + 1)]
        
      print('char', char)
      print('last', last)
      # print('last', last)



# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
