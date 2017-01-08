#### View the weather in your terminal

<p align="left">
  <img src="screenshot.png"/>
</p>
<sup>Uses [OpenWeatherMap](http://openweathermap.org) as data source.</sup>

#### Installation

```
pip install -Ur requirements.txt
ln -s `pwd`/weather.py /usr/local/bin/weather  # Optional symlink for convenience
```
### Usage

After installing and linking you can use "weather" to show the current weather.
If you want to show the weather of the next days, enter an Integer between 0 and 16
to look n days after the current day...

This is a modified version of:
https://github.com/dideler/simple-weather
