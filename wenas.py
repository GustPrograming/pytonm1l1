meme_dict = {
            "PERRO": "Animal doméstico fiel y amigable que suele ladrar.",
            "GATO": "Animal doméstico independiente y ágil que suele maullar.",
            }
word = input("Escribe una mascota ( perro o gato),  (¡con mayúsculas!): ").lower()
if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("PALABRA NO RECONOCIDA")

