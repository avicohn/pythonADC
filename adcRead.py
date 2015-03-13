#Avi Cohn, Jan 6th 2015
#ADCRead python script
import Adafruit_BBIO.ADC as ADC

#AIN0 = P9_39

ADC.setup()

#bug in ADC Python driver, need to read value twice to get latest value
analogValue = ADC.read("AIN0")
analogValue = ADC.read("AIN0")

#convert raw value to voltage
analogVoltage = analogValue * 1.8 
