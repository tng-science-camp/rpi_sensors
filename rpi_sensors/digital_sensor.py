#!/usr/bin/env python3
import logging
import RPi.GPIO as GPIO

class DigitalSensor(object):
    """
    A DigitalSensor object represents a GPIO input.
    """
    def __init__(self, gpio_pin, gpio_mode=GPIO.BCM, event_type=GPIO.BOTH):
        '''
        Args:
            gpio_pin (int): GPIO pin number this sensor is connected to.
            gpio_mode (optional): GPIO pin numbering convension. It may be GPIO.BCM or GPIO.BOARD. If not
                specified, it default to GPIO.BCM.
            event_type (optional): Even detection type. To detect both rising and falling edges, use GPIO.BOTH.
                To detect rising edges, use GPIO.RISING. To detect falling edges, use GPIO.FALLING.
                If not specified, it default to GPIO.BOTH.
        '''
        logging.info('Initializing a DigitalSensor.')
        self._gpio_pin = gpio_pin
        self._gpio_mode = gpio_mode
        self._event_type = event_type
        self._detect_callbacks = set()
        GPIO.setmode(self._gpio_mode)
        GPIO.setup(self._gpio_pin, GPIO.IN)
        GPIO.add_event_detect(self._gpio_pin, self._event_type,
                              callback=self._execute_callbacks)

    def __del__(self):
        GPIO.cleanup(self._gpio_pin)
        
    def get_gpio_pin(self):
        '''Get the GPIO pin used for this sensor.
        
        Note:
            The GPIO pin value may be in GPIO.BCM or GPIO.BOARD convension.
            Use get_gpio_mode() to determine the pin number convension used
            for this sensor.
        
        Returns:
            int: GPIO pin value.
        '''
        return self._gpio_pin
        
    def get_gpio_mode(self):
        '''Get GPIO pin number convension used for this sensor.
        
        Returns:
            GPIO.BCM or GPIO.BOARD
        '''
        return self._gpio_mode
        
    def get_event_type(self):
        '''Get event detection type.
        
        Returns:
            GPIO.BOTH, GPIO.RISING, or GPIO.FALLING    
        '''
        return self._event_type
        
    def get_sensor_value(self):
        '''Get current sensor value.
        
        Returns:
            float: Current GPIO pin value
        '''
        return GPIO.input(self._gpio_pin)
        
    def wait_for_event(self, edge=self._event_type):
        '''
        '''
        GPIO.wait_for_edge(self._gpio_pin, edge)
    
    def set_event_detect(self, edge, bouncetime=None):
        self._event_type = edge
        GPIO.add_event_detect(self._gpio_pin, self._event_type, bouncetime=bouncetime)
        
    def add_detect_callback(self, callback):
        self._detect_callbacks.add(callback)
    
    def remove_detect_callback(self, callback):
        self._detect_callbacks.remove(callback)

    def clear_detect_callbacks(self):
        self._detect_callbacks.clear()

    def _execute_callbacks(self):
        for callback in self._detect_callbacks:
            callback()
            
if __name__ == "__main__":
    digital_sensor = DigitalSensor(17)
    
    def print_value():
        print("{:d}".format(digital_sensor.get_value()))
        
    digital_sensor.add_detect_callback(print_value)
        
    try:
        while True:
            
    finally:
        GPIO.cleanup()
