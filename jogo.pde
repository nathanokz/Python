PImage papel, lixeira;
boolean arrastando = false;
float x, y;
void setup(){
  size(1366,768);
  papel=loadImage("papel.jpg");
  
  imageMode(CENTER);
  lixeira=loadImage("lixeira.jpg");
  x=width/2;
  y=height/2;
  textSize(16);
}

void draw(){
  background(255);
  image(papel,x,y);
  image(lixeira,683,600);
  fill(0);
  text("MouseX :" + mouseX,10,20);
  text("MouseY :"+ mouseY,10,40);
}

void mousePressed(){
  image(papel,x,y);
}
void mouseReleased(){
  if((mouseX>580) && (mouseX<780) && (mouseY>475) && (mouseY<710)) image(lixeira,1500,1500);
  arrastando = false;
}

void mouseDragged(){
  arrastando = true;
  x=mouseX;
  y=mouseY;
  image(papel,x,y);
}
  
