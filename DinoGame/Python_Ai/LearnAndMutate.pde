void LearnAndMutate() {
    // Reset Varaibles 
    for (int i = 1; i < Object.length + 1; i++) {
      Object[i - 1] = new PVector(int(random(height - 67, height - 47)), i * (2000 / Object.length));
      ObjectType[i - 1] = "Cactus";
    }
  }
}
