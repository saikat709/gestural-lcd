const int led = 13;    
const int sensor = 2;  

int state = LOW; // Previous state
int val = 0;     // Current read

void setup() {
  pinMode(led, OUTPUT);
  pinMode(sensor, INPUT);
  Serial.begin(9600);

  Serial.println("Calibrating sensor...");
  delay(10000); // 10 seconds for sensor to stabilize
  Serial.println("Sensor ready.");
}

void loop() {
  val = digitalRead(sensor);

  if (val == HIGH && state == LOW) {
    digitalWrite(led, HIGH);
    Serial.println("Motion detected");
    state = HIGH;
  } 
  else if (val == LOW && state == HIGH) {
    digitalWrite(led, LOW);
    Serial.println("Motion stopped");
    state = LOW;
  }

  delay(100); // Prevent spamming
}
