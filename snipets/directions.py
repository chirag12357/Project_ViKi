from geolocation.main import GoogleMaps

if __name__ == "__main__":
    address = "mahadevapura"

    google_maps = GoogleMaps(api_key='AIzaSyDDOFM2C1pNvnl2L-224Ql4jjINC_KLGJU')

    location = google_maps.search(location=address)

    print(location.all())

    my_location = location.first()

    print(my_location.city)
    print(my_location.route)
    print(my_location.street_number)
    print(my_location.postal_code)

    for administrative_area in my_location.administrative_area:
        print("%s: %s" % (administrative_area.area_type, administrative_area.name))

    print(my_location.country)
    print(my_location.country_shortcut)

    print(my_location.formatted_address)

    print(my_location.lat)
    print(my_location.lng)
