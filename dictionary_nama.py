data_kue = {
    "Donut" : 5,
    "Bolu" : 8,
    "Brownies" : 4,
    "Tart" : 7,
    "Bagelen" : 8
}
print ("Menu Kue", data_kue)

data_kue["Roti"] = 10
data_kue["Brownies"] = 11
data_kue.pop("Tart")
print ("Menu Baru", data_kue)