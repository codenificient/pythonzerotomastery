#at the carwash
def carwash(amtpaid):
	if (amtpaid >= 12):
		print("Wash with Tricolor foam")
		print("Rinse Twice")
		print("Dry with large blow Dryer")

	elif (amtpaid <= 12):
		print("Wash with white foam")
		print("Rinse once")
		print("Air Dry")

carwash(13)