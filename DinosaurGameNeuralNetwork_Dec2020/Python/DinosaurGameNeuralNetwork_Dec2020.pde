Population Population;
int PopulationSize = 1000;

PVector[] Object = new PVector[3];
String[] ObjectType = new String[3];
int ObjectWidth = 80; 
int ObjectHeight = 40;
float Gravity = 0.65;
int Speed = 8;
int OverallScore = 0;
int HighScore = 0;
float MutationRate = 0.1;
int Generation = 0;
int PopulationAlive = 0;

void setup() {
  Population = new Population(PopulationSize);

  for (int i = 1; i < Object.length + 1; i++) {
    Object[i - 1] = new PVector(int(random(height - 67, height - 47)), i * (2000 / Object.length));
    ObjectType[i - 1] = "Cactus";
  }
  for (int i = 0; i < Road.length; i++) {
    Road[i] = new PVector(int(random(height - 20, height)), int(random(0, width)));
  }
}

void draw() {
  DinoGameRun();
  LearnAndMutate();
}