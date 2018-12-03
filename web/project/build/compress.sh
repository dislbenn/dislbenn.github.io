#!/bin/bash

echo -e "\033[0;36mBEGINNING FILE COMPRESSION\033[0m"
echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
sleep 2
while true
do
    if [ -d ./logs ]
    then
        echo -e "\033[0;35mINITIALIZING DIRECTORY SEARCH\033[0m"
        sleep 1.5

        echo -e "\033[0;33mLOG DIRECTORY SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.log ]
        then
            echo -e "LOG File Detected:\n"
            sleep 2
            ls ./*.log
            sleep 3
            echo -e "Compressing LOG Files in LOG Directory..\n"
            if [ ./logs.tar ]
            then

                echo -e "FILE ALREADY EXIST!\n"
                ls ./logs.tar
                echo -e "REMOVING OLD FILE\n"
                sleep 2
                rm -r logs.tar
                sleep 1.5
                echo -e "FILE REMOVED SUCCESSFULLY\n"
            fi
            
            mv ./*.log logs
            tar -cvf logs.tar logs
            echo -e "logs.tar created"
            echo -e "Files Compression Was Successful!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No LOG Files Were Found!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break

    else
        echo -e "\033[0;33mLOG DIRECTORY NOT DETECTED\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        break
    fi
done

while true
do
    if [ -d ./csv ]
    then
        echo -e "\033[0;35mINITIALIZING DIRECTORY SEARCH\033[0m"
        sleep 1.5

        echo -e "\033[0;33mCSV DIRECTORY SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.csv ]
        then
            echo -e "CSV File Detected:\n"
            sleep 2
            ls ./*.csv
            sleep 3
            echo -e "Compressing CSV Files in CSV Directory..\n"
            if [ ./csv.tar ]
            then
                echo -e "FILE ALREADY EXIST!\n"
                ls ./csv.tar
                echo -e "REMOVING OLD FILE\n"
                sleep 2
                rm -r csv.tar
                sleep 1.5
                echo -e "FILE REMOVED SUCCESSFULLY\n"
            fi

            tar -cvf csv.tar csv
            echo -e "Files Compression Was Successful!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No CSV Files Were Found!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break

    else
        echo -e "\033[0;33mCSV DIRECTORY NOT DETECTED\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        break
    fi
done
