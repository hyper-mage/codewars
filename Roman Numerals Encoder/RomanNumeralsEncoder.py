### thoughts ###
# First off each symbol needs its own rule
 # n >= 1000 then M
 # n >= 500 then D
# and so on. For remainder values we'll subtract and re-evaluate
 # 600 gives D then 600-500 gives C resulting in DC
# Since values can only be identical up to 3 times in a row
# we'll need to either lookback or make a new set of checks
# I think a new set of checks will be more readable and efficient
 # so 900 fails for >= 1000 but passes for >= 900 which gives CM
  # I don't really like that but that is my initial thought


def solution(n):
    # TODO convert int to roman string
    rn = ''
    
            
    return