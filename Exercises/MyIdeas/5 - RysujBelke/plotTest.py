import matplotlib.pyplot as plt

class DrawingUtil():
    def __init__(self, min_cover, min_bar_dist, beam_height, beam_width, bar_fi, n_bars):
        self.min_cover = min_cover
        self.min_bar_dist = min_bar_dist
        self.beam_height = beam_height
        self.beam_width = beam_width
        self.bar_fi = bar_fi
        self.n_bars = n_bars

    def drawReinf(self):
        b_eff = self.beam_width - 2*self.min_cover

        if b_eff < (self.bar_fi*self.n_bars + self.min_bar_dist*(self.n_bars-1)):
            print("Impossible to fit bars into chosen cross-section!")

        fig = plt.figure(frameon=False)
        ax = fig.add_axes([0, 0, 1, 1])

        dist = (b_eff - self.n_bars*self.bar_fi)/(self.n_bars-1)

        print(F"Distances between bars: {round(dist + self.bar_fi, 2)}")

        from_edge = self.min_cover + self.bar_fi/2
        positions = [(from_edge + (dist + self.bar_fi)*_, self.beam_height-from_edge) for _ in range(self.n_bars)]

        beam = plt.Rectangle((0,0), self.beam_width, self.beam_height, edgecolor = "black", facecolor = "gray")
        ax.add_patch(beam)

        for _ in range(self.n_bars):
            bar = plt.Circle(positions[_], self.bar_fi/2, edgecolor = "black", facecolor = "red")
            ax.add_patch(bar)

        ax.axis("off")
        plt.axis("scaled")

        plt.show()

if __name__ == "__main__":
    beams = []

    beams.append(DrawingUtil(6, 3, 35, 70, 1.6, 8))

    beams[0].drawReinf()



