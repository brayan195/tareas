
# coding: utf-8

# In[45]:


paquete
__init__.py
modulo.py
modulo1.py
modulo2.py 
modulo3.py
    
    
paquete
__init__.py
modulo1.py
subpaquete 
__init__.py
modulo1.py
modulo2.py
    
modulo1.py
paquete
__init__.py
modulo1.py
subpaquete
__init__.py
modulo1.py
subpaquete
__init__.py
modulo1.py
modulo2.py

#-*- coding: utf-8 -*-
import modulo
import paquete.modulo1
import paquete.subpaquete.modulo

    print modulo.CONSTANTE_1
    print paquete.modulo.CONSTANTE_1
    print paquete.subpaquete.modulo.CONSTANTE_1

    import modulo as m
    import paquete.modulo as pm
    import paquete.subpaquete.modulo as psm
     
print m.CONSTANTE_1
print pm.CONSTANTE_1
print psm.CONSTANTE_1

from paquete.modulo1 import CONSTANTE_1
print CONSTANTE_1
from paquete.modulo1 import CONSTANTE_1, CONSTANTE_2

from paquete.modulo1 import CONSTANTE_1 as C1, CONSTANTE_2 as C2
from paquete.subpaquete.modulo1 import CONSTANTE_1 as CS1, CONSTANTE_2 as CS2
print C1 
print C2
print CS1
print CS2

from paquete.modulo1 import *
print CONSTANTE_1
print CONSTANTE_2





