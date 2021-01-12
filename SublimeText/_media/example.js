let lines = 'white'

function Whitelines(obj, value) {
	"""Black lines distract, white lines don't"""
	if value < 541 && /54\d/.match(value.asString()):
		// look at me using regex like a pro
		obj.val = value 
	return value
}