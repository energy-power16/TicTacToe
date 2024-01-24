import pygame as pg
from random import randint

pg.init()
font = pg.font.SysFont("arial", 24)

side = 30
w = 17
h = 15
DISPLAYSURF = pg.display.set_mode((w * side, h * side))

BLACK = (0, 0, 0)
GREEN = (10, 255, 10)
RED = (255, 10, 10)

game_running = 0

dirs = [pg.K_RIGHT, pg.K_DOWN, pg.K_LEFT, pg.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0


def place_apple():
  a = (randint(0, w - 1), randint(0, h - 1))
  while a in snake:
    a = (randint(0, w - 1), randint(0, h - 1))
  return a


apple = place_apple()


def check_collisions():
  head = snake[-1]
  for i in range(len(snake) - 1):
    if head == snake[i]:
      return 2
  if head[0] >= w or head[0] < 0:
    return 3
  if head[1] >= h or head[1] < 0:
    return 3
  if head == apple:
    return 1
  return 0


clock = pg.time.Clock()
f = pg.font.SysFont('Avenir Heavy', 50, True)

points = 0
while True:
  clock.tick(4)
  for e in pg.event.get():
    if e.type == pg.QUIT:
      pg.quit()
      break
    if e.type == pg.KEYDOWN:
      if game_running == 0:
        game_running = 1
      if e.key == pg.K_SPACE:
        game_running = 0
        snake = [(7, 3), (7, 4)]
        direction = 0
        apple = place_apple()
      for i in range(4):
        if e.key == dirs[i] and direction != (i + 2) % 4:
          direction = i
  if game_running == 2:
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(f.render("Game over!", False, GREEN), (3 * side, 3 * side))
    DISPLAYSURF.blit(text, (0, 0))
    pg.display.update()
    game_running = 3
  if game_running == 3:
    continue
  snake.append((snake[-1][0] + dx[direction], snake[-1][1] + dy[direction]))
  coll = check_collisions()
  if coll >= 2:
    game_running = 2
    pass
  elif coll == 1:
    apple = place_apple()
    points += 1
    pass
  elif coll == 0:
    snake.pop(0)

  DISPLAYSURF.fill(BLACK)
  for i in range(len(snake)):
    pg.draw.rect(DISPLAYSURF, GREEN, pg.Rect(snake[i][0] * side, snake[i][1] * side, side, side))
  pg.draw.rect(DISPLAYSURF, RED, pg.Rect(apple[0] * side, apple[1] * side, side, side))
  text = font.render("Score: " + str(points), 0, (100, 15, 200))
  DISPLAYSURF.blit(text, (0, 0))
  pg.display.update()
