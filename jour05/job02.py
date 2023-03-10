def draw_rectangle(width,height):
    print("|", "-"*width, "|")
    for _ in range(2,height):
        print(f"|"," "*width,"|")
    print("|", "-"*width, "|")

draw_rectangle(10,3)