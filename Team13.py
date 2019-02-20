#teamname:The Nexus Renegades
#members:Orion Milly, Solbi Jung

####
#teamname:The Nexus Renegades
#
#
#
####
import random 

team_name = 'The Nexus Renegades'
strategy_name =  'Restless Rebellion'
strategy_description = '#1 Always betray(rebell!!!) unless we never had a turn, or have have a safe ground of 800 point because the max points we can get off because of "c" is 800. Since it is hard to get any postive point.'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
      return 'c'
    elif their_history[-1] == 'b':
      return 'b'
    elif their_history[-1] == 'c':
      return 'b'
    elif my_score >= 800:
      return 'c'
    else:
      return 'c'


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed last time, i should betray this time
    if test_move(my_history='bcbc',
              their_history='cccb', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b'):       
      print 'vengeance test successful.'
