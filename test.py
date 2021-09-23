import requests

while True:
	print("MENU");
	print("1.Read All");
	print("2.Data of specific song")
	print("3.Rate the song")
	print("4.exit")
	choice = int(input("Enter the Choice: "));
	
	if choice==1:
		wa="http://127.0.0.1:8000/playlist_option/"
		res=requests.get(wa)
		data=res.json()
		print(data)

	elif choice==2:
		name=input("Enter the title of song: ")
		wa= "http://127.0.0.1:8000/playlist_option/" + name
		res=requests.get(wa)
		if res.status_code==404:
			print(r,' does not exist')
		else:
			data=res.json()
		print(data)

	elif choice==3:
		name=input("Enter the title of song: ")
		star_rating=int(input("Rate the song (out of5): "))
		play=({'star_rating':star_rating})
		wa="http://127.0.0.1:8000/playlist_option/"+name
		res=requests.put(wa,play)
		if res.status_code==404:
			print(r,'does not exist')
		else:
			data=res.json()
			print(data)
	elif choice==4:
		exit()
	else:
		print("Invalid choice")
			