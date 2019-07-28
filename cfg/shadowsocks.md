# install setuptools, pip3, shadowsocks client, privoxy
on ubuntu14.04, python3.6 (china). 20190728

## install setuptools (https://www.cnblogs.com/jadexia/p/7797791.html)
```
wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
tar -zxvf setuptools-19.6.tar.gz
cd setuptools-19.6.tar.gz
python3 setup.py build
python3 setup.py install
```
## install pip3
```
wget --no-check-certificate  https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb
tar -zxvf pip-8.0.2.tar.gz
cd pip-8.0.2
python3 setup.py build
python3 setup.py install
```
## install shadowsocks client
```
pip install git+https://github.com/shadowsocks/shadowsocks.git@master
cfg.json:
{
    "server":"my_server_ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
sudo sslocal -c cfg.json -d start
```
## install privoxy
```
sudo apt-get install privoxy
sudo echo "forward-socks5t / 0.0.0.0:1080 ." >> /etc/privoxy/config
sudo service privoxy start
```
