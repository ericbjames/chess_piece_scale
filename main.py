import pygame
import os

pygame.init()

X = 720
Y = 720
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True
dt = 0
boxes = []

entity_folder = "entities/"

def image_loader(path: str):
    for filename in os.listdir(path):
        yield pygame.image.load(os.path.join(path, filename)).convert_alpha()

pieces = list(image_loader(entity_folder))

for piece in pieces:
    rect = piece.get_rect(center=(X//2, Y//2))
    boxes.append({"image": piece, "rect": rect, "movey": 0})  # Initialize rectangles and movement for each image

active_piece = None

def gravity(entity):
    entity['movey'] += .1  # how fast player falls
    worldy = 720  # assuming your world height
    ty = 20  # adjust this value according to your entity size
    if entity['rect'].y > worldy and entity['movey'] >= 0:
        entity['movey'] = 0
        entity['rect'].y = worldy - ty - ty - ty 

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box['rect'].collidepoint(event.pos):
                        active_piece = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_piece = None

        if event.type == pygame.MOUSEMOTION:
            if active_piece is not None:
                boxes[active_piece]['rect'].move_ip(event.rel)

        if event.type == pygame.QUIT:
            running = False

    # Apply gravity to each entity
    for box in boxes:
        gravity(box)
        box['rect'].move_ip(0, box['movey'])  # Move the entity vertically

    # Blit images onto the screen
    for box in boxes:
        screen.blit(box["image"], box["rect"])

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
