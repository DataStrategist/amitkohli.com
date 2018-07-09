---
title: Arduino theremin concert
author: Amit
type: post
date: 2014-11-11T00:52:47+00:00
url: /arduino-theremin-concert/
xyz_smap:
  - 1
switch_like_status:
  - 1
categories:
  - Arduino
  - Art
  - Maker
  - Music
tags:
  - arduino
  - theremin

---
One of the arduino tutorials was for a theremin. With a few modifications I was able to properly express my sophisticated musical abilities.

Enjoy!



Arduino code follows (prolly doesn&#8217;t make TOO much sense without the wiring schematic&#8230; if there&#8217;s interest I&#8217;ll put up a picture).

<pre>int sensorValue;
int sensorLow=1023;
int sensorHigh=0;
const int ledPin=13;
void setup(){
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,HIGH);
  Serial.begin(9600);
  while(millis()&lt;5000){
    sensorValue=analogRead(A0);
    if(sensorValue&gt;sensorHigh){
      sensorHigh=sensorValue;
    }
    if(sensorValue&lt;sensorLow){
      sensorLow=sensorValue;
    }
  }
  digitalWrite(ledPin,LOW);
}

void loop(){
  sensorValue=analogRead(A0);
  int pitch=map(sensorValue,sensorLow,sensorHigh,50,4000);
  tone(8,pitch,20);
  delay(10);
  Serial.print(sensorValue)
  Serial.print("  ")
  Serial.print(pitch)
}
</pre>