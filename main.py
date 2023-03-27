def caesar(message, key, mode):
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  translated = ''
  message = message.upper()

  if key > 25 or key < 1:
    print("Invalid Key")
  else:
    for letter in message:
      temp_letter = letters.find(letter)
      
      if mode == 'encrypt':
        temp_letter += key
  
      elif mode == 'decrypt':
        temp_letter -= key
  
      else:
        print("Invalid mode")

      if temp_letter >= len(letters):
        temp_letter -= len(letters)

      elif temp_letter <= 0:
        temp_letter += len(letters)
        
      translated += letters[temp_letter].lower()

  return translated

result = caesar('nathan', 20, 'encrypt')

print(result)