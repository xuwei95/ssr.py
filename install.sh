cd /root
yum install git
git clone https://github.com/xuwei95/shadowsocksr

echo "alias ssr='python /root/main.py'" >> /etc/bashrc
source /etc/.bashrc
echo "install success,input 'ssr'to config ..."
