#There is a price in cents, program will tell how many coins minimal coins is need to price.


def num_coins(cents):
  coins = [25, 10, 5, 1]
  temp = 0
  numberofcoins = 0
  while True:
    for coin in coins:
      if coin + temp < cents:
        temp += coin
        numberofcoins += 1
        while True:
          if coin + temp < cents:
            temp += coin
            numberofcoins += 1
          elif coin + temp == cents:
            temp += coin
            numberofcoins += 1
            return print(numberofcoins)
          else:
            break
      elif temp + coin == cents:
        temp += coin
        numberofcoins += 1
        return print(numberofcoins)

num_coins(100)



