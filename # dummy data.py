# dummy data 
data = [{'nama': "daffa", "umur": 20, "lokasi": "jakarta", 'absen': 3},
        {'nama': "erfe", "umur": 23, "lokasi": "jakarta"},
        {'nama': "saaa", "umur": 24, "lokasi": "jakarta"},
        {'nama': "fdfda", "umur": 44, "lokasi": "medan"}
        ]

from tabulate import tabulate
print(tabulate(data, headers = 'keys', tablefmt= 'pretty'))










}