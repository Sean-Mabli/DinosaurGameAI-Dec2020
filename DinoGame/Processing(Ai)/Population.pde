class Population {
  NeuralNetwork[] NeuralNetworks;

  Population(int PopulationSize) {
    NeuralNetworks = new NeuralNetwork[PopulationSize];
    for (int i = 0; i < NeuralNetworks.length; i++) {
      NeuralNetworks[i] = new NeuralNetwork();
    }
  }
} 

class NeuralNetwork {
  int ElfWidth = 40; 
  int ElfHeight = 43;
  float ElfVol = 0;
  float ElfX = height - ElfHeight;
  int Score = 0;
  boolean GameOver = false;
  
  double[] Input = {0, 0, 0, 0};
  double[] HiddenLayer1 = {0, 0, 0, 0, 0, 0};
  double[] Output = {0, 0, 0};

  double[][] WeightInputToHidden1 = {
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
    {0, 0, 0, 0}, 
  };  
  double[][] WeightHidden1ToOutput = {
    {0, 0, 0, 0, 0, 0}, 
    {0, 0, 0, 0, 0, 0}, 
    {0, 0, 0, 0, 0, 0}, 
  };
}
