#!/bin/bash

parrafo1="uno"
parrafo2="dos"
parrafo3=""

if [ $parrafo1 = $parrafo2 ]; then
    echo "\$parrafo1 es igual a \$parrafo2"

elif [ $parrafo1 != $parrafo2 ]; then
    echo "\$parrafo1 no es igual a \$parrafo2"
fi

if [ -z $parrafo3 ]; then
    echo "\$parrafo3 esta vacia"
fi