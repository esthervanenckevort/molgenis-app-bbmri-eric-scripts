# BBMRI-ERIC Directory Validation Scripts
## Requirements
- Python 3.6
- The following python packages:
  - networkx
  - geopy
  - validate_email
  - xlsxwriter
  - py3dns
  - requests
  - diskcache
  - yapsy

## Installation
- Verify installation:  
  ``
python3 -m ensurepip
``
- For each of the above packages `pip3  install --upgrade <package>`
- Ensure that file `/etc/resolve.conf` exists. If it does not exist create it with the following contents:  
  ``
nameserver 8.8.8.8
``
- Create the diskcache directories:  
  ``
mkdir -p data-quality-cache/directory
mkdir -p data-quality-cache/geolocator
mkdir -p data-quality-cache/emails
``	
- Download the MOLGENIS Python API library:  
  ``
pip3 install molgenis-py-client
``
- Install/update root certificates (also check install_certifi.py script)  
  ``
pip3 install --upgrade certifi
``
- If you want support for checking mappings of ORPHA codes to ICD-10 codes for RD biobanks, you need to get en_product1.xml from
  http://www.orphadata.org/cgi-bin/ORPHAnomenclature.html

## Running the script

The simples way to run is like this:  
``
python3 data-check.py
``

If you want to purge all caches (directory as well as remote checks) and output the results to both stdout and XLSX, use:  
``
python3 data-check.py --purge-all-caches -X test_results.xlsx
``

If you want to purge just the directory cache and output just to XLSX, and be a little bit more verbose use:  
``
python3 data-check.py -v --purge-cache directory -N -X test_results.xlsx
``

If you have en_product1.xml with ORPHA code mappings, you run the extended checks using  
``
python3 data-check.py -O en_product1.xml
``

If you need to debug what the heck is happening...  
``
python3 data-check.py -d --purge-all-caches
``

# Additional helper scripts

- **get-contacts.py** - contact generator for use in Negotiator invitation pipeline  
``
./get-contacts.py --purge-all-caches -X contacts.xlsx
``
- **covid-exporter.py** - statistics generator for COVID-19 biobanks
- **mission-cancer-exporter.py** - statistics generator for cancer biobanks
- **diagnosis-exporter.py** - dumper of diagnosis information from the directory, used for development purposes only  
``
./diagnosis-exporter.py -d >diagnosis-exporter.log 2>&1
``
