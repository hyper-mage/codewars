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
  # I feel like there is a more clever way to pull that off

# NOTE: this will only work up to 3999 per the description rules
# 4000 will give MMMM which is not right

# first submit failed 3 tests all ending in 89
    # looks like i did the sub rules wrong for 5
    # and probably 50 and 500 too if i had to guess
    # nope it was literally a typo VX instead of IV...

def solution(n):
    # TODO convert int to roman string
    rn = ''
    while n != 0:
        if n >= 1000:
            rn += 'M'
            n -= 1000
        elif n >= 500:
            if n >= 900:
                rn += 'CM'
                n -= 900
            else:
                rn += 'D'
                n -= 500
        elif n >= 100:
            if n >= 400:
                rn += 'CD'
                n -= 400
            else:
                rn += 'C'
                n -= 100
        elif n >= 50:
            if n >= 90:
                rn += 'XC'
                n -= 90
            else:
                rn += 'L'
                n -= 50
        elif n >= 10:
            if n >= 40:
                rn += 'XL'
                n -= 40
            else:
                rn += 'X'
                n -= 10
        elif n >= 5:
            if n >= 9:
                rn += 'IX'
                n -= 9
            else:
                rn += 'V'
                n -= 5
        elif n >= 1:
            if n >= 4:
                rn += 'IV'
                n -= 4
            else:
                rn += 'I'
                n -= 1     
    return rn