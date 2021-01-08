echo "a continuacion muestra las interfaces de wifi en caso de tener \n $(ifconfig wifi0 > practica7.txt && curl ifconfig.me >> practica7.txt)"
echo "a continuacion se mostrara las direcciones ip locales en la red $(nmap 192.168.15.1/24 >>practica7.txt)"
base64 < practica7.txt > practica7.1.txt
cp practica7.1.txt ./practica7.txt 
rm practica7.1.txt