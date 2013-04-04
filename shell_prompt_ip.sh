export PS1="[\u@`ifconfig eth0|grep 'inet addr'|sed -e 's/^.*inet addr:        \(.*\) Bcast.*$/\1/'`\h \W]$ "
