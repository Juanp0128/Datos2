import random
import re

class BadwordsFilter(object):
    def __init__(self, filtro, ignore_case=True, reemplazo="****",
                 completar=True, palabras=False):


        self.badwords = filtro
        self.ignore_case = ignore_case
        self.reemplazo = reemplazo
        self.completar = completar
        self.palabras = palabras

    def limpiar(self, length):

        return ''.join([random.choice(self.reemplazo) for i in
                  range(length)])

    def replacer(self, igual):
        value = igual.group()
        if self.completar:
            return self.limpiar(len(value))
        else:
            return value[0]+self.limpiar(len(value)-2)+value[-1]

    def cambiar(self, texto):
        #Cambia el String desde una mala palabra.

        regexp_insidewords = {
            True: r'(%s)',
            False: r'\b(%s)\b',
            }

        regexp = (regexp_insidewords[self.palabras] %
                  '|'.join(self.badwords))

        r = re.compile(regexp, re.IGNORECASE if self.ignore_case else 0)

        return r.sub(self.replacer, texto)



'''if __name__ == '__main__':

    f = BadwordsFilter(['aguacate', 'gono\w+','\w+rr','\w+norr\w+'], reemplazo="*")
    texto = input('Ingrese sus vulgaridades: ')

    print (f.cambiar(texto))

    f.palabras = True
    print (f.cambiar(texto)'''


