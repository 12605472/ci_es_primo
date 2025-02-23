class Negativo(Exception):
    pass


class Factorial(object):
    # 1.- Test que fallen, todo el codigo comentado. ESTE SERIA EL PRIMER CICLO


    # AHORA COMENZAMOS EL CICLO SEGUNDO
    # 2.- Test acerca del tipo de datos del parametro.
    '''def factorial(n):
        return n*1'''
    
    # 3.- Test con un número negativo
    '''def factorial(n):
        if (n < 0):
            raise Negativo('Tiene que ser un número positivo')
        return 1'''
    
    # 4.- Test con número positivo.
    '''def factorial(n):
        if (n < 0):
            raise Negativo('Tiene que ser un número positivo')   
        if n==0:
            return 1     
        return n * Factorial.factorial(n-1)'''
    

# ULTIMO CICLO REFACTORIZACION
    def factorial(n):
        if n <= 1:
            return 1
        return n * Factorial.factorial(n-1)