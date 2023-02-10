import GSA
GSA.authenticate()
playlist_id = input("Enter playlist URI: ")
GSA.getInformation(playlist_id, verbose=True)
