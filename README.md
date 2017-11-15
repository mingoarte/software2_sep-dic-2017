# TUIsD
Repositorio para el proyecto de Ingeniería de Software II Sep-Dic 2017

## Cómo crear un nuevo patrón?
Para crear un nuevo patrón debes definir su modelo, que implementa el modelo abstracto Patron y defina un método render que devuelva el HTML que corresponde a ese patrón.
Ejemplo:

```python
from builder.models import Patron
class MiPatron(Patron):
    # ... mis atributos

    # Este método devuelve el html que corresponde a la visualización del patrón
    def render(self):
        pass
```

Para crear una nueva instancia de un patrón, puedes utilizar el método create_pattern, que recibe los atributos de MiPatron, así como `template` y `position` para crear el TemplateComponent automaticamente. Este método devuelve la instancia creada

