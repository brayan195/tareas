
# coding: utf-8

# In[2]:


def mi_funcion():
    # aqui el algoritmo



# In[48]:


def mi_funcion():
    print ("Hola mundo")
    funcion()
def funcion():
    return "Hola mundo"
frase=funcion()
print(frase)


# In[5]:


def mi_funcion(nombre, apellido):
    # algoritmo
    


# In[9]:


def mi_funcion(nombre, apellido):
nombre_completo= nombre, apellido
print (nombre_completo)


# In[37]:


def saludar(nombre, mensaje='Hola'):
    print (mensaje, nombre)
    
    saludar("pepe grillo")


# In[39]:


def saludar(nombre, mensaje='Hola'):
      print (mensaje, nombre)
        saludar (mensaje="buen dia", nombre="juancho")


# In[44]:


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print (parametro_fijo)
     for argumento in arbitrarios:
            print (argumento)
    recorrer_parametros_arbitrarios('fixed','arbitrario 1', 'arbitrario 2', 'arbitrario 3')


# In[ ]:


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print (parametro_fijo) 
    for argumento in arbitrarios:
        print(argumento)
for clave in kwords
 print ("El valor de", clave,  "es", kwords[clave])
    recorrer_parametros_arbitrarios("fixed", "arbitrarios 1", "arbitrarios 2", "arbitrarios 3", cave1="valor uno",
                                   clave2="valor dos")


# In[46]:


def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos =[1500, 10]
print (calcular (*datos))


# In[47]:


def funcion():
    return "Hola mundo"

def saludar(nombre, mensaje='hola'):
    print (mensaje, nombre)
    print (mi_funcion())
    


# In[50]:


def funcion():
    return "Hola mundo"

def llamada_de_retorno(func=""):
    """llamada de retorno anivel"""
    return globals()[func]()
print (llamada_de_retorno("funcion"))
nombre_de_la_funcion="funcion"
print (locals()[nombre_de_la_funcion]())


# In[51]:


def funcion(nombre):
    return "Hola " + nombre


def llamada_de_retorno(func=""):
    """llamada de retorno a nivel global"""
    return globals()[func]("Laura")

print (llamada_de_retorno("funcion"))

# llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"
print(locals()[nombre_de_la_funcion]("facundo"))


# In[52]:


if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print(locals()[nombre_de_la_funcion]("Emlse"))
        
        


# In[55]:


def funcion(nombre):
    return "Hola " + nombre

def llamada_de_retorno(func=""):
    if func in globals():
        if callable(globals()[funcion]):
            return globals()[func]("Laura")
        else:
            return "funcion no encontrada"
        
        print(llamada_de_retorno("funcion"))
        
        nombre_de_la_funcion = "funcion"
        if nombre_de_la_funcion in locals():
            if callable(locals()[nombre_de_la_funcion]):
                print(locals()[nombre_de_la_funcion]("facundo"))
                
                else:
                    print("funcion no encontrada")
        


# In[56]:


def jugar(intento=1):
    respuesta = raw_input("¿De que color es una naranja")
    if respuesta != "naranja":
        if intento < 3:
            print("\nperdiste!")
        else:
            print("\nGanaste!")
    jugar()      
    

