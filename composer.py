from PIL import Image, ImageDraw, ImageFilter
import random
import json
import os

path = "nft"
if not os.path.exists(path):
	os.makedirs(path)
path = "meta"
if not os.path.exists(path):
	os.makedirs(path)

background = {1: "beige watercolor", 2: "blue watercolor", 3: "gray watercolor", 4: "green watercolor", 5: "orange watercolor", 6: "pink watercolor", 7: "purple watercolor", 8: "violet watercolor", 9: "red watercolor", 10: "yellow watercolor", 11: "rainbow", 12: "sunset", 13: "bokeh", 14: "bricks", 15: "coffee", 16: "confetti", 17: "desert", 18: "feathers", 19: "galactic", 20: "icy", 21: "lava", 22: "leafy", 23: "maze", 24: "mosaic", 25: "old_school", 26: "sand", 27: "space", 28: "sprinkles", 29: "wood"}

backgroundPct = {0:0, 1:7, 2:7, 3:7, 4:7, 5:7, 6:7, 7:7, 8:7, 9:7, 10:7, 11:6, 12:6, 13:3, 14:3, 15:3, 16:3, 17:3, 18:3, 19:3, 20:3, 21:3, 22:3, 23:3, 24:3, 25:3, 26:3, 27:3, 28:3, 29:3}



swimsuit = {1: "air", 2: "bandeau", 3: "bondgirl", 4: "flounce", 5: "halterneck", 6: "micro thong", 7: "microkini", 8: "monokini", 9: "one piece", 10: "one shoulder", 11: "patch", 12: "pushup", 13: "ringed bikini", 14: "silhouette", 15: "skirt", 16: "sport band", 17: "sport suit", 18: "sport top", 19: "tied", 20: "triangle top", 21: "underwire", 22: "wetsuit", 23: "minikini"}

swimsuitPct = {0:0, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4, 14:4, 15:4, 16:4, 17:4, 18:4, 19:4, 20:4, 21:4, 22:4, 23:4}

swimsuitNavel = {0:True, 1:True, 2:True, 3:True, 4:True, 5:False, 6:False, 7:True, 8:False, 9:False, 10:False, 11:True, 12:True, 13:True, 14:False, 15:False, 16:False, 17:False, 18:True, 19:True, 20:True, 21:True, 22:False, 23:True}

swimsuitPelvic = {0:True, 1:False, 2:True, 3:False, 4:True, 5:True, 6:True, 7:False, 8:True, 9:True, 10:True, 11:True, 12:True, 13:False, 14:True, 15:False, 16:True, 17:True, 18:True, 19:True, 20:True, 21:True, 22:True, 23:False}

swimsuitBlockchain = {0:True, 1:True, 2:True, 3:False, 4:True, 5:True, 6:True, 7:False, 8:True, 9:True, 10:True, 11:True, 12:True, 13:True, 14:True, 15:True, 16:True, 17:True, 18:True, 19:True, 20:True, 21:True, 22:True, 23:True}

swimsuitCleavage = {0:True, 1:True, 2:True, 3:True, 4:False, 5:False, 6:True, 7:True, 8:True, 9:False, 10:False, 11:False, 12:True, 13:True, 14:False, 15:False, 16:True, 17:False, 18:True, 19:True, 20:True, 21:True, 22:False, 23:True}


swimsuitColor = {0: "", 1: "blue", 2: "red", 3: "gold", 4: "silver", 5: "green"}


lastUnique = 9
unique = {1: "angles", 2: "athlete", 3: "bourgeois", 4: "collars", 5: "cream", 6: "fifth element", 7: "koi", 8: "liquid", 9: "triad"}

uniqueNavel = {0:True, 1:False, 2:False, 3:True, 4:False, 5:True, 6:True, 7:True, 8:False, 9:False}

uniqueBlockchain = {0:True, 1:True, 2:True, 3:False, 4:True, 5:True, 6:False, 7:True, 8:True, 9:False}

uniqueCleavage = {0:True, 1:False, 2:True, 3:True, 4:False, 5:False, 6:True, 7:False, 8:False, 9:True}



blockchain = {0: "none", 1: "ethereum", 2: "solana", 3: "binance", 4: "bitcoin", 5: "cardano", 6: "dogecoin", 7: "algorand", 8: "flow", 9: "avalanche", 10: "tezos", 11: "tron", 12: "wax"}

blockchainPct = {0:0, 1:3, 2:3, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:3, 11:3, 12:3}



bodyArtifacts = {1: "light shadow", 2: "dark shadow", 3: "highlight", 4: "outline"}



body = {1: "brown", 2: "beige", 3: "beige athlete", 4: "bronze", 5: "bronze athlete", 6: "aqua", 7: "brown athlete", 8: "carbon android", 9: "ceramic android", 10: "cheetah", 11: "cherry", 12: "dark brown", 13: "dark brown athlete", 14: "fitness", 15: "gold", 16: "hulk", 17: "khaki", 18: "khaki athlete", 19: "lemon", 20: "silver", 21: "tigress"}

bodyPct = {0:0, 1:5, 2:5, 3:5, 4:4, 5:4, 6:2, 7:7, 8:2, 9:2, 10:2, 11:5, 12:7, 13:7, 14:6, 15:2, 16:2, 17:7, 18:7, 19:4, 20:4, 21:2}



bottom = {0: "none", 1: "blue fanny pack", 2: "green shorts", 3: "leather fanny pack", 4: "pink shorts", 5: "red fanny pack", 6: "sarong"}

bottomPct = {0:0, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2}

bottomBack = {1:True, 2:False, 3:True, 4:False, 5:True, 6:False}



navel = {0: "none", 1: "cherry", 2: "diamond", 3: "gold barbell", 4: "gold butterfly", 5: "gold filaments", 6: "gold ring", 7: "white gold butterfly"}

navelPct = {0:0, 1:2, 2:2, 3:2, 4:2, 5:4, 6:4, 7:4}


pelvic = {0: "none", 1: "biohazard", 2: "flame", 3: "ghost", 4: "leaf", 5: "pac", 6: "protoskin", 7: "puss", 8: "radioactive", 9: "skull", 10: "tongue"}

pelvicPct = {0:0, 1:6, 2:6, 3:6, 4:6, 5:6, 6:6, 7:6, 8:6, 9:6, 10:6}

# except swimsuit 22
neck = {0: "none", 1: "choker", 2: "diamond choker", 3: "heirloom"}

neckPct = {0:0, 1: 2, 2: 2, 3: 2}



longNecklace = {0: "no pendant", 1: "blue stone", 2: "bronze scroll", 3: "cherries", 4: "gold filaments", 5: "gold scroll", 6: "green stone", 7: "pink stone", 8: "silver scroll", 9: "yellow stone"}

longNecklacePct = {0:0, 1:3, 2:3, 3:3, 4:5, 5:5, 6:5, 7: 5, 8: 4, 9: 4}



shortNecklace = {0: "no pendant", 1: "bulb", 2: "cherries", 3: "gold filaments", 4: "gold lantern", 5: "silver filaments", 6: "silver lantern", 7: "wellness tool"}

shortNecklacePct = {0:0, 1:3, 2:3, 3:3, 4:5, 5:5, 6:5, 7: 3}



top = {0: "none", 1: "bag", 2: "buoy", 3: "denim backpack", 4: "fins", 5: "leather backpack", 6: "life jacket", 7: "silk shirt", 8: "snorkel mask", 9: "spear gun"}

topPct = {0:0, 1:5, 2:5, 3:5, 4:10, 5:10, 6:10, 7: 10, 8: 8, 9: 8}

topBack = {0:False, 1:True, 2:True, 3:True, 4:False, 5:True, 6:True, 7:False, 8:True, 9:True}







for i in range(1, 6) :

	backgroundSel = 1
	swimsuitSel = 1
	swimsuitColorSel = 0
	uniqueSel = 1
	isUnique = False
	blockchainInclude = False
	blockchainSel = 1
	bodySel = 1
	bottomSel = 0
	navelSel = 0
	neckSel = 0
	hasNecklace = False
	isLongNecklace = True
	goldNecklace = True
	necklaceLength = "long"
	necklaceColor = "gold"
	pendantSel = 0
	topSel = 0
	pelvicSel = 0

	longNecklaceSel = 0
	shortNecklaceSel = 0

	includeBlockchain = True
	includeNavel = True
	includeCleavage = True
	includePelvic = True



	image = ''
	metadata = {"name":"Swim.skin " + str(i), "description":"Advancing connections between technology and fashion.", "image":"_url_", "attributes": list()}


	for key in background:
		r = random.randint(1,100)
		if r <= backgroundPct[key]:
			backgroundSel = key
			break
	metadata["attributes"].append({"trait_type":"background", "value":background[backgroundSel]})

	r = random.randint(1,400)
	if (r <= 2) :
		isUnique = True

	if (isUnique) :
		if (lastUnique < 9) :
			lastUnique = lastUnique + 1
			uniqueSel = lastUnique
		else :
			isUnique = False

	r = random.randint(1,5)
	if (r <= 9) :
		swimsuitColorSel = r

	if (not isUnique) :
		for key in swimsuit:
			r = random.randint(1,100)
			if r <= swimsuitPct[key]:
				swimsuitSel = key
				break
		metadata["attributes"].append({"trait_type":"swimwear", "value":swimsuitColor[swimsuitColorSel] + " " + swimsuit[swimsuitSel]})
	else :
		metadata["attributes"].append({"trait_type":"swimwear", "value":unique[uniqueSel]})

	r = random.randint(1,100)
	if (r <= 60) :
		blockchainInclude = True
	
	if (blockchainInclude):
		for key in blockchain:
			r = random.randint(1,100)
			if r <= blockchainPct[key]:
				blockchainSel = key
				break
		metadata["attributes"].append({"trait_type":"blockchain", "value":blockchain[blockchainSel]})

	for key in body:
		r = random.randint(1,100)
		if r <= bodyPct[key]:
			bodySel = key
			break
	metadata["attributes"].append({"trait_type":"body", "value":body[bodySel]})

	for key in bottom:
		r = random.randint(1,100)
		if r <= bottomPct[key]:
			bottomSel = key
			break
	metadata["attributes"].append({"trait_type":"bottom", "value":bottom[bottomSel]})

	for key in navel:
		r = random.randint(1,100)
		if r <= navelPct[key]:
			navelSel = key
			break
	metadata["attributes"].append({"trait_type":"navel", "value":navel[navelSel]})

	for key in neck:
		r = random.randint(1,100)
		if r <= neckPct[key]:
			neckSel = key
			break
	metadata["attributes"].append({"trait_type":"neck", "value":neck[neckSel]})

	r = random.randint(1,100)
	if (r <= 50) :
		hasNecklace = True

	r = random.randint(1,100)
	if (r <= 40) :
		isLongNecklace = False
		necklaceLength = "short"

	r = random.randint(1,100)
	if (r <= 60) :
		goldNecklace = False
		necklaceColor = "silver"

	if (hasNecklace) :
		metadata["attributes"].append({"trait_type":"necklace", "value":necklaceLength + " " + necklaceColor})

		if (isLongNecklace) :
			for key in longNecklace:
				r = random.randint(1,100)
				if r <= longNecklacePct[key]:
					longNecklaceSel = key
					break
			metadata["attributes"].append({"trait_type":"pendant", "value":longNecklace[longNecklaceSel]})
		else :
			for key in shortNecklace:
				r = random.randint(1,100)
				if r <= shortNecklacePct[key]:
					shortNecklaceSel = key
					break
			metadata["attributes"].append({"trait_type":"pendant", "value":shortNecklace[shortNecklaceSel]})
	else :
		metadata["attributes"].append({"trait_type":"necklace", "value":"none"})
		metadata["attributes"].append({"trait_type":"pendant", "value":"none"})

	for key in top:
		r = random.randint(1,100)
		if r <= topPct[key]:
			topSel = key
			break
	metadata["attributes"].append({"trait_type":"top", "value":top[topSel]})

	for key in pelvic:
		r = random.randint(1,100)
		if r <= pelvicPct[key]:
			pelvicSel = key
			break
	metadata["attributes"].append({"trait_type":"pelvic", "value":pelvic[pelvicSel]})





	# background
	img1 = Image.open('images/background/' + background[backgroundSel].replace(" ", "_") + '.png')

	# bottom back
	if bottomSel > 0 and bottomBack[bottomSel] :
		img2 = Image.open('images/bottom/' + bottom[bottomSel].replace(" ", "_") + '_back.png')
		img1.paste(img2, (0, 0), img2)

	# top back
	if topSel > 0 and topBack[topSel] :
		img2 = Image.open('images/top/' + top[topSel].replace(" ", "_") + '_back.png')
		img1.paste(img2, (0, 0), img2)


	# body
	img2 = Image.open('images/body/' + body[bodySel].replace(" ", "_") + '.png')
	img1.paste(img2, (0, 0), img2)

	# body
	img2 = Image.open('images/body/' + body[bodySel].replace(" ", "_") + '.png')
	img1.paste(img2, (0, 0), img2)

	# swimwear
	if (isUnique) :
		img2 = Image.open('images/swimwear/unique/' + unique[uniqueSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)
		if not uniqueBlockchain[uniqueSel] :
			includeBlockchain = False
		if not uniqueNavel[uniqueSel] :
			includeNavel = False
		if not uniqueCleavage[uniqueSel] :
			includeCleavage = False
		includePelvic = False
	else :
		img2 = Image.open('images/swimwear/' + swimsuit[swimsuitSel].replace(" ", "_") + '/' + swimsuitColor[swimsuitColorSel] + '.png')
		img1.paste(img2, (0, 0), img2)
		if not swimsuitBlockchain[swimsuitSel] :
			includeBlockchain = False
		if not swimsuitNavel[swimsuitSel] :
			includeNavel = False
		if not swimsuitCleavage[swimsuitSel] :
			includeCleavage = False
		if not swimsuitPelvic[swimsuitSel] :
			includePelvic = False


	# blockchain
	if includeBlockchain and blockchainSel > 0:
		img2 = Image.open('images/blockchain/' + blockchain[blockchainSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)


	# body artifacts
	img2 = Image.open('images/body_artifacts/light_shadow.png')
	img1.paste(img2, (0, 0), img2)
	img2 = Image.open('images/body_artifacts/dark_shadow.png')
	img1.paste(img2, (0, 0), img2)
	img2 = Image.open('images/body_artifacts/highlight.png')
	img1.paste(img2, (0, 0), img2)
	img2 = Image.open('images/body_artifacts/outline.png')
	img1.paste(img2, (0, 0), img2)

	# cleavage
	if includeCleavage:
		img2 = Image.open('images/body_artifacts/cleavage.png')
		img1.paste(img2, (0, 0), img2)


	# pelvic
	if includePelvic and pelvicSel > 0:
		img2 = Image.open('images/pelvic/' + pelvic[pelvicSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)

	# bottom
	if bottomSel > 0:
		img2 = Image.open('images/bottom/' + bottom[bottomSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)

	# navel
	if includeNavel and navelSel > 0:
		img2 = Image.open('images/jewellery/navel/' + navel[navelSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)

	# necklace
	if hasNecklace:
		if isLongNecklace :
			if longNecklaceSel > 0:
				img2 = Image.open('images/jewellery/long_necklace/' + necklaceColor + '.png')
				img1.paste(img2, (0, 0), img2)
				img2 = Image.open('images/jewellery/long_necklace/pendant/' + longNecklace[longNecklaceSel].replace(" ", "_") + '.png')
				img1.paste(img2, (0, 0), img2)
		else :
			if shortNecklaceSel > 0:
				img2 = Image.open('images/jewellery/short_necklace/' + necklaceColor + '.png')
				img1.paste(img2, (0, 0), img2)
				img2 = Image.open('images/jewellery/short_necklace/pendant/' + shortNecklace[shortNecklaceSel].replace(" ", "_") + '.png')
				img1.paste(img2, (0, 0), img2)
	else :
		if neckSel > 0:
			img2 = Image.open('images/jewellery/neck/' + neck[neckSel].replace(" ", "_") + '.png')
			img1.paste(img2, (0, 0), img2)

	#top
	if topSel > 0:
		img2 = Image.open('images/top/' + top[topSel].replace(" ", "_") + '.png')
		img1.paste(img2, (0, 0), img2)















	f = open("./meta/" + str(i), "w")
	f.write(json.dumps(metadata))
	f.close()

	img1.save("./nft/" + str(i) + ".png", format="png")
	#img1.save("samples/" + str(i) + ".png", format="png")


	f = open("unique.txt", "w")
	f.write(str(lastUnique))
	f.close()
