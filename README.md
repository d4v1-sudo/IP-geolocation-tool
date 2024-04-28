## 🖥️ → 🔎 → 🗺️ - IP Geolocation Tool

This Python script utilizes the MaxMind GeoIP2 database to retrieve geolocation information for a given IP address.

### Prerequisites
- Python 3.x
- MaxMind GeoLite2 City and ASN databases (`GeoLite2-City.mmdb`, `GeoLite2-ASN.mmdb`)

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
### Download all MaxMind database for mor data:

[MaxMind GeoLite2 Database](https://github.com/P3TERX/GeoLite.mmdb)

### Disclaimer
This script relies on third-party data provided by MaxMind. The accuracy of the geolocation information may vary.

<a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2FIP-geolocation-tool"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2FIP-geolocation-tool&label=Thanks%20for%20dropping%20in&labelColor=%23000000&countColor=%23FFFFFF" /></a>
