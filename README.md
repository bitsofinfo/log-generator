# log-generator

Simple python script to generate random time series data into a log file (GMT time)
useful for generating sample time-series based data to feed other downstream systems.

### Usage

```
logGenerator.py --logFile <targetFile>
    [--minSleepMs <int>] [--maxSleepMs <int>]
    [--sourceDataFile <fileWithTextData>] [--iterations <long>]
    [--minLines <int>] [--maxLines <int>]
    [--logPattern <pattern>] [--datePattern <pattern>]
```

### Defaults

```
iterations = -1 # infinite
minSleep = 0.1
maxSleep = 1
minLines = 1
maxLines = 1
logFile = 'logGenerator.log'
sourceDataFile = 'defaultDataFile.txt'
logPattern = '%(asctime)s,%(msecs)d %(process)d %(filename)s %(lineno)d %(name)s %(levelname)s %(message)s'
datePattern = "%Y-%m-%d %H:%M:%S"
```
