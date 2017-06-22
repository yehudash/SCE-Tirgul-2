sudo yum install git-all -y

#install git python and devtools
sudo yum -y install git-all centos-relese-SCL python-setuptools python-setuptools-devel python-devel
sudo yum -y groupinstall "Development Tools"

#install pip
sudo easy_install pip

#clone proejct repo
git clone https://github.com/yehudash/SCE-Tirgul-2.git
cd SCE-Tirgul-2
