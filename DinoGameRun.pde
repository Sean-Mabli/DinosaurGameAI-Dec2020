void DinoGameRun() {
  // Object Position Updating/Genaration
  for (int i = 0; i < Object.length; i++) {
    Object[i].y += -Speed;
    if (Object[i].y < -ObjectWidth) {
      Object[i] = new PVector(int(random(height - 67, height - 47)), int(random(1000, 1600)));
      ObjectType[i] = "Cactus";

      // Set Over All Score
      int l = 0;
      for (int k = 0; k < PopulationSize && Population.NeuralNetworks[k].GameOver == true; k++) {
        l += 1;
      }
      if (l != PopulationSize) {
        OverallScore += 1;
      }

      // Change Cactus To Bird 20% Of The Time
      if (random(0, 1) < 0.2) {
        Object[i].x = int(random(height - 114, height - 74));
        ObjectType[i] = "Bird";
      }
    }
    if (i < Object.length - 1) {
      while (Object[i].y < Object[i + 1].y + 300 && Object[i].y + 300 > Object[i + 1].y) {
        Object[i].y = int(random(1000, 1600));
      }
    } else if (i == Object.length - 1) {
      while (Object[i].y < Object[0].y + 300 && Object[i].y + 300 > Object[0].y) {
        Object[0].y = int(random(1000, 1600));
      }
    }
  }

  for (int k = 0; k < PopulationSize; k++) {
    if (Population.NeuralNetworks[k].GameOver == false) {
      // Set Elf X Coordinates
      Population.NeuralNetworks[k].ElfX += Population.NeuralNetworks[k].ElfVol;
      Population.NeuralNetworks[k].ElfVol += Gravity;
      Population.NeuralNetworks[k].ElfX = constrain(Population.NeuralNetworks[k].ElfX, 0, height - Population.NeuralNetworks[k].ElfHeight);

      // Game Over Check
      for (int i = 0; i < Object.length; i++) {
        if (Population.NeuralNetworks[k].ElfX < Object[i].x + ObjectHeight && Population.NeuralNetworks[k].ElfX + Population.NeuralNetworks[k].ElfHeight > Object[i].x && 30 < Object[i].y + ObjectWidth  && 30 + Population.NeuralNetworks[k].ElfWidth > Object[i].y) {
          Population.NeuralNetworks[k].GameOver = true;
          Population.NeuralNetworks[k].Score = OverallScore;
        }
      }

      // Set Inputs
      if (Object[0].y < Object[1].y && Object[0].y < Object[2].y) {
        Population.NeuralNetworks[k].Input[0] = Object[0].y / 2000;
        if (ObjectType[0] == "Cactus") {
          Population.NeuralNetworks[k].Input[1] = 0;
        } else if (ObjectType[0] == "Bird") {
          Population.NeuralNetworks[k].Input[1] = 1;
        } 
        Population.NeuralNetworks[k].Input[2] = Object[1].y / 2000;
        if (ObjectType[1] == "Cactus") {
          Population.NeuralNetworks[k].Input[3] = 0;
        } else if (ObjectType[1] == "Bird") {
          Population.NeuralNetworks[k].Input[3] = 1;
        }
      } else if (Object[1].y < Object[0].y && Object[1].y < Object[2].y) {
        Population.NeuralNetworks[k].Input[0] = Object[1].y / 2000;
        if (ObjectType[1] == "Cactus") {
          Population.NeuralNetworks[k].Input[1] = 0;
        } else if (ObjectType[1] == "Bird") {
          Population.NeuralNetworks[k].Input[1] = 1;
        } 
        Population.NeuralNetworks[k].Input[2] = Object[2].y / 2000;
        if (ObjectType[2] == "Cactus") {
          Population.NeuralNetworks[k].Input[3] = 0;
        } else if (ObjectType[2] == "Bird") {
          Population.NeuralNetworks[k].Input[3] = 1;
        }
      } else if (Object[2].y < Object[0].y && Object[2].y < Object[1].y) {
        Population.NeuralNetworks[k].Input[0] = Object[2].y / 2000;
        if (ObjectType[2] == "Cactus") {
          Population.NeuralNetworks[k].Input[1] = 0;
        } else if (ObjectType[2] == "Bird") {
          Population.NeuralNetworks[k].Input[1] = 1;
        } 
        Population.NeuralNetworks[k].Input[2] = Object[0].y / 2000;
        Population.NeuralNetworks[k].Input[3] = (160 - Object[0].x) / 200;
        if (ObjectType[0] == "Cactus") {  
          Population.NeuralNetworks[k].Input[3] = 0;
        } else if (ObjectType[0] == "Bird") {
          Population.NeuralNetworks[k].Input[3] = 1;
        }
      }
      
      // Run Network
      for (int i = 0; i < 6; i++) {
        Population.NeuralNetworks[k].HiddenLayer1[i] = 0;
      }
      for (int i = 0; i < 3; i++) {
        Population.NeuralNetworks[k].Output[i] = 0;
      }

      for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
          Population.NeuralNetworks[k].HiddenLayer1[i] = Population.NeuralNetworks[k].WeightInputToHidden1[i][j] * Population.NeuralNetworks[k].Input[j] + Population.NeuralNetworks[k].HiddenLayer1[i];
        }
        Population.NeuralNetworks[k].HiddenLayer1[i] = 1 / (1 + Math.exp(-Population.NeuralNetworks[k].HiddenLayer1[i]));
      }

      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 6; j++) {
          Population.NeuralNetworks[k].Output[i] = Population.NeuralNetworks[k].WeightHidden1ToOutput[i][j] * Population.NeuralNetworks[k].HiddenLayer1[j] + Population.NeuralNetworks[k].Output[i];
        }
        Population.NeuralNetworks[k].Output[i] = 1 / (1 + Math.exp(-Population.NeuralNetworks[k].Output[i]));
      };

      // Complete Action Based On Output
      if (Population.NeuralNetworks[k].Output[0] > Population.NeuralNetworks[k].Output[1] && Population.NeuralNetworks[k].Output[0] > Population.NeuralNetworks[k].Output[2]) {
        // Do Nothing
      } else if (Population.NeuralNetworks[k].Output[1] > Population.NeuralNetworks[k].Output[0] && Population.NeuralNetworks[k].Output[1] > Population.NeuralNetworks[k].Output[2]) {
        // Jump
        if (Population.NeuralNetworks[k].ElfHeight == 26 && Population.NeuralNetworks[k].ElfWidth == 55) {
          Population.NeuralNetworks[k].ElfHeight = 43;
          Population.NeuralNetworks[k].ElfWidth = 40;
          Population.NeuralNetworks[k].ElfVol = -12;
          Population.NeuralNetworks[k].ElfX = height - 43;
        }
        if (Population.NeuralNetworks[k].ElfX == height - 43) {
          Population.NeuralNetworks[k].ElfVol = -12;
        }
      } else if (Population.NeuralNetworks[k].Output[2] > Population.NeuralNetworks[k].Output[0] && Population.NeuralNetworks[k].Output[2] > Population.NeuralNetworks[k].Output[1]) {
        // Duck
        if (Population.NeuralNetworks[k].ElfX == height - 43) {
          Population.NeuralNetworks[k].ElfHeight = 26;
          Population.NeuralNetworks[k].ElfWidth = 55;
        }
      }
    }
  }
}
