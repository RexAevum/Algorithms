# Time - O(n*log n ) | Space - O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    # Sort both lists in desc order so that we can check which list has the tallest student for them to be in the back row
    redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	# check which class is in the back
	redInBack = True if redShirtHeights[0] > blueShirtHeights[0] else False
	
	i = 0
	while i < len(redShirtHeights):
		if redShirtHeights[i] == blueShirtHeights[i]:
			return False
		if redShirtHeights[i] < blueShirtHeights[i] and redInBack:
			return False
		if redShirtHeights[i] > blueShirtHeights[i] and not redInBack:
			return False
		i += 1
	return True