import pygame
import sys

pygame.init()

# গেম বোর্ডের প্রস্থ
WIDTH, HEIGHT = 800, 600

# রং
WHITE = (255, 255, 255)

# গেম বোর্ড তৈরি
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("চলমান গাড়ি গেম")

# গাড়ি রেক্টেঙ্গের প্রোপার্টি
carImg = pygame.image.load('car.png')
carRect = carImg.get_rect()

# গাড়ির গতি
car_speed = 5

# গাড়ির প্রারম্ভিক অবস্থান
carRect.centerx = WIDTH // 2
carRect.centery = HEIGHT // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # গেম বোর্ডে নির্দিষ্ট পরিসীমা রেখা
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        carRect.centerx -= car_speed
    if keys[pygame.K_RIGHT]:
        carRect.centerx += car_speed
    if keys[pygame.K_UP]:
        carRect.centery -= car_speed
    if keys[pygame.K_DOWN]:
        carRect.centery += car_speed

    # গাড়ির ছবিটি ড্রো করুন
    screen.blit(carImg, carRect)

    pygame.display.update()