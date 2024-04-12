int counter = 0;
int incomingChar;

void setup(){
  Serial.begin(115200); // Start up Serial Port
  delay(700);// Wait for Serial to settle
  Serial.println("Rcolecting Data...");
}

void loop(){
  // Wait for computer to send character
  // Once character received, start sending data to computer
  if (Serial.available() > 0){
    incomingChar = Serial.read();
    
    // Send data to computer via Serial
    for (int i = 0; i < 10; i++){
      Serial.print(counter);
      Serial.print(",");
      Serial.print(counter + 1);
      Serial.print(",");
      Serial.println(counter + 2); // \n will end read by computer
      counter++;
      delay(3000);
    } 
  
  // Once data send is finished, send 'stop' to complete
  Serial.println("stop");
  Serial.flush();
  }
  
}
