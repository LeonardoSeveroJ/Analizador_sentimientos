from textblob import TextBlob
pos_count =0
pos_correct=0

with open("positivas.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis= TextBlob(line)
        #print(line)
        try:
            eng=analysis.translate(to='en')
            if eng.sentiment.polarity>0:
                pos_correct += 1
            pos_count += 1
        except:
            #mostramos este mensaje en caso de que se presente algun problema
            print("El elemento no esta presente")

neg_count =0
neg_correct =0

with open("negativas.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis= TextBlob(line)
        #print(line)
        try:
            eng=analysis.translate(to='en')
            if eng.sentiment.polarity>0:
                neg_correct += 1
            neg_count += 1
        except:
            #mostramos este mensaje en caso de que se presente algun problema
            print("El elemento no esta presente")


print("Precision positviva= {}% via  {} ejemplos".format(pos_correct/pos_count*100.0, pos_count))
print("Precision negativa= {}% via  {} ejemplos".format(neg_correct/neg_count*100.0, neg_count))
                                                      

                
        
