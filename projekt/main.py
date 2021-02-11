from program_loop import *

if __name__ == "__main__":
    #option = "greedy"
    option = "brute"
    boxes = random_Boxes()
    container = Container(CONTAINER_WIDTH, CONTAINER_HEIGHT, black, CONTAINER_X, CONTAINER_Y)
    print_Boxes(boxes)
    program_loop(container, boxes, option)


