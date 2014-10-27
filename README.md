network-alert
=============
[![Build Status](https://travis-ci.org/mccannm11/network-alert.png?branch=master)](https://travis-ci.org/mccannm11/network-alert)

A little python script script to send alert emails when a new computer connects to your network.

## Install
    apt-get install python-dev
    git clone https://github.com:mccannm11/network-alert.git
    cd network-alert
    python setup.py test
    python setup.py install

## Run
You need to be root!
`nalert {learn, alert, known, unknown, clear}`

## Commands
* learn: saves the mac addresses found on our network to file.
* alert: sends you an email if unknown devices are found. Also performs a learn.
* known: lists known devices.
* unknown: lists unknown devices if any.
* all: lists all devices currently on the network.

## Run tests
`python setup.py test`

## Cron
You're going to want to set up a cron to run this every `x` minutes!
