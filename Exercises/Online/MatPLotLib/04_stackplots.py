from matplotlib import pyplot as plt
import random

plt.style.use("fivethirtyeight")

minutes = [n for n in range(1, 10, 1)]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ["Player 1", "Player 2", "Player 3"]
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, player1, player2, player3, labels= labels, colors= colors)

plt.title("Stack Chart")
plt.tight_layout()
plt.legend(loc= (0.07, 0.05))
plt.show()