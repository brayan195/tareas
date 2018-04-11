
# coding: utf-8

# In[2]:


a, b, c= 'string', 15, 'true' 


# In[4]:


print (a)


# In[5]:


print (b)


# In[6]:


print (c)


# In[8]:


mi_tupla = ('hola mundo', 2011)
texto, anio = mi_tupla 
print (texto)


# In[9]:


print (anio)


# In[10]:


mi_lista = ['Argentina', 'Buenos Aires']
pais, provincia = mi_lista
print (pais)


# In[11]:


print (provincia)


# In[22]:


mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print (mi_tupla[1]) # salida: 15
print (mi_tupla[1:4])# devuelve: (15, 2.8, 'otro dato')
print (mi_tupla [3:])# devuelve ('otro dato', 25)
print (mi_tupla[:2])# devuelve ('cadena de texto', 15)

print (mi_tupla[-1]) # salida: 25 
print (mi_tupla[-2])# salida: otro dato 


# In[24]:


print (mi_lista[1]) # Salida: 15
print (mi_lista[1:4]) # Devuelve: [15, 2.8, 'otro dato']
print (mi_lista [-2]) # Salida: otro dato 


# In[27]:


mi_lista[2] = 3.8 # el tercer elemento ahora es 3.8
mi_lista.append('Nuevo Dato')

