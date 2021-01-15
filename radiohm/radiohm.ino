
// Pin des capteurs
int VCAPTEUR = A0;
int clk = 3;
int dat = 5;

//#define clk 3
//#define dat 5

// Acquisitions par seconde
int nbParSeconde = 10;
int temps = 1000/nbParSeconde;
int nbmoy = 100;

float potCapteur;

boolean data[24] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; //24 bit boolean array for storing the received data
boolean mm_in = 0; //0 for mm, 1 for inch

int received_bit_location = 0;

float measured_value = 0.0;

void process_data();

long last_received = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  pinMode(VCAPTEUR, INPUT);
  pinMode(clk,INPUT);
  pinMode(dat,INPUT);
  attachInterrupt(digitalPinToInterrupt(clk), clk_ISR, FALLING);  // Faire une mesure lorsque le signal de clock descend
}

void loop() {
  potCapteur = 0.0;
  for (int i = 0; i < nbmoy; i++){
    potCapteur += analogRead(VCAPTEUR);
  }

  potCapteur = potCapteur/nbmoy;
//  potCapteur = analogRead(VCAPTEUR);

  //potCapteur -= analogRead(dat);
  //potCapteur -= analogRead(clk);

  if (mm_in == 1){ // if it's in the inch mode
    //Serial.print(measured_value,4); Serial.println(" in");
  } else {
    Serial.print(measured_value,2);
    Serial.print(" ");
    Serial.println(potCapteur);
  }

  delay(temps);

}

void process_data(){
  
measured_value = 0.0;

if(data[23] == 0){ //if it's in the mm mode
  mm_in = 0;
  //converting binary to decimal value
  for (int i = 0; i<=15; i++){
  measured_value += data[i]*pow(2,i)/100.0;
  }
    if (data[20] == 1){
    measured_value = measured_value * -1; //add the negative sign if it exists
    }
}

if(data[23] == 1){ //if it's in the inch mode
  mm_in = 1;
  //converting binary to decimal value
  for (int i = 1; i<=16; i++){
  measured_value += data[i]*pow(2,(i-1))/1000.0;
  }
    if (data[0]  == 1){
    measured_value += 0.0005; //add the 0.5 mil sign if it exists  
    }
    if (data[20] == 1){
    measured_value = measured_value * -1; //add the negative sign if it exists
    }
}
}

void clk_ISR(){
  if ( millis() - last_received > 2 ){ // Est-ce trop tot?
    received_bit_location = 0;
  }
  
  if (received_bit_location <= 23){
    data[received_bit_location] = !digitalRead(dat); //inverting the received data due to the hardware circuit level shifting
    received_bit_location++;
  } 
  
  if (received_bit_location == 24){
    received_bit_location = 0;
    process_data();
  }
  
  last_received = millis();
  //Serial.println(received_bit_location);
}
