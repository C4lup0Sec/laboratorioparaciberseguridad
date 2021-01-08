#!/bin/bash
history | tail -n 1
var0 = 0
if  ["$?" != $var0]
then 
    echo "existe un error"
    mail -s "Error en el ultimo comando" usuario1@mail.com
    exit 1
fi
