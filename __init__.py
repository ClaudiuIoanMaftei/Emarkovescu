import Markov, Corpus
import re

def versify(line):
    new_line = ""
    first=True
    for token in line.split(" "):
        if token[0].isalpha() and token[0].isupper():
            if not first:
                new_line += "\n"
            else:
                first=False
        new_line += token + " "

    return new_line

def count_rhymes(lines):
    rhymes = {}
    if isinstance(lines,str):
        lines=lines.split("\n")

    for line in lines:
        try:
            margin=0
            while(True):
                if line[-1-margin].isalpha() and (line[-2-margin].isalpha() or line[-2-margin].isspace()):
                    key=line[-2-margin]+line[-1-margin]
                    if key in rhymes:
                        rhymes[key]+=1
                    else:
                        rhymes[key]=0
                    break
                else:
                    margin+=1
        except:
            print(line)
    return rhymes

def generate_versified_sentence():
    while (True):
        line = Markov.model.make_sentence()
        line = versify(line)
        rhymes = count_rhymes(line)
        if max([rhymes[key] for key in rhymes.keys()]) > 0:
           return line

def generate_stanzas_random(amount=3):
    result=""
    for i in range(amount):
        result+=generate_versified_sentence()+'\n\n'

    return result


if __name__ == '__main__':
    Markov.load_model()

    print(generate_stanzas_random())


