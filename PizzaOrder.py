avaible_topies = ["mushrooms", "olives", "onion", "green peppers", "pepproni","pinaple", "extra cheese"]
cutomer_orders = ["mushrooms", "onion", "pepproni", "chicken"]
for cutomer_order in cutomer_orders:
	if cutomer_order in avaible_topies:
		print("adding " + cutomer_order + ".")
	else:
		print("SOrry, we don't have "+cutomer_order)
