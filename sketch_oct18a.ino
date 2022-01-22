/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/



void setup(){
    Serial.begin(9600);
    Serial.println("CLEARDATA");
    Serial.println("LABEL,EMG");
}

void loop() {
    int EMG = analogRead(A0);
    Serial.print("DATA,");
    Serial.println(EMG);
    delay(50);
} 
