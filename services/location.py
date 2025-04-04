import geocoder

class Geolocation:
    def get_location(self):
        g = geocoder.ip("me")
        return g.latlng if g.ok else None
