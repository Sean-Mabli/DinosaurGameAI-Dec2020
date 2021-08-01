void LearnAndMutate() {
    // Mutate
    for (int k = 1; k < Population.NeuralNetworks.length; k++) {
      for (int m = 0; m < int(MutationRate * 24); m++) {
        Population.NeuralNetworks[k].WeightInputToHidden1[int(random(0, 6))][int(random(0, 4))] = random(-1, 1);
      }
      for (int m = 0; m < int(MutationRate * 18); m++) {
        Population.NeuralNetworks[k].WeightHidden1ToOutput[int(random(0, 3))][int(random(0, 6))] = random(-1, 1);
      }
    }  

    // Set High Score
    if (OverallScore > HighScore) {
      HighScore = OverallScore;
    }

    // Reset Varaibles 
    for (int i = 1; i < Object.length + 1; i++) {
      Object[i - 1] = new PVector(int(random(height - 67, height - 47)), i * (2000 / Object.length));
      ObjectType[i - 1] = "Cactus";
    }

    OverallScore = 0;

    for (int k = 0; k < PopulationSize; k++) {
      Population.NeuralNetworks[k].ElfWidth = 40; 
      Population.NeuralNetworks[k].ElfHeight = 43;
      Population.NeuralNetworks[k].ElfVol = 0;
      Population.NeuralNetworks[k].ElfX = height - Population.NeuralNetworks[k].ElfHeight;
      Population.NeuralNetworks[k].Score = 0;
      Population.NeuralNetworks[k].GameOver = false;
    }

    // Other
    Generation += 1;
  }
}
