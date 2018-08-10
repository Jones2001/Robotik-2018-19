sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python-pygame -y
wget https://raw.githubusercontent.com/NastyGamer/Robotik-2018-19/master/Ball-Detection.py
wget http://github.com/TinkerBoard/gpio_lib_python/archive/sbc/tinkerboard/python.zip GPIO_API_for_Python.zip
sudo apt-get install python-dev -y
unzip GPIO_API_for_Python.zip
cd GPIO_API_for_Python/
sudo python setup.py install
sudo apt-get purge libreoffice wolfram-engine sonic-pi scratch
sudo apt-get clean
sudo apt-get autoremove
sudo rm Install.sh
