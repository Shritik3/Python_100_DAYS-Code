from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(plain_text, shift_amount,direction):
  cipher_text = ""
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      if direction=='encode':
        new_position = position + shift_amount
      elif direction=='decode':
        new_position = position - shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text+=char
  print(f"The {direction}d text is {cipher_text}")


bool=True
while bool==True:
  direction = input("Type 'encode' to encrypt, type 'decode'       to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(text,shift,direction)
  user_choice=input("Type 'yes' if you want to continue, 'no' if   you want to exit\n") 
  if user_choice=='no':
    bool=False
    print('GoodBye!')
