
import geocoder
g = geocoder.ip('me')

print(g.latlng)
print('--------------')
print(g.city)