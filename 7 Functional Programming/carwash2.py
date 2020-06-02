#CAR WASH STALL
Amount1 = input("Please enter Wash amount")
amtpaid = int(Amount1)
def carwash(amtpaid):
	if (amtpaid >= 12):
		print("Wash with Tricolor foam")
		print("Rinse Twice")
		print("Dry with large blow Dryer")

	elif (amtpaid <= 12):
		print("Wash with white foam")
		print("Rinse once")
		print("Air Dry")

carwash(amtpaid)