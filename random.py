import random
import math
import numpy as np
import matplotlib.pyplot as plt

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
    print("Mean weight of animal list: ", animal_mean)
    
    stand_dev = np.std(animal_list, dtype=np.float64)
    print("Standard deviation of animal list: ", stand_dev)
    
    stan_error_mean = stand_dev / (math.sqrt(len(animal_list)))
    print("Standard error of the mean: ", stan_error_mean)
    
    prob_of_elephants = len(animal_list) / 7
    print("Probability of randomly selecting an elephant or large animal over 4000kg: ", prob_of_elephants)
    
    np_random_means = np.array(calculate_random_means(animal_list))
    average_random_mean = np.average(np_random_means)
    print("Average mean of 20 random samples", average_random_mean)
    
#    num_bins = 20
#    plt.hist(random_list, num_bins, facecolor='blue')
#    plt.show()
    
def calculate_random_means(animal_list) :
    random_means = []
    for i in range(20):
        index = np.random.choice(animal_list.shape[0], 20, replace=False) 
        #creates a random list of 20 
        random_list = animal_list[index]
       
        random_mean = np.mean(random_list)
        random_means.append(random_mean)
        print("Mean of the random sample of the list", random_mean)
    return random_means

if __name__ == '__main__':
    animals = generateRandom()
    do_stats(animals)