# Create 2 array numpy:

#  Un array unidimensionale di numeri casuali compresi tra 0 e 1;</li>
#  Un array bidimensionale di dimensione 3x3 con valori interi casuali.
import numpy as np

# Array unidimensionale di numeri casuali compresi tra 0 e 1
array_unidimensionale = np.random.random(10)  # Ad esempio, 10 numeri casuali
print("Array unidimensionale:", array_unidimensionale)

# Array bidimensionale di dimensione 3x3 con valori interi casuali
array_bidimensionale = np.random.randint(0, 10, (3, 3))  # Valori interi casuali tra 0 e 9
print("Array bidimensionale:\n", array_bidimensionale)
