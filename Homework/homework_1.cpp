#include<iostream>

using namespace std;

int main(){
  float nevarro = 0, space = 0, carne = 0;
  float grasa = 0, proteinas = 0, carbohidratos = 0, calorias = 0;

  cout << "Nevarro Nummies consumidas (en unidades): "; cin >> nevarro;
  cout << "Space Soup consumida (en [ml]): "; cin >> space;
  cout << "Carne de rana consumida (en [g]): "; cin >> carne;

  grasa = ((1.9)*nevarro) + ((10/285)*space) + ((0.3/100)*carne);
  carbohidratos = ((6)*nevarro) + ((12/285)*space);
  proteinas = ((0.8)*nevarro) + ((11/285)*space) + ((16/100)*carne);

  calorias = (9*grasa) + (4*carbohidratos) + (4*proteinas);

  cout << "Goru ha consumido:" << endl;
  cout << grasa << " [g] de grasas" << endl;
  cout << carbohidratos << " [g] de carbohidratos" << endl;
  cout << proteinas << " [g] de proteinas";
  cout << "dando un total de" << endl;
  cout << calorias << " [calorias]" << endl;

  return 0;
}
