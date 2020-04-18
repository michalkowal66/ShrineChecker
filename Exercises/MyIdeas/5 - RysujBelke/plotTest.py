import matplotlib.pyplot as plt

def drawReinf(min_cover, min_bar_dist, beam_height, beam_width, bar_fi, number_of_bars, effective_width):
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])

    dist = (b_eff - bars_n*fi)/(bars_n-1)

    print(F"Distances between bars: {round(dist + bar_fi, 2)}")

    from_edge = cmin + fi/2
    positions = [(from_edge + (dist + fi)*_, height-from_edge) for _ in range(bars_n)]

    beam = plt.Rectangle((0,0), width, height, edgecolor = "black", facecolor = "gray")
    ax.add_patch(beam)

    for _ in range(bars_n):
        bar = plt.Circle(positions[_], fi/2, edgecolor = "black", facecolor = "red")
        ax.add_patch(bar)

    ax.axis("off")
    plt.axis("scaled")

    plt.show()

#User defined values:
cmin = 6
cp = 3
height = 45
width = 250
fi = 1.6
bars_n = 14

b_eff = width - 2*cmin

if b_eff < (fi*bars_n + cp*(bars_n-1)):
    print("Impossible to fit bars into chosen cross-section!")
else:
    drawReinf(cmin, cp, height, width, fi, bars_n, b_eff)




