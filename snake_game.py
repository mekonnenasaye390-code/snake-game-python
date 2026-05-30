import tkinter as tk
import random

# =========================
# ADVANCED SNAKE GAME
# Tkinter + User Controls
# =========================

WIDTH = 1000
HEIGHT = 400
SPACE_SIZE = 20
BODY_PARTS = 3
SPEED = 100

BACKGROUND_COLOR = "black"
SNAKE_COLOR = "lime"
FOOD_COLOR = "red"
TEXT_COLOR = "white"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([100, 100])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                outline="green"
            )

            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x,
            y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=FOOD_COLOR,
            tag="food"
        )


def next_turn():

    global score
    global food
    global running

    if not running:
        return

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x,
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR,
        outline="green"
    )

    snake.squares.insert(0, square)

    # Food Eat
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1

        score_label.config(text=f"Score: {score}")

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # Collision
    if check_collisions():
        game_over()
    else:
        window.after(SPEED, next_turn)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions():

    x, y = snake.coordinates[0]

    # Wall collision
    if x < 0 or x >= WIDTH:
        return True

    if y < 0 or y >= HEIGHT:
        return True

    # Body collision
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    global running

    running = False

    canvas.delete(tk.ALL)

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 - 40,
        font=("Arial", 40, "bold"),
        text="GAME OVER",
        fill="red"
    )

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 + 20,
        font=("Arial", 20),
        text="Press R to Restart",
        fill="white"
    )


def restart_game(event=None):

    global snake
    global food
    global score
    global direction
    global running

    canvas.delete(tk.ALL)

    score = 0
    direction = "down"
    running = True

    score_label.config(text=f"Score: {score}")

    snake = Snake()
    food = Food()

    next_turn()


# =========================
# MAIN WINDOW
# =========================

window = tk.Tk()

window.title("🐍 Snake Game")

window.resizable(False, False)

score = 0
direction = "down"
running = True

# Score label
score_label = tk.Label(
    window,
    text=f"Score: {score}",
    font=("Arial", 24, "bold"),
    fg=TEXT_COLOR,
    bg="black"
)

score_label.pack(fill=tk.X)

# Canvas
canvas = tk.Canvas(
    window,
    bg=BACKGROUND_COLOR,
    width=WIDTH,
    height=HEIGHT
)

canvas.pack()

# Keyboard Controls
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# WASD Controls
window.bind("a", lambda event: change_direction("left"))
window.bind("d", lambda event: change_direction("right"))
window.bind("w", lambda event: change_direction("up"))
window.bind("s", lambda event: change_direction("down"))

# Restart Key
window.bind("r", restart_game)

# Create Game
snake = Snake()
food = Food()

next_turn()

window.mainloop()