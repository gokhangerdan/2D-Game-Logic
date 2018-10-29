import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

pos_x = 0
pos_y = 0
moving_speed = 10

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: pos_x += moving_speed
        if pressed[pygame.K_UP]: pos_y -= moving_speed
        if pressed[pygame.K_LEFT]: pos_x -= moving_speed
        if pressed[pygame.K_DOWN]: pos_y += moving_speed

        if pos_x < 0: pos_x = 0
        if pos_x > 470: pos_x = 470
        if pos_y < 0: pos_y = 0
        if pos_y > 470: pos_y = 470

        print(pos_x, pos_y)

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(pos_x, pos_y, 30, 30))

        pygame.display.flip()
        clock.tick(60)
