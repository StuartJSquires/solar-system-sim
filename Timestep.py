def verlet_step(interacting_bodies):
	"""This function takes the position's and velocities of all bodies, steps them forward
	by half of the timestep, calculates and sums the accelerations due to all other bodies
	at the half step position, then fully steps the velocities forward by one timestep and
	the positions by another halfstep.

	"""
	for body in interacting_bodies: 
		body.position += (body.velocity) * (timestep) / 2

	for body in interacting_bodies:
		body.sum_of_accelerations = 0
		for interacting_body in interacting_bodies:
			if interacting_body != body:
				distance = body.position - interacting_body.position
				acceleration = (gravitational_constant * interacting_body.mass) / (distance)**2
				body.sum_of_accelerations += acceleration
	
	for body in interacting_bodies:
		body.velocity += (body.sum_of_accelerations * timestep)
		body.position += (body.velocity * timestep) / 2