/*
motor speed
*/

int SPEED= 160;

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

int DELAY_TIME = 100;

void setup(){
	Serial.begin(9600);
	pinMode(a1,OUTPUT);
	pinMode(a2,OUTPUT);
	pinMode(b1,OUTPUT);
	pinMode(b2,OUTPUT);
}

void loop(){
    char DataToRead[2];
	DataToRead[1] = '\n';
	
	Serial.readBytesUntil(char(13),DataToRead, 2);
	char direction = DataToRead[0];
	
	int i=1;
	while(DataToRead[i] != '\n' && i < 2) i++;
	
	switch(direction){
		case 'B':
			analogWrite(a1,0);
			analogWrite(a2,SPEED);
			analogWrite(b1,SPEED);
			analogWrite(b2,0);
			delay(DELAY_TIME);
			break;
		case 'G':
			analogWrite(a1,SPEED);
			analogWrite(a2,0);
			analogWrite(b1,0);
			analogWrite(b2,SPEED);
			delay(DELAY_TIME);
			break;
		case 'L':
			analogWrite(a1,0);
			analogWrite(a2,SPEED);
			analogWrite(b1,0);
			analogWrite(b2,0);
			delay(DELAY_TIME);
			break;
		case 'R':
			analogWrite(a1,0);
			analogWrite(a2,0);
			analogWrite(b1,SPEED);
			analogWrite(b2,0);
			delay(DELAY_TIME);
			break;
		default:
			return;
    }
}
