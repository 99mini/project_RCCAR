String Speed;
int speed= 200;

int a1 = 4;
int a2 = 5;
int b1 = 6;
int b2 = 7;

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
	case 'G':
		analogWrite(a1,0);
		analogWrite(a2,speed);
		analogWrite(b1,speed);
		analogWrite(b2,0);
		delay(3000);
		break;
	case 'B':
		analogWrite(a1,speed);
		analogWrite(a2,0);
		analogWrite(b1,0);
		analogWrite(b2,speed);
		delay(3000);
		break;
	case 'L':
		analogWrite(a1,0);
		analogWrite(a2,speed);
		analogWrite(b1,0);
		analogWrite(b2,0);
		delay(3000);
		break;
	case 'R':
		analogWrite(a1,0);
		analogWrite(a2,0);
		analogWrite(b1,speed);
		analogWrite(b2,0);
		delay(3000);
		break;
	default:
		return;
    }
}
