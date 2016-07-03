# Zero

The application is intended to provide information about environment. At the moment, temperature and humidity.

It consists two parts:

- Slack bot. It's the main communication channel. Users can ask the bot about a current status of environment.
- Data picker. It collects information about environment and stores it into a database.

Data picker is based on the [PiSensors](https://github.com/kyakovenko/python-pi-sensors) library, so currently it
can work only with a RaspberryPi and a DHT11 sensor.

# Setting the project

The Zero has a few settings parameters which should be set. You can do it directly in the zero/slackbot_settings.py
file or you can create a 'zero/local_settings.py' where you can redefine them.

| Settings       |    Description                                          |       Default value        |
| API_TOKEN      | Your api token for Slack                                |       empty string         |
| ERRORS_TO      | A desired recipient who will get message about errors   |       empty string         |
| DHT11_PIN      | A pin to which your device is connected.                |            7               |

# Running the project

There is a fabric script which is intended to simplify a deploy process. First of all, you have to install fabric in
your python environment, for example, using the following command:

```shell
pip install fabric
```

After than you can use fabric and deploy the application to your RaspberryPi with the following command:

```shell
fab -H{host_name_or_its_ip} -u {user_name} deploy
```

Usually, an application's launch takes about 20-30 seconds after a RaspberryPi restart.

# Updating the project

If you just want to update the application on your Raspberry Pi, you can launch the following command:

```shell
fab -H{host_name_or_its_ip} -u {user_name} update
```

# License

The Zero is distributed under the MIT license. Please, see the [LICENSE](LICENSE) file.