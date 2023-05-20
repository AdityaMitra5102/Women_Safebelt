#include "ESP8266WiFi.h"
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

String nm="Anisha";
String eml="ghoshanisha2002@gmail.com";
char* ssid="";
const char* ssid2[5]={"A","B","C","D","E","F"};//Enter SSID
const char* password = ""; //Enter Password
String ip=""; //Change to correct IP
void setup()
{ 
  Serial.begin(9600);
  // Connect to WiFi
for(int i=0;i<5;i++)
{
  WiFi.begin(ssid[i],password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
     Serial.print("*");
  } 

  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.print("The IP Address of ESP8266 Module is: ");
  Serial.print(WiFi.localIP());// Print the IP address
  ssid=ssid2[i];
  break;
  
}
}

void loop() 
{
  int k=(analogRead(0));
  if(k>900)
  {
    Serial.println("Button pressed");
    delay(1000);
    sendEmail();
  }
}

void sendEmail()
{
  String serverPath = "http://"+ip + "/safebandemail?name="+nm+"&ssid="+ssid+"&email="+eml;
  Serial.println(serverPath);
  WiFiClient client;
  HTTPClient http;
  http.begin(client,serverPath.c_str());
  http.GET();
}
