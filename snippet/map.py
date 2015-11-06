def array_of_dict( array, key ):
	if isinstance( key, list ):
		return tree_array_of_struct( array, key )
	result = {}
	for a in array:
		result[ a[key] ] = a
	return result

def tree_array_of_struct( array, keys ):
	result = {}
	l_keys = len( keys )
	for a in array:
		aux_map = result
		for i in range( l_keys ):
			if a[ keys[i] ] in aux_map:
				aux_map = aux_map[ a[ keys[i] ] ]
				if i == l_keys-1:
					aux_map[ a[ keys[i] ] ] = a
			else:
				if i == l_keys-1:
					aux_map[ a[ keys[i] ] ] = a
				else:
					aux_map[ a[ keys[i] ] ] = {}
	return result
