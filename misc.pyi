import pygame

# string stuff
print(f'Hi, {name}')

# mouse stuff
self.rect.center = pygame.mouse.get_pos()

# mask stuff
self.mask = pygame.mask.from_surface(self.image) # self.mask is usually in a class that inherits from pygame.sprite.Sprite

if pygame.sprite.spritecollide(thing1, group, dokill=false,pygame.sprite.collide_mask): # check mask collision
    # do stuff