frase_input = str(input("Tu frase para invertir:"))
frase2 = frase_input.split()

frase2.reverse()

frase_output = ' '.join(frase2)
print(frase_output)