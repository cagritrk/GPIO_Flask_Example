from flask import Flask, render_template
import OPi.GPIO as GPIO

app = Flask(__name__)

port = 7                        # set BCM7 (pin 26) as port (7)
GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setup(port, GPIO.OUT)      # set BCM7 (pin 26) as an output (LED)

@app.route('/')
def index():
    if (GPIO.gpio_function(port) == 0):
        led_status = "Led Off"
    else:
        led_status = "Led On"
    return render_template("index.html", message = led_status)

@app.route('/ledon/', methods=['POST'])
def ledOn():
    led_status = "Led ON"
    GPIO.output(port, 1)
    print ("Led ON Calisti")
    return render_template("index.html", message = led_status)

@app.route('/ledoff/', methods=['POST'])
def ledOff():
    led_status = "Led Off"
    GPIO.output(port, 0)
    print ("Led OFF Calisti")
    return render_template("index.html", message = led_status)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=80)