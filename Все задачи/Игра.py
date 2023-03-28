import tkinter
import random
import threading
import time


# Перемещение объекта
def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])

# Старт
def prepare_and_start():
    global player, exit, fires, enemies, __flag
    canvas.delete("all")

    # Спавн игрока и выхода
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    while exit_pos[0] == player_pos[0] or exit_pos[1] == player_pos[1]:
        exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]), 
        (player_pos[0] + step, player_pos[1] + step), 
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]), 
        (exit_pos[0] + step, exit_pos[1] + step), 
        fill='yellow')
    
    # Спавн огня
    N_FIRES = 6 
    fires = []
    fires_unique_check = []
    canvas.create_oval(
            (540, 60), 
            (540 + step, 60 + step), 
            fill='black')
    for _ in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        while fire_pos[0] == player_pos[0] or fire_pos[0] == exit_pos[0] or fire_pos[1] == player_pos[1] or fire_pos[1] == exit_pos[1] or fire_pos in fires_unique_check:
            fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]), 
            (fire_pos[0] + step, fire_pos[1] + step), 
            fill='red')
        fires_unique_check.append(fire_pos)
        fires.append(fire)

    # Спавн врагов
    N_ENEMIES = 1 #Число врагов
    enemies = []
    for _ in range(N_ENEMIES):
        enemy_pos = (random.randint(0, N_X - 1) * step, 
                     random.randint(0, N_Y - 1) * step)
        enemy = canvas.create_oval(enemy_pos, (enemy_pos[0] + step, enemy_pos[1] + step), fill='tomato')
        enemies.append((enemy, random.choice([always_right, random_move])))
    
    label.config(text="Найди выход!")
    __flag = True
    master.bind("<KeyPress>", key_pressed)


# Движение врагов    
def always_right():
    return (step, 0)
def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


# Бездействие функций
def do_nothing(x) -> None:
    pass

# Проверка положения игрока
def check_move():
    global __flag, __wins
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
        __flag = False
        __wins += 1
        label_wins.config(text=f"Победы подряд: {__wins}")
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
            __flag = False
            __wins = 0
            label_wins.config(text=f"Победы подряд: {__wins}")
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
            __flag = False
            __wins = 0
            label_wins.config(text=f"Победы подряд: {__wins}")

# Обработка клавиатуры пользователя
def key_pressed(event):
    print(event)
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(player, (0, step))
    if event.keysym == 'Right':
        move_wrap(player, (step, 0))
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    if canvas.coords(player)[1] == N_X * step:
        move_wrap(player, (0, -N_X * step))
    if canvas.coords(player)[0] == N_Y * step:
        move_wrap(player, (-N_Y * step, 0))
    if canvas.coords(player)[0] == -step:
        move_wrap(player, (N_Y * step, 0))
    if canvas.coords(player)[1] == -step:
        move_wrap(player, (0, N_X * step))
    check_move()


# SETTINGS
step = 60
N_X = 10
N_Y = 10


__flag = True # Играет ли игрок в данный момент
__wins = 0 # Победы подряд

# Движение игрока
def play_enemies():
    while True:
        if __flag:
            for enemy in enemies:
                direction = enemy[1]()
                place = [(step, 0), (-step, 0), (0, step), (0, -step)]
                if canvas.coords(enemy[0])[1] == 60:
                    place.remove((0, -step))
                if canvas.coords(enemy[0])[0] == 60:
                    place.remove((-step, 0))
                # if canvas.coords(enemy[0])[0] == 60:

                direction = random.choice(place)
                if canvas.coords(enemy[0])[0] == 540 and direction[0] == 60:
                    move_wrap(enemy[0], ())
                print(direction, canvas.coords(enemy[0]), step)
                if canvas.coords(enemy[0])[1] == N_X * step:
                    move_wrap(enemy[0], (0, -N_X * step))
                elif canvas.coords(enemy[0])[0] == N_Y * step:
                    move_wrap(enemy[0], (-N_Y * step, 0))
                elif canvas.coords(enemy[0])[0] == step:
                    move_wrap(enemy[0], (N_Y * step, 0))
                elif canvas.coords(enemy[0])[1] == step:
                    move_wrap(enemy[0], (0, N_X * step))
                else:
                    move_wrap(enemy[0], direction)
        time.sleep(2)

def main():
    global master, canvas, label, label_wins
    master = tkinter.Tk()
    label = tkinter.Label(master, text="Найди выход")
    label.pack()
    label_wins = tkinter.Label(master, text=f"Победы подряд: {__wins}")
    label_wins.pack()
    canvas = tkinter.Canvas(master, bg='blue', 
                            height=N_X * step, width=N_Y * step)
    canvas.pack()
    restart = tkinter.Button(master, text="Начать заново",
                            command=prepare_and_start)
    restart.pack()
    prepare_and_start()

    # Второй поток для автоматического движения врагов.
    thread = threading.Thread(target=play_enemies)
    thread.daemon = True
    thread.start()

    master.mainloop()

if __name__ == "__main__":
    main()
    
