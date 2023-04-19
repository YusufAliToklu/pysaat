import pygame
import time
import sys
pygame.init()

pencere_genislik = 800
pencere_yukseklik = 400
pencere = pygame.display.set_mode((pencere_genislik, pencere_yukseklik))
pygame.display.set_caption("2D Dijital Saat")

font = pygame.font.SysFont('calibri', 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    saat = time.strftime("%H:%M:%S")
    yazi_renk = (255, 255, 255)
    saat_yazi = font.render(saat, True, yazi_renk)

    pencere.fill((0, 0, 0))
    pencere.blit(saat_yazi, (pencere_genislik // 2 - saat_yazi.get_width() // 2, pencere_yukseklik // 2 - saat_yazi.get_height() // 2))

    pygame.display.update()
    time.sleep(1)
