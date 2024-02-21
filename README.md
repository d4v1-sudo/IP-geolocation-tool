## IP Geolocation Tool

This Python script utilizes the MaxMind GeoIP2 database to retrieve geolocation information for a given IP address.

### Prerequisites
- Python 3.x
- MaxMind GeoLite2 City and ASN databases (`GeoLite2-City.mmdb`, `GeoLite2-ASN.mmdb`)

### Installation
1. Download the MaxMind GeoLite2 City and ASN MMDB files from [MaxMind](https://dev.maxmind.com/geoip/geoip2/geolite2/) and place them in the same directory as the script.

### Usage
1. Run the script.
2. Enter the IP address you want to look up when prompted.

### Output
The script will provide the following information if the IP address is found:
- IP Address
- AS Number
- AS Name
- ISP
- City
- Region
- Country
- Country Code
- Postal Code
- Timezone
- Latitude
- Longitude
- Google Maps link to the location

### Example
```
IP: 8.8.8.8
IP Informations:
IP Address: 8.8.8.8
AS Number: 15169
AS Name: Google LLC
ISP: Google LLC
City: Mountain View
Region: California
Country: United States
Country Code: US
Postal Code: 94043
Timezone: America/Los_Angeles
Latitude: 37.4229
Longitude: -122.085
Google Maps: [Google Maps Link](https://www.google.com/maps/search/?api=1&query=37.4229,-122.085)
```

### Note
- If the IP address is not found in the database, the script will display a message indicating that the address was not found.

### Dependencies
- [geoip2](https://pypi.org/project/geoip2/) Python library, which can be installed via pip:

```
pip install geoip2
```

### Disclaimer
This script relies on third-party data provided by MaxMind. The accuracy of the geolocation information may vary.
