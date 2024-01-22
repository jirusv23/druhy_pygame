import sys, pygame
pygame.init()

rozliseni_okna = (1000, 1000)
okno = pygame.display.set_mode(rozliseni_okna)
barva_okna = (0,0,255)

barva_hrace = (255,0,0)
velikost_hrace = 5
rychlost_hrace = 10/(velikost_hrace/10)
pozice_hrace_x = 100
pozice_hrace_y = 100

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    stiknute_klavesy = pygame.key.get_pressed()        
    
    if stiknute_klavesy[pygame.K_UP]:
        pozice_hrace_y -= rychlost_hrace
    if stiknute_klavesy[pygame.K_DOWN]:
        pozice_hrace_y += rychlost_hrace
    if stiknute_klavesy[pygame.K_LEFT]:
        pozice_hrace_x -= rychlost_hrace
    if stiknute_klavesy[pygame.K_RIGHT]:
        pozice_hrace_x += rychlost_hrace
    
    if pozice_hrace_x >= rozliseni_okna[0] - velikost_hrace:
        pozice_hrace_x = rozliseni_okna[0] - velikost_hrace
    
    
    okno.fill(barva_okna)    
    pygame.draw.rect(okno, barva_hrace, (pozice_hrace_x, pozice_hrace_y, velikost_hrace, velikost_hrace))    
    pygame.display.update()
            
    