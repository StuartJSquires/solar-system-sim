def verlet_step(interacting_bodies):

	for body in interacting_bodies:
		position = np.copy(body.position)
		
		for interacting_body in interacting_bodies:
			if interacting_body != body:
				second_position = np.copy(interacting_body.position)
				
				distance = position - second_position

				
