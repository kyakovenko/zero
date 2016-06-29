# Zero

The application is intended to provide information about environment. At the moment, temperature and humidity.

It consists two parts:

- Slack bot. It's the main communication channel. Users can ask the bot about a current status of environment.
- Data picker. It collects information about environment and stores it into a database.

Data picker is based on the [PiSensors](https://github.com/kyakovenko/python-pi-sensors) library so currently it
can work only with a RaspberryPi and a DHT11 sensor.

# Installation / Requirements

There is a fabric script which is intended to simplify a deploy process. First of all, you have to install fabric in
your python environment, for example, using the following command:

```
pip install fabric
```

After than you can use fabric and deploy the application to your RaspberryPi with the following command:

```
fab -H{host_name_or_its_ip} -u {user_name} deploy
```

Usually, an application's launch takes about 20-30 seconds after a RaspberryPi restart.

# License

Zero is distributed under the MIT license. Please, see the [LICENSE](LICENSE) file.