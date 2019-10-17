# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.


def count_code(str):
  count= 0
  for n in range(65,255):
    word = 'co'+chr(n)+'e'
    if str.count(word) > 0:
      count+= str.count(word)
  return count

print(count_code('cozexxcope'),
      count_code('aaacodebbb'),
      count_code('codexxcode'))


