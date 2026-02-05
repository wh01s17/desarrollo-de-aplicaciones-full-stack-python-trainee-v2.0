# Ecommerce CLI con POO - Módulo 4

## Descripción

Aplicación de ecommerce por consola desarrollada con Programación Orientada a Objetos en Python. Implementa dos roles diferenciados (Administrador y Cliente) con funcionalidades específicas para cada uno.

## Características Principales

### 🔹 Programación Orientada a Objetos

- **Clases**: Producto, Catalogo, Carrito, ItemCarrito, Usuario (abstracta), Admin, Cliente, Tienda
- **Herencia**: Admin y Cliente heredan de Usuario (clase base abstracta)
- **Composición**: Catalogo contiene Productos, Carrito contiene ItemCarrito
- **Encapsulamiento**: Métodos y atributos bien organizados

### 🔹 Roles de Usuario

#### 👨‍💼 ADMINISTRADOR

- Listar productos del catálogo
- Crear nuevos productos
- Actualizar productos existentes (nombre, categoría, precio)
- Eliminar productos del catálogo
- Guardar catálogo en archivo de texto

#### 👤 CLIENTE

- Ver catálogo de productos
- Buscar productos por nombre o categoría
- Agregar productos al carrito (con cantidad)
- Ver carrito y total
- Confirmar compra (guarda orden en archivo)
- Vaciar carrito

### 🔹 Manejo de Excepciones

- `ProductoNoEncontradoError`: Cuando no se encuentra un producto por ID
- `CantidadInvalidaError`: Cuando la cantidad es menor o igual a 0
- `CarritoVacioError`: Cuando se intenta operar con un carrito vacío
- `ArchivoError`: Errores al leer/escribir archivos
- Manejo robusto con bloques try/except/finally

### 🔹 Persistencia de Datos

- **catalogo.csv**: Guarda el catálogo de productos en formato CSV delimitado por ";" (opcional)
- **ordenes.txt**: Registra todas las compras confirmadas con fecha/hora, productos y total

## Estructura de Archivos

```
ecommerce_m4/
│
├── main.py                 # Punto de entrada de la aplicación
├── tienda.py              # Clase principal que coordina la ejecución
├── usuarios.py            # Clases Usuario, Admin y Cliente
├── producto.py            # Clase Producto
├── catalogo_clase.py      # Clase Catalogo con métodos CRUD
├── carrito_clase.py       # Clases Carrito e ItemCarrito
├── excepciones.py         # Excepciones personalizadas
│
├── catalogo.csv           # (generado) Catálogo guardado en formato CSV
├── ordenes.txt            # (generado) Registro de compras
│
└── README.md              # Este archivo
```

## Requisitos

- Python 3.10 o superior
- No requiere librerías externas

## Cómo Ejecutar

1. Navega al directorio del proyecto:

```bash
cd ecommerce_m4
```

2. Ejecuta la aplicación:

```bash
python main.py
```

o

```bash
python3 main.py
```

## Flujo de Uso

1. **Al iniciar**, la aplicación muestra el banner de bienvenida
2. **Selección de rol**: Elige si quieres entrar como Administrador (1) o Cliente (2)
3. **Menú específico**: Se muestra el menú correspondiente al rol seleccionado
4. **Operaciones**: Realiza las operaciones deseadas según el rol
5. **Salir**: Opción 0 para cerrar la sesión

## Ejemplos de Uso

### Como Administrador

```
1. Listar productos -> Ver todos los productos
2. Crear producto -> Ingresar nombre, categoría y precio
3. Actualizar producto -> Modificar un producto existente
4. Eliminar producto -> Remover un producto del catálogo
5. Guardar catálogo -> Exportar a catalogo.txt
```

### Como Cliente

```
1. Ver catálogo -> Ver todos los productos disponibles
2. Buscar producto -> Filtrar por nombre o categoría
3. Agregar al carrito -> Seleccionar producto y cantidad
4. Ver carrito -> Ver resumen y total a pagar
5. Confirmar compra -> Finalizar compra y guardar orden
6. Vaciar carrito -> Limpiar el carrito
```

## Validaciones Implementadas

- ✅ ID de producto debe existir
- ✅ Cantidad debe ser entre 1 y 99
- ✅ Precio debe ser mayor a 0
- ✅ Nombres y categorías no pueden estar vacíos
- ✅ No se puede confirmar compra con carrito vacío
- ✅ Manejo de errores de archivos (lectura/escritura)

## Conceptos de POO Aplicados

1. **Abstracción**: Clase Usuario como clase base abstracta
2. **Herencia**: Admin y Cliente heredan de Usuario
3. **Encapsulamiento**: Atributos privados (\_proximo_id) y métodos privados (\_crear_producto)
4. **Polimorfismo**: Métodos mostrar_menu() y ejecutar_opcion() implementados diferente en cada clase hija
5. **Composición**: Catalogo tiene lista de Productos, Carrito tiene lista de ItemCarrito

## Notas Técnicas

- Código en español con convenciones snake_case
- Documentación con docstrings en todas las clases y métodos
- Type hints para mejor legibilidad y mantenimiento
- Separación de responsabilidades en módulos independientes
- Código limpio y bien estructurado

## Autor

Desarrollado como parte del Módulo 4 - Programación Orientada a Objetos
Bootcamp Python Full Stack

---

© 2026 Python-Shop Ecommerce CLI
