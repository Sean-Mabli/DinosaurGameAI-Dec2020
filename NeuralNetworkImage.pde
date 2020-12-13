void NeuralNetworkImage() {
  // Input Layer
  stroke(83);
  fill(83);
  circle(560, 220, 20);
  circle(560, 260, 20);
  circle(560, 300, 20);
  circle(560, 340, 20);
  // Hidden Layer 1
  circle(660, 180, 20);
  circle(660, 220, 20);
  circle(660, 260, 20);
  circle(660, 300, 20);
  circle(660, 340, 20);
  circle(660, 380, 20);
  // Output Layer
  circle(760, 240, 20);
  circle(760, 280, 20);
  circle(760, 320, 20);
  // Node Labels
  stroke(83);
  fill(83);
  textSize(20);
  text("Distance To Closest Object", 277, 225);
  text("Type of Closest Object", 318, 265);
  text("Distance To 2nd Closest Object", 232, 305);
  text("Type of 2nd Closest Object", 275, 345);
  
  text("Do Nothing", 780, 247);
  text("Jump", 780, 287);
  text("Duck", 780, 327);
  

  // Input To Hidden 1
  stroke(83);
  fill(83);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[0][0])); // Input Node 1 to Hidden Node 1
  line(660, 180, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[0][1])); // Input Node 2 to Hidden Node 1
  line(660, 180, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[0][2])); // Input Node 3 to Hidden Node 1
  line(660, 180, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[0][3])); // Input Node 4 to Hidden Node 1
  line(660, 180, 560, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[1][0])); // Input Node 1 to Hidden Node 2
  line(660, 220, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[1][1])); // Input Node 2 to Hidden Node 2
  line(660, 220, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[1][2])); // Input Node 3 to Hidden Node 2
  line(660, 220, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[1][3])); // Input Node 4 to Hidden Node 2
  line(660, 220, 560, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[2][0])); // Input Node 1 to Hidden Node 3
  line(660, 260, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[2][1])); // Input Node 2 to Hidden Node 3
  line(660, 260, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[2][2])); // Input Node 3 to Hidden Node 3
  line(660, 260, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[2][3])); // Input Node 4 to Hidden Node 3
  line(660, 260, 560, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[3][0])); // Input Node 1 to Hidden Node 4
  line(660, 300, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[3][1])); // Input Node 2 to Hidden Node 4
  line(660, 300, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[3][2])); // Input Node 3 to Hidden Node 4
  line(660, 300, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[3][3])); // Input Node 4 to Hidden Node 4
  line(660, 300, 560, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[4][0])); // Input Node 1 to Hidden Node 5
  line(660, 340, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[4][1])); // Input Node 2 to Hidden Node 5
  line(660, 340, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[4][2])); // Input Node 3 to Hidden Node 5
  line(660, 340, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[4][3])); // Input Node 4 to Hidden Node 5
  line(660, 340, 560, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[5][0])); // Input Node 1 to Hidden Node 6
  line(660, 380, 560, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[5][1])); // Input Node 2 to Hidden Node 6
  line(660, 380, 560, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[5][2])); // Input Node 3 to Hidden Node 6
  line(660, 380, 560, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightInputToHidden1[5][3])); // Input Node 4 to Hidden Node 6
  line(660, 380, 560, 340);
  // Hidden 1 to Output
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][0])); // Hidden Node 1 to Output Node 1
  line(760, 240, 660, 180);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][1])); // Hidden Node 2 to Output Node 1
  line(760, 240, 660, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][2])); // Hidden Node 3 to Output Node 1
  line(760, 240, 660, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][3])); // Hidden Node 4 to Output Node 1
  line(760, 240, 660, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][4])); // Hidden Node 5 to Output Node 1
  line(760, 240, 660, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[0][5])); // Hidden Node 6 to Output Node 1
  line(760, 240, 660, 380);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][0])); // Hidden Node 1 to Output Node 2
  line(760, 280, 660, 180);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][1])); // Hidden Node 2 to Output Node 2
  line(760, 280, 660, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][2])); // Hidden Node 3 to Output Node 2
  line(760, 280, 660, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][3])); // Hidden Node 4 to Output Node 2
  line(760, 280, 660, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][4])); // Hidden Node 5 to Output Node 2
  line(760, 280, 660, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[1][5])); // Hidden Node 6 to Output Node 2
  line(760, 280, 660, 380);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][0])); // Hidden Node 1 to Output Node 3
  line(760, 320, 660, 180);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][1])); // Hidden Node 2 to Output Node 3
  line(760, 320, 660, 220);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][2])); // Hidden Node 3 to Output Node 3
  line(760, 320, 660, 260);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][3])); // Hidden Node 4 to Output Node 3
  line(760, 320, 660, 300);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][4])); // Hidden Node 5 to Output Node 3
  line(760, 320, 660, 340);
  strokeWeight((float)(1 - Population.NeuralNetworks[0].WeightHidden1ToOutput[2][5])); // Hidden Node 6 to Output Node 3
  line(760, 320, 660, 380);
}
