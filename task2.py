import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.right(90)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.left(45)
        t.backward(length)

def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (0-10): "))
            if 0 <= level <= 10:
                break
            else:
                print("Будь ласка, введіть число від 0 до 10.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    length = 100  
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)  
    draw_pythagoras_tree(t, length, level)
    screen.mainloop()

if __name__ == "__main__":
    main()
