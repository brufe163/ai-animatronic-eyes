import cv2
from ultralytics import YOLO
import numpy as np
import serial  


model = YOLO("yolov8n-face.pt").to("cuda") # Cargamos el modelo YOLOv8 preentrenado para detección de caras

video_path = "http://192.168.100.21:81/stream"  # URL de la cámara IP, depende de la wifi a la que se conecte
cap = cv2.VideoCapture(video_path)

 
if not cap.isOpened():  # Verificamos si se pudo abrir el video
    print("Error: No se pudo abrir el video.")
    exit()


frames_to_skip = int(cap.get(cv2.CAP_PROP_FPS) // 2) # Solo procesamos 2 frames por segundo, ayuda a reducir la carga computacional

ser = serial.Serial('COM3', 9600)  # Configurar la comunicación serial, reemplazar COM por el que se esté usando
print("Comunicación serial establecida.")

try:
    frame_count = 0
    while True:
        success, img = cap.read()
        if not success:
            break
        if frame_count % frames_to_skip == 0:
            results = model(img, stream=True, verbose=False, conf=0.4)
            for r in results: # Procesamos los resultados de detección
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    center_x = (x1 + x2) // 2 # Calculamos el centro de la cara (coordenada X)
                    ser.write(f"{center_x}\n".encode())  # Enviamos la coordenada X seguida de un salto de línea
                    cv2.circle(img, (center_x, (y1 + y2) // 2), 5, (255, 0, 255), -1) # Dibujamos el punto central en la imagen
            cv2.imshow('Output', img) # Mostrar la imagen con el punto central dibujado
        frame_count += 1
        if cv2.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    cap.release()# Liberamos los recursos
    cv2.destroyAllWindows()
    ser.close()  # Cerramos la comunicación serial al finalizar
    print("Comunicacióon serial cerrada.")


