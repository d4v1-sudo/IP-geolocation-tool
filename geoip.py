import geoip2.database

def search_ip(ip_address):
    try:
        city_reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        asn_reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')

        city_response = city_reader.city(ip_address)
        asn_response = asn_reader.asn(ip_address)

        isp = city_response.traits.isp if city_response.traits.isp else "N/A"
        postal_code = city_response.postal.code if city_response.postal.code else "N/A"
        timezone = city_response.location.time_zone if city_response.location.time_zone else "N/A"

        single_ip_info = [
            ip_address,
            asn_response.autonomous_system_number,
            asn_response.autonomous_system_organization,
            isp,
            city_response.city.name if city_response.city.name else "N/A",
            city_response.subdivisions.most_specific.name if city_response.subdivisions.most_specific.name else "N/A",
            city_response.country.name,
            city_response.country.iso_code,
            postal_code,
            timezone,
            str(city_response.location.latitude),
            str(city_response.location.longitude),
            "https://www.google.com/maps/search/?api=1&query=" + str(city_response.location.latitude) + "," + str(city_response.location.longitude)
        ]

        city_reader.close()
        asn_reader.close()

        return single_ip_info
    except geoip2.errors.AddressNotFoundError:
        return None

def main():
    ip_address = input("IP: ")
    ip_info = search_ip(ip_address)
    if ip_info:
        print("IP Informations:")
        print("IP Address:", ip_info[0])
        print("AS Number:", ip_info[1])
        print("AS Name:", ip_info[2])
        print("ISP:", ip_info[3])
        print("City:", ip_info[4])
        print("Region:", ip_info[5])
        print("Country:", ip_info[6])
        print("Country Code:", ip_info[7])
        print("Postal Code:", ip_info[8])
        print("Timezone:", ip_info[9])
        print("Latitude:", ip_info[10])
        print("Longitude:", ip_info[11])
        print("Google Maps:", ip_info[12])
    else:
        print("IP address not found in database.")

if __name__ == "__main__":
    main()
