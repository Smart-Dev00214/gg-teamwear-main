## API - Get Started
```
cd api/
npm install
npm run build
npm run start
```
visit http://localhost:3000/ (should say hello world) 

## Setup Instance
sudo apt install git
ssh-keygen -t ed25519 -C "s.rosa@wiredhub.io"
cat ~/.ssh/id_ed25519.pub
https://github.com/settings/ssh/new
To change github password: ssh-keygen -p -f ~/.ssh/id_ed25519
git clone git@github.com:R-Stefano/gg-teamwear.git (wiredhub)
sudo apt-get install python-pip
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install nodejs -y

Allow visit http://34.154.23.158:8080/
https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/details/allow-8080?project=gg-teamwear&hl=en

## Put online bots
cd gg-teamwear
sudo python -m pip install install -r requirements.txt
sudo python -m pip install mysql-python
sudo apt install default-libmysqlclient-dev
sudo cp bots-webserver.service /etc/systemd/system/bots-webserver.service
cd bots-3.2.0
sudo python setup.py install
cp ./prod_settings.py ./bots/config/settings.py
sudo cp -R usersys/* bots/usersys/
sudo systemctl start bots-webserver.service OR sudo python bots-webserver.py
visit http://34.154.23.158:8080/



## Put online webapp
sudo cp webapp.service /etc/systemd/system/webapp.service
cd webapp
npm install
npm run build
sudo systemctl start webapp.service OR npm run start

# Switch Steps
Turnon OpenVPN
Login with root at 
Go to <>/admin/bots/routes/
Turn all of them off
Dump Bots DB
Dump new_schema DB
Upload botsDb
Upload new_schema
update channels: update channel set keyfile='/home/stefano_bane/gg-teamwear/id_rsa' where host='eu-sftp.amazonsedi.com'
update internal path: UPDATE channel SET path = REPLACE(path, '/home/app/internalFileExchange', '/home/stefano_bane/gg-teamwear/internalFileExchange') where path like '/home/app/internalFileExchange%'
update external path: UPDATE channel SET path = REPLACE(path, '/home/scambio', '/home/stefano_bane/gg-teamwear/scambio') where path like '/home/scambio%'
????
compare with http://192.168.11.231:8080/login/

## Notes
???? api/src/file-output/file-output.service.ts
??? api schema and migrations?
(api) sudo cp api.service /etc/systemd/system/api.service
(api) sudo systemctl start api.service 
(api) npm run start:prod