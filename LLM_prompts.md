LLM_prompts.md

Prompt 1 – Estructuras de datos

Prompt inicial:
Diseñe las estructuras de datos para un simulador de memoria virtual en Python. Cree las clases PTEntry, PageTable y PhysicalMemory. PTEntry debe tener frame, present y dirty. Use dataclasses y las constantes PAGE_SIZE=256, VIRTUAL_PAGES=16, PHYSICAL_FRAMES=8. Explique por qué existe cada clase y cada campo.

Prompt refinado:
Cree las clases PTEntry, PageTable y PhysicalMemory usando @dataclass. PTEntry debe tener frame, present y dirty. PageTable debe mapear páginas virtuales a PTEntry. PhysicalMemory debe contener frames (bytearray de PAGE_SIZE) y free_frames. Use las constantes proporcionadas y explique la razón de cada clase.

Respuesta (resumen del contenido generado por GPT):
PTEntry contiene frame, present y dirty. PageTable mapea páginas a entradas PTEntry. PhysicalMemory contiene los marcos físicos y la lista de marcos libres.

Prompt 2 – Page Fault + FIFO Replacement

Prompt inicial:
Desarrolle _ensure_in_ram(page_no). Debe manejar page faults, elegir víctimas con FIFO, escribir páginas dirty y actualizar la tabla. Use frame_to_page para mapeo inverso.

Prompt refinado:
Implemente _ensure_in_ram(page_no):

Si la página ya está presente, terminar.

Si no está presente: tomar un marco libre o desalojar usando FIFO.

Si la víctima está dirty, escribirla al backing store.

Cargar la página desde el backing store.

Actualizar frame_to_page y fifo_queue.
Explique la lógica paso a paso.

Respuesta (resumen de GPT):
El método verifica presencia, maneja un page fault, usa un marco libre o hace eviction FIFO, escribe el dirty si es necesario, carga la página y actualiza estructuras.

Prompt 3 – Read, Write, Zero

Prompt inicial:
Implemente read_byte, write_byte y zero_page usando address translation y _ensure_in_ram. write_byte debe activar el dirty bit.

Prompt refinado:
read_byte: traducir dirección, asegurar página y leer byte.
write_byte: asegurar página, escribir valor y marcar dirty.
zero_page: asegurar página, llenar con ceros y marcar dirty.

Respuesta (resumen de GPT):
Las funciones traducen la dirección virtual, llaman a _ensure_in_ram y realizan la operación solicitada, ajustando el dirty bit cuando aplica.

Prompt 4 – vm.py final

Prompt inicial:
Combine todo en un solo archivo vm.py.

Prompt refinado:
Genere vm.py completo: constantes, PTEntry, PageTable, PhysicalMemory, y la clase VM con métodos init, _ensure_in_ram, read_byte, write_byte, zero_page.

Respuesta (resumen de GPT):
Código final integrado que implementa tablas de páginas, memoria física, page fault, FIFO y operaciones de lectura/escritura.