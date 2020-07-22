#!/bin/bash

function CriarDBPadrao(){
    #echo "Entre com a senha do usuario root do MYSQL(A senha nao aparecera enquanto voce escreve)"
    #read -sp rootpasswd
    dbname=EdPermanente
    username=db
    host=%
    password=L4bn3t
    query="GRANT ALL PRIVILEGES ON $dbname.* TO $username@'$host' IDENTIFIED BY '$password'";
    #mysql -e "CREATE DATABASE EdPermanente"
    #mysql -e "CREATE USER 'bd'@'%' IDENTIFIED BY 'L4bn3t'"
    #mysql -e "GRANT ALL PRIVILEGES ON EdPermanente.* to 'bd'@'%'"
    #mysql -e "FLUSH PRIVILEGES"
}


function DropDatabase(){
    echo "Entre com a senha do usuario root do MYSQL(A senha nao aparecera enquanto voce escreve)!"
    read -sp rootpasswd
    echo "Qual nome do database que deseja dropar?"
    read -p dbname
    mysql -uroot -p${rootpasswd} -e "DROP DATABASE $dbname;"
}

function CriarDBEUsuarioPersonalizado(){
    echo "Entre com a senha do usuario root do MYSQL(A senha nao aparecera enquanto voce escreve)!"
    read -sp rootpasswd
    echo "Entre com o nome do banco que deseja criar"
    read -p dbname
    echo "Entre com o nome do usuario"
    read -p username
    echo "%,ip ou hostname?"
    read host
    echo "Qual a senha do usuario?(A senha nao aparecera enquanto voce escreve)"
    read -sp userpasswd
    #query="GRANT ALL PRIVILEGES ON $dbname.* TO $username@'$host' IDENTIFIED BY '$password'";
    mysql -uroot -p${rootpasswd} -e "CREATE DATABASE ${dbname};"
    mysql -uroot -p${rootpasswd} -e "CREATE USER ${username}@${host} IDENTIFIED BY '${userpasswd}';"
    mysql -uroot -p${rootpasswd} -e "GRANT ALL PRIVILEGES ON ${dbname}.* TO '${username}'@'${host}';"
    mysql -uroot -p${rootpasswd} -e "FLUSH PRIVILEGES;"
}

loop=1
while [ $loop -eq 1 ]
do
    echo "O que deseja fazer?"
    echo "1- Criar o banco e o usuario padrao"
    echo "2- Criar um banco e usuario personalizado"
    echo "3- Apagar um banco de dados"
    read var

    if [ $var -eq 1 ];
    
    then
        echo "teste"
        CriarDBPadrao
    else
        if [ $var -eq 2 ];
        
        then
            CriarDBEUsuarioPersonalizado
        else
            if [ $var -eq 3 ]
            
            then
                DropDatabase
            else
                loop=0
            fi
        fi
    fi
done