# TUIsD
Repositorio para el proyecto de Ingeniería de Software II Sep-Dic 2017

## Cómo crear un nuevo patrón?
Para crear un nuevo patrón debes definir su modelo, que implementa el modelo abstracto Patron y definir algunos métodos que especifican como se renderiza el patrón, su formulario de configuración, y qué va en el card del builder

```python
from builder.models import Patron
class MiPatron(Patron):
    # ... mis atributos

    # Importante, este nombre es utilizado alrededor de la aplicacion, y debe ser consistente con el nombre de patron que utilizas en JS para las funciones que se describen mas adelante
    name = "nombre del patron en minusculas"

    # Este método devuelve el html que corresponde al patrón
    def render(self):
        pass
    # Este método devuelve el html que corresponde al formulario de configuración del patrón
    def render_config_modal(self):
        pass
    # Este método devuelve el html que corresponde a la visualización del patrón en el constructor
    def render_card(self):
        pass
```

Para crear una nueva instancia de un patrón, puedes utilizar el método create_pattern, que recibe los atributos de MiPatron, así como `template` y `position` para crear el TemplateComponent automaticamente. Este método devuelve la instancia creada


En cuánto al JS, los botones de configurar y eliminar son genéricos, no tienes que modificar su comportamiento para cada patrón. Lo que debes implementar, además de cualquier JS particular de tu modal de configuración, es una función que devuelva un JSON con la url y data para hacer la llamada ajax a tu endpoint que guarda/crea tu patron. Ejemplo:

```javascript
function sendMiPatronData() {
  var x = "Dato que recibe miRuta sobre MiPatron"
  var y = "Dato que recibe miRuta sobre MiPatron"

  return {
    url: "/miRuta",
    data: {
      'x': x,
      'y': 
     }
  }
}
```

Para guiarte, puedes tomar como referencia el patron Encuesta.


# Bugs conocidos
- A veces al agregar un patron se agrega dos veces.
- Al editar una encuesta se crea una nueva (views.pollConfig)