ConDNAdo
====================

Que es?
---------------------

Un pequeño programa Python que genera una interfaz
donde se puede especificar:

+ el archivo de origen
+ el formato del archivo de origen
+ el archivo destino
+ el formato del archivo destino
 
 La conversion es realizada usando Biopython.
 
Cómo lo uso en Linux?
---------------------
 
 Estos son los comandos que deberias ejecutar para poder usarlo en Ubuntu 11.04:

    sudo aptitude install python-virtualenv
    
    mkdir condnado
    cd condnado
    virtualenv --no-site-packages -p python2.6 virtualenv 
    ./virtualenv/bin/pip  install numpy
    ./virtualenv/bin/pip  install biopython
    wget -O ConDNAdo.tgz https://github.com/hgdeoro/ConDNAdo/tarball/master
    tar xzf ConDNAdo.tgz
    ./virtualenv/bin/python hgdeoro-ConDNAdo-*/convert.py
 
Cómo lo uso en Window$?
---------------------
