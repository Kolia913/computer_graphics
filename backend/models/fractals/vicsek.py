import matplotlib.pyplot as plt


def draw_vicsek(ax, levels=4, x=0, y=0, size=1):
    if levels == 0:
        ax.add_patch(plt.Rectangle((x, y), size, size, color="black"))
    else:
        size3 = size / 3
        for i in range(3):
            for j in range(3):
                if i == 1 or j == 1:
                    draw_vicsek(ax, levels - 1, x + i * size3, y + j * size3, size3)


def get_vicsek_fractal(levels: int = 4):
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.axis("off")
    draw_vicsek(ax, levels=levels)

    return fig


def __main():
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.axis("off")
    draw_vicsek(ax, levels=2)
    plt.show()


if __name__ == "__main__":
    __main()
