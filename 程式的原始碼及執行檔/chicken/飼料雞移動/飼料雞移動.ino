const int In1 = 6;
const int In2 = 7;
String str;

 
void setup(){
  Serial.begin (115200);

  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  scanf("%s",&str);
    
}
void loop(){
  if(Serial.available()){                               //  接收指令
    str = Serial.readStringUntil('\n');                 //  接收指令       
  }
  if (str == "run"){
    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    delay(5000);
    str = "stop";
  }
  if(str == "stop"){
    Serial.println("stop");
    delay(500);
    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    delay(5000);
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    str =  " ";
  }
}
