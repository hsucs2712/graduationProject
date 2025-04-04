#include <Stepper.h> 

const int stepsPerRevolution = 2048;                    //設定步進馬達轉一圈為 2048步，此數值不可改變
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

int trigPin = 6;                                       //Trig Pin
int echoPin = 7;                                       //Echo Pin
long duration, cm, inches;

String str;

void setup() {
  myStepper.setSpeed(10);                               //設定轉速，容許設定的範圍為每分鐘 0-15 圈

  Serial.begin (9600);                                  // Serial Port begin
  pinMode(trigPin, OUTPUT);                             // 定義輸入及輸出 
  pinMode(echoPin, INPUT);
  scanf("%d",&str);
}

void loop() {  
  if(Serial.available()){                               //  接收指令
    str = Serial.readStringUntil('\n');                 //  接收指令
    if(str == "stop"){                                  //當收到stop時 str為空值 飼料雞將停止轉動
      str = " ";  
    }       
  }
   if(str == "general"){                                //一般模式
        Serial.println("run");                      
        digitalWrite(trigPin, LOW);
        delayMicroseconds(5);
        digitalWrite(trigPin, HIGH);                    // 給 Trig 高電位，持續 10微秒
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        pinMode(echoPin, INPUT);                        // 讀取 echo 的電位
        duration = pulseIn(echoPin, HIGH);              // 收到高電位時的時間
      
        cm = (duration/2) / 29.1;                       // 將時間換算成距離 cm 或 inch  
        
        delay(10);

        
        if (cm >= 100){                                         //修改if內的條件來達到控制速度
          myStepper.setSpeed(15);                               //設定轉速 15，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }else if(cm < 100 && cm >= 50){
          myStepper.setSpeed(10);                               //設定轉速 10，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }else{
          myStepper.setSpeed(5);                                //設定轉速 5，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }                                           
    }
    if(str == "feather"){                                //一般模式
        Serial.println("run");                      
        digitalWrite(trigPin, LOW);
        delayMicroseconds(5);
        digitalWrite(trigPin, HIGH);                    // 給 Trig 高電位，持續 10微秒
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        pinMode(echoPin, INPUT);                        // 讀取 echo 的電位
        duration = pulseIn(echoPin, HIGH);              // 收到高電位時的時間
      
        cm = (duration/2) / 29.1;                       // 將時間換算成距離 cm 或 inch  
        
        delay(10);

        
        if (cm >= 100){                                         //修改if內的條件來達到控制速度
          myStepper.setSpeed(15);                               //設定轉速 15，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }else if(cm < 100 && cm >= 50){
          myStepper.setSpeed(10);                               //設定轉速 10，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }else{
          myStepper.setSpeed(5);                                //設定轉速 5，容許設定的範圍為每分鐘 0-15 圈
          myStepper.step(2);                   //正轉一圈
        }                                           
    }
}
