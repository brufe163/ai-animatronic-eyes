#include <Servo.h>

Servo servoX;  // Objeto Servo para el eje X

double Kp = 1.0;  // Constante proporcional
double Ki = 0.0;  // Constante integral
double Kd = 0.0;  // Constante derivativa

double errorX, lastErrorX;
double integralX, derivativeX;

double targetX;  // Posición objetivo en el eje X (coordenada de la cara)

int pinServoX = 9;  // Pin donde está conectado el servo X

void setup() {
  servoX.attach(pinServoX);  // Inicializar el servo en el pin correspondiente
  servoX.write(90);  // Posición inicial del servo (ejemplo: centrado)
  
  // Inicializar valores del PID
  errorX = 0;
  lastErrorX = 0;
  integralX = 0;
  derivativeX = 0;

  Serial.begin(9600);  // Iniciar comunicación serial
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    targetX = data.toInt();  // Leer la posición objetivo desde el PC
  }

  // Calcular error en X
  double actualPositionX = servoX.read();  // Obtener posición actual del servo
  errorX = targetX - actualPositionX;

  // Calcular términos PID
  integralX += errorX;
  derivativeX = errorX - lastErrorX;

  // Calcular señal de control PID
  double outputX = Kp * errorX + Ki * integralX + Kd * derivativeX;

  // Aplicar señal de control al servo X
  double newPositionX = actualPositionX + outputX;
  servoX.write(newPositionX);

  // Actualizar valores para la siguiente iteración
  lastErrorX = errorX;

  delay(20);  // Pequeña pausa para estabilizar el movimiento
}
