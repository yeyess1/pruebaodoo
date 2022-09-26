#orden de Palabras

def amount_words(text):
    amount = []
    words =''.join([i for i in text if not i.isdigit()]) #excluir los numeros del array 
    words = words.split()
    arr1 = []
    arr2 = [] 
    for j in range(0, len(words)):
        for k in range(1, len(words)):
            if words[j] not in arr1:
                if words[j]==words[k]:
                    arr1.append(words[j])
                elif words[k] not in arr2:
                    arr2.append(words[k])
    for i in arr2:
        amount.append(arr1.count(i)+1)#contar la cantidad de elemenetos repetidos
        
    return(print("",len(arr1),"\n", " ".join(map(str, amount))))

prueba= "4 abc abcdefg abc bcdefg abcdefg"
amount_words(prueba)




       
