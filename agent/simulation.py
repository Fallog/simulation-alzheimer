import random
import pygame
from agent.Particle import Particle
from Grid import Grid


if __name__ == "__main__":
    pygame.init()

    width, height = 500, 500
    screen = pygame.display.set_mode((width, height), flags=pygame.SCALED)

    particles = [Particle(random.randint(0, width), random.randint(0, height), random.uniform(-1, 1),
                          random.uniform(-1, 1)) for _ in range(100)]

    clock = pygame.time.Clock()

    grid = Grid(width, height, 100, 100)
    grid.setup_grid()
    grid.fill_cells_with_particles(particles)

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

        pygame.display.set_caption(f"Individual Based Model Simulation\tFPS: {int(clock.get_fps())}")

        screen.fill(pygame.color.Color("white"))

        for p in particles:
            p.move()
            p.draw(screen)

        grid.collision_on_borders()

        grid.collision_inside_grid()

        grid.clear_cells()

        grid.fill_cells_with_particles(particles)

        pygame.display.flip()

        clock.tick(60)  # limitation des fps à 60

    pygame.quit()
