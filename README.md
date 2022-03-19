# Wi-Fi Password Exporter
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Wi-Fi password exporter for windows OS.  
It will allow you to export the passwords of Wi-Fis your device has connected to a CSV file simply.

## How to use it
Just run it with Python 3. Then wait until it finishes.  
The results will be exported to `WifiPasswordList.csv`.

## How it works
The script uses the shell command `netsh` to export the Wi-Fi configurations.  
Then the script parses the files and extracts the SSIDs and passwords, exporting them to a CSV file `WifiPasswordList.csv`.  
(Some temporary files will be generated during the process, which will be cleared when finished.)  
Note that for those hotspots which have no passwords, the information will not be exported to the CSV file.
