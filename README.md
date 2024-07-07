# ai-animatronic-eyes
**Integrantes:** Joaquín Barra, Bruno Cavieres, Fernando Feliú
**Curso:** ME4250 - Mecatrónica

Este repositorio contiene material esencial para el desarrollo de un sistema de ojos animatrónicos que mediante una cámara pueden realizar seguimiento de caras.

El diseño de sistemas de ojos animatrónicos constituye un desafío de ingeniería complejo que requiere la integración sincronizada de actuadores para simular movimientos humanos. Este estudio detalla la implementación de servomotores y ensambles para desarrollar un mecanismo robusto y ágil. La simulación del movimiento ocular implica la implementación de visión por computadora para el seguimiento visual de personas que interactúan con el animatrónico. Se propone un sistema de control que estima la posición de las caras de las personas y ajusta su orientación hacia el centro de la cámara.
## Requisitos
* Hardware
  * Arduino Uno/Nano
  * ESP32-CAM
  * Jumpers
  * Servomotores
* Software
  * Python (3.9+)
  * Torch
  * CUDA
  * Arduino IDE
  * Librerías de ESP32 para Arduino IDE
## Modo de uso
1. Clonar repositorio:
```sh
   git clone https://github.com/brufe163/ai-animatronic-eyes.git
   ```
2. Instalar dependencias (TODO: requirements.txt).
3. Modificar códigos .ino de la carpeta Code a ESP32-CAM y Arduino mediante Arduino IDE.
 * En el caso de ESP32-CAM, se debe establecer el nombre de la señal WiFi y su clave para conectar el dispositivo a internet. **Muy importante:** el computador debe estar conectado a la misma red WiFi.
 * En el caso del arduino, se debe tener consideración con posibles cambios de los pines de conexión de los servomotores, los que se definen al inicio del código.
4. Subir códigos a ESP32-CAM y Arduino mediante Arduino IDE.
 * **Muy importante:** En el caso de ESP32-CAM, luego de subir el código, abrir comunicación serial y apretar el botón RESET del ESP32. Aparecerá una dirección IP, a la que al acceder permitirá ver el contenido de la cámara. Se debe extraer el link del stream (terminado en /stream), y **se debe cerrar la página**, ya que sólo se puede acceder al link de forma unitaria.
5. Mantener conectado el Arduino y ejectuar script detection.py. 
