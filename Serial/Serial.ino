/*
motor speed
*/

#define R_MAX 255
#define L_MAX 255
#define R_MID 120
#define L_MID 120

#define DELAY_TIME 120
#define SMALL_DELAY_TIME 150
#define TINY_DELAY_TIME 100

/*
motor pin number
a: right motor
b: left motor
*/

int a1 = 4;
int a2 = 5;
int b1 = 6;
int b2 = 7;

/*
constant delay time
delay time is wheel operation time
if the delay time is longer, the wheel operation time is longer.
*/

void setup(){
	Serial.begin(9600);
	pinMode(a1,OUTPUT);
	pinMode(a2,OUTPUT);
	pinMode(b1,OUTPUT);
	pinMode(b2,OUTPUT);
}

void test() {
  
	analogWrite(a1,R_MAX);
	analogWrite(a2,0);
	analogWrite(b1,0);
	analogWrite(b2,L_MAX);
	Serial.println("test code");
	delay(2000);
}

void mainFunction(){
	char DataToRead[2];
	DataToRead[1] = '\n';
	
	Serial.readBytesUntil(char(13),DataToRead, 2);
	char direction = DataToRead[0];
	
	int i=1;
	while(DataToRead[i] != '\n' && i < 2) i++;
	
	switch(direction){
		case 'G':
			analogWrite(a1,0);
			analogWrite(a2,R_MAX);
			analogWrite(b1,L_MAX);
			analogWrite(b2,0);
			delay(TINY_DELAY_TIME);
			break;

		case 'B':
			analogWrite(a1,R_MAX);
			analogWrite(a2,0);
			analogWrite(b1,0);
			analogWrite(b2,L_MAX);
			delay(SMALL_DELAY_TIME);
			break;

		case 'L':
			analogWrite(a1,0);
			analogWrite(a2,L_MAX);
			analogWrite(b1,0);
			analogWrite(b2,0);
			delay(SMALL_DELAY_TIME);
			break;
		case 'R':
			analogWrite(a1,0);
			analogWrite(a2,R_MAX);
			analogWrite(b1,0);
			analogWrite(b2,0);
			delay(SMALL_DELAY_TIME);
			break;
		case 'l':
			analogWrite(a1,0);
			analogWrite(a2,R_MAX);
			analogWrite(b1,0);
			analogWrite(b2,0);
			delay(SMALL_DELAY_TIME);
			break;
		case 'r':
			analogWrite(a1,0);
			analogWrite(a2,0);
			analogWrite(b1,L_MAX);
			analogWrite(b2,0);
			delay(SMALL_DELAY_TIME);
			break;
		default:
			analogWrite(a1,0);
			analogWrite(a2,0);
			analogWrite(b1,0);
			analogWrite(b2,0);
			return;
    }
	if(direction == 'R' || direction == 'L'){
      delay(20);
    }
    else if(direction =='B'){
      delay(100);
    }
   
    analogWrite(a1,0);
	analogWrite(a2,0);
	analogWrite(b1,0);
	analogWrite(b2,0);
	delay(300);
	Serial.println(direction);
	
}

void loop(){
  //test();
  
  mainFunction();
}
