# solar-system-sim

This is an n-body solar system simulation. It takes in json files containing orbital parameters of planets (and moons),
and outputs csv files with the positions and velocities over time. A separate utility is used to build frames and 
animate the motion of the planets. This is nearly finished, but there is a major bug where one component of the velocity
is way too high. If the planets all lie in a plane, the simulation works perfectly. See [here](https://www.youtube.com/watch?v=omqPFv7Inds) for a demonstration video.

This was build during Summer 2015 by Stuart Squires, Miles Kopala, and Dylan Johnston.
