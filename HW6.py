from vpython import*
G=6.673E-11


mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

def G_force(m, pos_vec):
    return -G * mass['earth'] * m / mag2(pos_vec) * norm(pos_vec)

class as_obj(sphere):
    def kinetic_energy(self):
        return 0.5 * self.m * mag2(self.v)
    def potential_energy(self):
        return - G * mass['sun'] * self.m / mag(self.pos)

scene = canvas(width=800, height=800, background=vector(0.5,0.5,0))
scene.lights = []

#sun = sphere(pos=vector(0,0,0), radius = radius['sun'], color = color.orange, emissive=True)

#scene.forward = vector(0, -1, 0)

local_light(pos=vector(0,0,0))
earth = as_obj(pos = vector(0,0,0), radius = radius['earth'], m = mass['earth'], texture={'file':textures.earth}, make_trail = False)

moon = as_obj(pos = vector(moon_orbit['r'], 0, 0), radius = radius['moon'], m = mass['moon'], v = vector(0, 0, -moon_orbit['v']))


stars = [moon]
dt=60
'''
stars = [earth, mars, halley]
dt=60*60*6
print(earth.potential_energy(), earth.kinetic_energy())
'''
while True:
    rate(1000)
    for star in stars:
        star.a = G_force(star.m, star.pos) / star.m
        star.v = star.v + star.a * dt
        star.pos = star.pos + star.v * dt

