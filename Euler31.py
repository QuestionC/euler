# LSD currency problem
currency = {
  1: 0,
  2: 0,
  5: 0,
  10: 0,
  20: 0,
  50: 0,
  100: 0,
  200: 0
}

# How many ways can we make 200 using these denominations?
# We basically need combinations_with_replacement, but we gotta wwrite our own

# Remove coins if we're too high
ways = 0
total_cash = 0

while (True):
  for i in currency:
    if total_cash < 200: break
    total_cash -= currency[i]
    currency[i] = 0
  else:
    # We got to the end of the loop meaning we've exhausted coins
    print ('Total ways: ' + str(ways))
    break

# Now we're too low, so add the next coin tier
  total_cash += i
  currency[i] += i

  if total_cash == 200:
    ways += 1
    print (currency)


