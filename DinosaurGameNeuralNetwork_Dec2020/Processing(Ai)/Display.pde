void Display() {
  // Background
  background(255);
  strokeWeight(1);
  stroke(83);
  fill(83);
  line(-10, height - 20, 980, height - 20);

  for (int i = 0; i < Road.length; i++) {
    Road[i].y -= Speed;
    if (Road[i].y < 0) {
      Road[i] = new PVector(int(random(height - 20, height)), width);
    }
    stroke(83);
    rect(Road[i].y, Road[i].x, 1, 1);
  }

  // Objects
  for (int i = 0; i < Object.length; i++) {
    if (ObjectType[i] == "Cactus") {
      image(Cactus, Object[i].y, Object[i].x);
    } else if (ObjectType[i] == "Bird") {
      image(Bird, Object[i].y, Object[i].x);
    }
  }

  NeuralNetworkImage();

  for (int k = 0; k < PopulationSize; k++) {
    if (Population.NeuralNetworks[k].GameOver == false) {
      // Display Elf
      if (Population.NeuralNetworks[k].ElfHeight == 26 && Population.NeuralNetworks[k].ElfWidth == 55) {
        image(DinoDuck, 30, Population.NeuralNetworks[k].ElfX);
      } else if (Population.NeuralNetworks[k].ElfHeight == 43 && Population.NeuralNetworks[k].ElfWidth == 40) {
        image(DinoWalk, 30, Population.NeuralNetworks[k].ElfX);
      }
    }
  }

  // Display Info
  textSize(20);
  fill(83);
  text("Percent of Population Alive: " + PopulationAlive + " / " + PopulationSize, 550, 30);
  text("Generation: " + Generation, 550, 70);
  text("High Score: " + HighScore, 550, 110);
  text("Score: " + OverallScore, 550, 150);
}
