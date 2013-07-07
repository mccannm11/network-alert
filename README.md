#network-alert

A little python script script to send alert emails when a new computer connects to your network.

## Install
`git clone git@github.com:mccannm11/network-alert`

## Configure
Rename the config.example.cfg file to config.cfg and modify the values to your liking:

```
interface = wlan0
known_machines_file = known_machines
smtp_server = localhost
alerting_user = network-alert@localhost
users_to_alert = foo@bar.com,boo@baz.com
```


## Cron
You're going to want to set up a cron to run this every `x` minutes!