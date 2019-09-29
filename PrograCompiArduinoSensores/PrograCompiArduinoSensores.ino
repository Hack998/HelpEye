
//sonido
const int analogInPin = A1;
int sensorValue = 0;

//ultrasonico
const int Trigger = 2;   //Pin digital 2 para el Trigger del sensor 
const int Echo = 3;   //Pin digital 3 para el Echo del sensor

//Motor
int M1_Izq = 6; //Pin digital 4 para Direccion
int M1_Derecha = 7; //Pin digital 5 para Direccion

//Temperatura
int val;
const int tempPin = A0; //Pin digital A3 para temperatura
 
//Luz Aquí almacenamos los datos recogidos del LDR:
int valorLDR = 0;
//Luz Pin analógico donde conectarmos el LDR
int pinLDR = A3;

//Vibracion
int LED_Pin = 13;
int vibr_Pin =4;


//variable para meter todos los datos
//Temperatura,Distancia,Decibelios,Iluminacion
//vibra,incli,temp,luz,sonido
String TodosLosDatos = "";


void setup() {
  Serial.begin(9600);//iniciailzamos la comunicación
  //Ultrasonico
  pinMode(Trigger, OUTPUT); //pin como salida
  pinMode(Echo, INPUT);  //pin como entrada
  digitalWrite(Trigger, LOW);//Inicializamos el pin con 0
  //Motor
  pinMode(M1_Izq, OUTPUT);
  pinMode(M1_Derecha, OUTPUT);
  //Vibracion
  pinMode(LED_Pin, OUTPUT);
  pinMode(vibr_Pin, INPUT); //set vibr_Pin input for measurment
}

void loop() {
  ////////////////////////////////////////////////////////
  //Vibracion
  long measurement =TP_init();
  
  TodosLosDatos.concat((String)measurement);


  ///////////////////////////////////////////////////////
  //ultrasonico
  long t; //tiempo que demora en llegar el eco
  long d; //distancia en centimetros
  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);          //Enviamos un pulso de 10us
  digitalWrite(Trigger, LOW);
  t = pulseIn(Echo, HIGH); //obtenemos el ancho del pulso
  d = t/59;             //escalamos el tiempo a una distancia en cm
  TodosLosDatos.concat(",");
  TodosLosDatos.concat((String)d);


  ///////////////////////////////////////////////////////
  //Temperatura
  val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/10;    //temperatura en celsius
  float farh = (cel*9)/5 + 32; //temperatura en fahrenheit (borrar)
  TodosLosDatos.concat(",");
  TodosLosDatos.concat((String) round(cel)); 

  //////////////////////////////////////////////////////
  //Valor de luz leido intervalo entre  0 a 1023, 0=oscuridad
  valorLDR = analogRead(pinLDR);
  TodosLosDatos.concat(",");
  TodosLosDatos.concat((String) valorLDR); 
  
  ///////////////////////////////////////////////////////
  //sonido
  sensorValue = analogRead(analogInPin);
  double db = (20 * log(10)) * (sensorValue / 5);
  TodosLosDatos.concat(",");
  TodosLosDatos.concat((String)sensorValue);
  
  ///////////////////////////////////////////////////////
  Serial.println(TodosLosDatos);
  TodosLosDatos="";
  ///////////////////////////////////////////////////////






  String datosRecibidos;
  if (Serial.available() > 0) {
    datosRecibidos = Serial.readStringUntil('\n');
    //DEBUG(datosRecibidos);
    //Serial.println(datosRecibidos);
    //girar(1); //E
    //delay(1500);
 }

 
  //delay(1000);
  //girar (2);
  //delay(100); //1 sg
  //stop();

  for (int i=0; i<8; i++){
    if ((String)datosRecibidos[i]=="1"){
      girar(1); //E
      delay(1500);
      stop();
      delay(200);
    }
    if((String)datosRecibidos[i]=="0"){
      girar(2);
      delay(500);
      stop();
      delay(200);
    }
  }
  stop();
  //delay(1000);



  
 /*
  stop();
  delay(250); //250ms

  
  stop();
  delay(250); //250ms
  */
}

//Funcion de girar motor
void girar(int direccion)
{
  boolean inPin1 = LOW;
  boolean inPin2 = HIGH;

  if(direccion == 1){
    inPin1 = HIGH;
    inPin2 = LOW;
  }
    digitalWrite(M1_Izq, inPin1);
    digitalWrite(M1_Derecha, inPin2);
}

//Funcion de parar motor
void stop(){
    digitalWrite(M1_Izq, LOW);
    digitalWrite(M1_Derecha, LOW);
}

//Funcion para vibracion
long TP_init(){
  delay(10);
  long measurement=pulseIn (vibr_Pin, HIGH);  //wait for the pin to get HIGH and returns measurement
  return measurement;
}
