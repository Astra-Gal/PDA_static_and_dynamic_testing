### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#needs to import Card class

class CardGame:
#needs a def __init__ passing in self and any other parameters needed


  def check_for_ace(self, card):
    if card.value = 1:
    # in line 24, it should be == not =
      return True
    else
    # line 27 needs a colon after the else
      return False
   
# typo - dif should be def, and there should be a comma between card1 and card2
  dif highest_card(self, card1 card2):
#line 34 should be indented
  if card1.value > card2.value:
    return card
    # line 35 should return card1
  else:
    return card2
  


def cards_total(self, cards):
  total
  #line 43 should set the variable total to zero to start with
  for card in cards:
    total += card.value
    return "You have a total of" + total
# string formatted incorrectly. Line 47 should be:
# return f"You have a total of {total}"
  
```
