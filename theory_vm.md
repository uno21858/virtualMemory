Memoria Virtual – Del Concepto a la Simulación

Memoria virtual vs. memoria física
La memoria virtual es una técnica que permite a cada proceso tener un espacio de direcciones privado, grande y contiguo, aunque la memoria física (RAM) sea limitada. La memoria física es la RAM real. La memoria virtual usa respaldo en disco para almacenar páginas que no caben en RAM. Como explican Tanenbaum (Modern Operating Systems) y Silberschatz (Operating System Concepts), esto permite ejecutar programas grandes, aislar procesos y manejar la memoria de forma flexible.

Paginación y tablas de páginas
En paginación, la memoria virtual se divide en páginas y la física en marcos del mismo tamaño. Una tabla de páginas mapea páginas virtuales a marcos físicos. Una entrada contiene: frame (marco físico asignado), present (si está cargada) y dirty (si fue modificada). La MMU usa esta tabla para traducir direcciones. Los TLB aceleran la traducción.

Manejo de fallos de página
Un page fault ocurre cuando un proceso accede a una página que no está cargada. El sistema operativo:

Verifica que la página sea válida.

Obtiene un marco libre o elige uno para reemplazar.

Si la página víctima está dirty, se escribe al disco.

Carga la página solicitada desde el backing store.

Actualiza la tabla de páginas.

Reintenta la instrucción fallida.

Backing store y dirty bit
El backing store es un área en disco donde se guardan páginas que no están en RAM. El dirty bit indica si la página fue modificada. Según Tanenbaum, páginas dirty deben escribirse al disco antes de ser reemplazadas; páginas clean pueden descartarse porque el respaldo está actualizado.

Reemplazo FIFO
FIFO expulsa la página que lleva más tiempo en RAM. Ventaja: fácil de implementar. Desventaja: puede expulsar páginas muy usadas. Esto es parte de la anomalía de Belady. Sistemas reales prefieren LRU o Clock, pero FIFO es excelente para simulaciones educativas.

Traducción de direcciones
Una dirección virtual se divide en número de página y offset. La MMU consulta la tabla de páginas, obtiene el marco físico y combina el offset para formar la dirección física. Intel documenta este proceso como address translation, núcleo del funcionamiento de la MMU.

Aislamiento de procesos
Cada proceso tiene su propia tabla de páginas. Esto impide que un proceso acceda a la memoria de otro. Windows y Linux utilizan el aislamiento como base de seguridad y estabilidad.

Conexión con la simulación
En la simulación en Python, se implementan: tabla de páginas, carga y expulsión de páginas, dirty bit, FIFO, un backing store simulado, y traducción de direcciones. Es una réplica conceptual de cómo trabaja un sistema operativo real al gestionar la memoria.

Referencias:

Andrew S. Tanenbaum – Modern Operating Systems

Silberschatz, Galvin, Gagne – Operating System Concepts

Intel Architecture Developer Manuals