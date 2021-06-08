d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:\
    print('kunci tidak ditemukan di dictionary')
except ValueError:\
    print('nilai tidak sesuai')

try:
    print('rata-rata: {}'.format(d['ratarata'] / 3))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')
try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:
    print('penangan kesalahan: {}'.format(e))
