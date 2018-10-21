import random
import numpy as np
import matplotlib as plt

#If we have a 100 animals in the zoo all weighting from 1 to 6000kg. 
#What will be average weight of the animals if we select at random an animal and examine their weight
#n number of times. 
def generateRandom():
    # create an array of random weights
    animal_weights = []

    animal_weights.append(random.sample(range(4000, 6001), 7))
    animal_weights.append(random.sample(range(2500, 4000), 6))
    animal_weights.append(random.sample(range(800, 2500), 15))
    animal_weights.append(random.sample(range(100, 800), 20))
    animal_weights.append(random.sample(range(25, 100), 30))
    animal_weights.append(random.sample(range(1, 25), 22))
    
    #creates 1 single list
    flat_list_animals = [item for sublist in animal_weights for item in sublist]
    random.shuffle(flat_list_animals)
    
    return np.array(flat_list_animals)

def do_stats(animal_list):
    animal_mean = np.mean(animal_list)
    print(animal_mean)

if __name__ == '__main__':
    animals = generateRandom()
    do_stats(animals)

