#!/bin/bash

echo -e "\033[0;36mBEGINNING LOG CLEAN\033[0m"
echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
sleep 2
while true
do
    if [ -d ./logs ]
    then
        echo -e "\033[0;35mINITIALIZING FILE SEARCH\033[0m"
        sleep 1.5

        echo -e "\033[0;33mLOG FILE SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.log ]
        then
            echo -e "LOG File Detected:\n"
            sleep 2
            ls ./*.log
            sleep 3
            echo -e "Moving LOG Files to LOG Directory..\n"
            mv ./*.log ./logs
            echo -e "Files Successfully moved!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No LOG Files Were Found!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break

    else
        mkdir logs
        echo -e "\033[0;31mDIRECTORY CREATED\033[0m"
        echo -e "\033[0;35mINITIALIZING FILE SEARCH\033[0m"
        sleep 1.5
    
        echo -e "\033[0;33mLOG FILE SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.log ]
        then
            echo -e "LOG File Detected:\n"
            sleep 2
            ls ./*.log
            sleep 3
            echo -e "Moving LOG Files to LOG Directory..\n"
            mv ./*.log ./logs
            echo -e "Files Successfully moved!"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No LOG Files Were Found!"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break
    fi
done
