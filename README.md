![Version 2.0](http://img.shields.io/badge/version-v2.0-green.svg)
![Python 3.8](http://img.shields.io/badge/python-3.10-blue.svg)
[![MIT License](http://img.shields.io/badge/license-MIT%20License-blue.svg)](https://github.com/OBoladeras/updog/blob/master/LICENSE)

<p>
  <img src="https://raw.githubusercontent.com/OBoladeras/updog2/main/updog2/static/images/updog.png" width=85px alt="updog"/>
</p>

Updog is a replacement for Python's `SimpleHTTPServer`. 
It allows uploading and downloading via HTTP/S, 
can set ad hoc SSL certificates and use HTTP basic auth.

<p align="center">
  <img src="https://raw.githubusercontent.com/OBoladeras/updog2/main/updog2/static/images/example.png" alt="Updog screenshot"/>
</p>

## Installation

Install using pip:

`pip3 install updog2`

## Usage

`updog2 [-d DIRECTORY] [-p PORT] [--password PASSWORD] [--ssl]`

| Argument                            | Description                                      |
|-------------------------------------|--------------------------------------------------| 
| -d DIRECTORY, --directory DIRECTORY | Root directory [Default=.]                       | 
| -p PORT, --port PORT                | Port to serve [Default=9090]                     |
| -qr, --qr                           | Show QR code to access the page                  |
| --password PASSWORD                 | Use a password to access the page. (No username) |
| --ssl                               | Enable transport encryption via SSL              |
| --version                           | Show version                                     |
| -h, --help                          | Show help                                        |

## Examples

**Serve from your current directory:**

`updog2`

**Serve from another directory:**

`updog2 -d /another/directory`

**Serve from port 1234:**

`updog2 -p 1234`

**Password protect the page:**

`updog2 --password examplePassword123!`

*Please note*: updog uses HTTP basic authentication.
To login, you should leave the username blank and just
enter the password in the password field.

**Use an SSL connection:**

`updog2 --ssl`

**Show a QR code to access the page:**

`updog2 -qr`


## Notes

This project is a fork of [updog](https://github.com/sc0tfree/updog) by [sc0tfree](https://github.com/sc0tfree).
The original project is no longer maintained, so I decided to fork it and keep it up to date.
The changes I made can be found in the [CHANGELOG](CHANGELOG.md).
