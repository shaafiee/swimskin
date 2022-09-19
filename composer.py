from PIL import Image, ImageDraw, ImageFilter
import random
import json







background = {1:"blue", 2:"wallpaper", 3:"gradient", 4:"green", 5:"purple", 6:"red", 7:"texture", 8:"yellow"}

backgroundPct = {0:0, 1:10, 2:2, 3:5, 4:10, 5:10, 6:10, 7:10, 8:10}



eye = {1:"black", 2:"blue", 3:"brown", 4:"burgundy", 5:"green", 6:"purple"}

eyePct = {0:0, 1:20, 2:30, 3:20, 4:10, 5:20, 6:5}



neck = {0:"none", 1:"light", 2:"thick"}

neckPct = {0:2, 1:40, 2:30}



color = {1:"gray", 2:"cobalt", 3:"brown", 4:"blonde", 5:"black", 6:"pink", 7:"gold"}

colorPct = {0:0, 1:20, 2:10, 3:20, 4:10, 5:30, 6:10, 7:10}



beard = {1:"garibaldi", 2:"goatee", 3:"pigtail", 4:"monk", 5:"full", 6:"curtain", 7:"van-dork", 8:"soul-patch", 9:"carnal", 10:"tails"}

beardPct = {1:10, 2:10, 3:10, 4:10, 5:20, 6:30, 7:10, 8:10, 9:5, 10:10}



moustache = {0:"none", 1:"barely", 2:"chevron", 3:"painters", 4:"english"}

moustachePct = {0:0, 1:20, 2:30, 3:30, 4:10}



groom = {1:"barber", 2:"scissors", 3:"shearer", 4:"trimmer"}

groomPct = {1:30, 2:20, 3:10, 4:30}



oil = {1:"argan", 2:"chocolate", 3:"lavender", 4:"musk", 5:"olive", 6:"rose", 7:"shea"}

oilPct = {1:20, 2:10, 3:10, 4:2, 5:20, 6:10, 7:10}





for i in range(1, 5556) :

	backgroundSel = 1
	eyeSel = 1
	neckSel = 0
	colorSel = 1
	beardSel = 5
	moustacheSel = 2
	groomSel = 1
	oilSel = 1



	image = ''
	metadata = {"name":"Okay Beard " + str(i), "description":"It's a bear market: time to grow a beard.", "image":"_url_", "attributes": list()}

	for key in background:
		r = random.randint(1,100)
		if r <= backgroundPct[key]:
			backgroundSel = key
			break;
	metadata["attributes"].append({"trait_type":"background", "value":background[backgroundSel]})

	for key in eye:
		r = random.randint(1,100)
		if r <= eyePct[key]:
			eyeSel = key
			break;
	metadata["attributes"].append({"trait_type":"eyes", "value":eye[eyeSel]})

	for key in neck:
		r = random.randint(1,100)
		if r <= neckPct[key]:
			neckSel = key
			break;
	metadata["attributes"].append({"trait_type":"neck hair", "value":neck[neckSel]})

	for key in color:
		r = random.randint(1,100)
		if r <= colorPct[key]:
			colorSel = key
			break;
	metadata["attributes"].append({"trait_type":"hair color", "value":color[colorSel]})

	for key in beard:
		r = random.randint(1,100)
		if r <= beardPct[key]:
			beardSel = key
			break;
	metadata["attributes"].append({"trait_type":"beard", "value":beard[beardSel]})

	for key in moustache:
		r = random.randint(1,100)
		if r <= moustachePct[key]:
			moustacheSel = key
			break;
	metadata["attributes"].append({"trait_type":"moustache", "value":moustache[moustacheSel]})

	for key in groom:
		r = random.randint(1,100)
		if r <= groomPct[key]:
			groomSel = key
			break;
	metadata["attributes"].append({"trait_type":"groom", "value":groom[groomSel]})

	for key in oil:
		r = random.randint(1,100)
		if r <= oilPct[key]:
			oilSel = key
			break;
	metadata["attributes"].append({"trait_type":"oil", "value":oil[oilSel]})




	img1 = Image.open('art/other/background.png')

	img2 = Image.open('art/eye/' + eye[eyeSel] + '_eyes.png')
	img1.paste(img2, (0, 0), img2)

	img2 = Image.open('art/other/eye_outline.png')
	img1.paste(img2, (0, 0), img2)
	
	img2 = Image.open('art/other/' + background[backgroundSel] + '_back.png')
	img1.paste(img2, (0, 0), img2)

	if neckSel > 0:
		img2 = Image.open('art/neck/' + neck[neckSel] + '.png')
		img1.paste(img2, (0, 0), img2)

	img2 = Image.open('art/other/overall_outline.png')
	img1.paste(img2, (0, 0), img2)


	img2 = Image.open('art/beard/' + color[colorSel] + '_' + beard[beardSel] + '.png')
	img1.paste(img2, (0, 0), img2)

	if moustacheSel > 0:
		img2 = Image.open('art/beard/' + color[colorSel] + '_' + moustache[moustacheSel] + '.png')
		img1.paste(img2, (0, 0), img2)

	img2 = Image.open('art/groom/' + groom[groomSel] + '.png')
	img1.paste(img2, (0, 0), img2)

	img2 = Image.open('art/oil/' + oil[oilSel] + '.png')
	img1.paste(img2, (0, 0), img2)






	f = open("/mnt/node/beards/meta/" + str(i), "w")
	f.write(json.dumps(metadata))
	f.close()

	img1.save("/mnt/node/beards/images/" + str(i) + ".png", format="png")



