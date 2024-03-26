"""Prueba Mercado libre realizada por Miguel Gómez"""


class Buffer(object):
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and
    LIFO (Last In First Out).
    """

    def __init__(self, policy: str):
        policy = policy.upper()
        if policy not in ["FIFO", "LIFO"]:
            raise ValueError()
        self._policy = policy
        self.list_objets = []

  

    def insert(self, item: str) -> None:
        """Inserta un registro en una lista según politica

        Args:
          item: objeto que quieroi agre3gar a la lista

        return:
          no retorna nada
        """

        if self._policy == "FIFO":
          self.list_objets.append(item)
        else:
          self.list_objets.insert(0, item)

    def extract(self):
        """Elimina el registro de la lista

        return:
          item: Se retorna elemento que se elimino

        raise:
          Retorna error cuando se intenta extraer en un buffer vacio
        """

        if not self.list_objets:
          raise IndexError("Buffer is empty")
        elif self._policy == "FIFO":
          return self.list_objets.pop()       
        else:
          return self.list_objets.pop(0)


    def flush(self) -> None:
        self.list_objets.claer()

    def see(self):
      """Me permite ver el contenido de la lista

      return:
        list_objets: Es una lista con los caracteres agregados
      """
      print(self.list_objets)
        

# Test de FIFO
fifo = Buffer("FIFO")
print("\nTest FIFO")
fifo.insert("a")
print("Agrego el elemento A")
fifo.see()
fifo.insert("b")
print("Agrego el elemento B")
fifo.see()
print("Elemento extraido:", fifo.extract())
print("Extrago un elemento con Fifo")
fifo.see()


# Test de FIFO
lifo = Buffer("LIFO")
print("\nTest LIFO")
lifo.insert("a")
print("Agrego el elemento A")
lifo.see()
lifo.insert("b")
print("Agrego el elemento B")
lifo.see()
print("Elemento extraido:", lifo.extract())
print("Extrago un elemento con LIFO")
lifo.see()


# Cado cuando se intenta extrer de un elemento que no tiene elementos
print("\nError provocado con fines demostrativos")
sinElemento = Buffer("LIFO")
sinElemento.extract()
