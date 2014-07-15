"""
A Space Travel function using itertools.starmap.
"""

import world
import itertools

def space_voyage(spaceport, ship_ids, destination):
   	if world.exists(destination):
		params = []
		for id in ship_ids:
			if spaceport.queryHangar(id).isReady():
				params.append(id, destination)
		if len(params) > 0:
			return itertools.starmap(spaceport.launch, params)
		else:
			raise spaceport.NoShipsReadyException()
	else:
		raise world.DestinationException()
