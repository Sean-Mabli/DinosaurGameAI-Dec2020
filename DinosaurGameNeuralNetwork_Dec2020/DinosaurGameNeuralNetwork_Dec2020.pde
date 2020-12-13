Population Population;
int PopulationSize = 1000;

PrintWriter PrintToTxt;

PVector[] Object = new PVector[3];
String[] ObjectType = new String[3];
PVector[] Road = new PVector[50];
int ObjectWidth = 73; 
int ObjectHeight = 47;
float Gravity = 0.65;
int Speed = 8;
int OverallScore = 0;
int HighScore = 0;
float MutationRate = 0.1;
int Generation = 0;
int PopulationAlive = 0;

PImage DinoWalk;
PImage DinoDuck;
PImage Cactus;
PImage Bird;

void setup() {
  size(960, 540);

  DinoDuck = loadImage("DinoDuck004.png");
  DinoWalk = loadImage("DinoWalk002.png");
  Cactus = loadImage("Cactus001.png");
  Bird = loadImage("Bird002.png");

  Population = new Population(PopulationSize);

  for (int i = 1; i < Object.length + 1; i++) {
    Object[i - 1] = new PVector(int(random(height - 67, height - 47)), i * (2000 / Object.length));
    ObjectType[i - 1] = "Cactus";
  }
  for (int i = 0; i < Road.length; i++) {
    Road[i] = new PVector(int(random(height - 20, height)), int(random(0, width)));
  }

  PrintToTxt = createWriter("Weights.txt");
  RandomizeWeight();
}

void draw() {
  DinoGameRun();
  Display();
  PrintWeights();
  LearnAndMutate();
}

void RandomizeWeight() {
  for (int k = 0; k < PopulationSize; k++) {
    for (int j = 0; j < 4; j++) {
      for (int i = 0; i < 6; i++) {
        Population.NeuralNetworks[k].WeightInputToHidden1[i][j] = random(-1, 1);
      }
    }
    for (int j = 0; j < 6; j++) {
      for (int i = 0; i < 3; i++) {
        Population.NeuralNetworks[k].WeightHidden1ToOutput[i][j] = random(-1, 1);
      }
    }
  }
}

void PrintWeights() {
  if ((millis() % (60000 * 30)) < 20) {
    PrintToTxt.println(HighScore);
    PrintToTxt.println("double[][] WeightInputToHidden1 = {");
    PrintToTxt.print("{");
    for (int i = 0; i < 6; i++) {
      for (int j = 0; j < 4; j++) {
        PrintToTxt.print((float)Population.NeuralNetworks[1].WeightInputToHidden1[i][j] + ", ");
      }
      PrintToTxt.print("},");
      PrintToTxt.println();
      if (i != 5) {
        PrintToTxt.print("{");
      }
    }
    PrintToTxt.println("};");
    PrintToTxt.println();

    PrintToTxt.println("double[][] WeightHidden1ToOutput = {");
    PrintToTxt.print("{");
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 6; j++) {
        PrintToTxt.print((float)Population.NeuralNetworks[1].WeightHidden1ToOutput[i][j] + ", ");
      }
      PrintToTxt.print("},");
      PrintToTxt.println();
      if (i != 2) {
        PrintToTxt.print("{");
      }
    }
    PrintToTxt.println("};");
    PrintToTxt.println();
    PrintToTxt.flush();
    delay(20);
  }
}
