import pytest
import src.factorial as f # Importamos la función que aún no hemos creado

'''Para comprobar el ejercicio hay que ir comentando y descomentando codigo segun las 
instrucciones de los comentarios'''

# Definiciones para el Test 1
def test_factorial_1_pasa():
    f.Factorial.factorial(1)
        
def test_factorial_1_falla():
    with pytest.raises(AttributeError):
        f.Factorial.factorial(1)
    
# Test 2    
def test_tipo_falla():
    assert f.Factorial.factorial("d")==1
    
def test_tipo_pasa():
    assert f.Factorial.factorial(1)==1
    
#Test 3
def test_negativo_pasa():
    f.Factorial.factorial(-1)
        
def test_negativo_falla():
    with pytest.raises(f.Negativo):
        f.Factorial.factorial(-1)
        
#Test 4
def test_positivo_falla():
    assert f.Factorial.factorial(4)==20
    
def test_positivo_pasa():
    assert f.Factorial.factorial(4)==24