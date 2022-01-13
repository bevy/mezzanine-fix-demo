# mezzanine-fix-demo

This repo was created to demonstrate the following `mezzanine` issue: https://github.com/stephenmcd/mezzanine/issues/2016

## How to run

1. Install `mysql_config` if it's not already present on your system, eg.
```
# Debian / Ubuntu
sudo apt-get install libmysqlclient-dev
# macOS
brew install mysql
```
2. Install `tox` if it's not already installed:
```
pip3 install tox
```
3. Start the MySQL server:
```
docker-compose up
```
4. With the server running, run tests:
```
tox
```
