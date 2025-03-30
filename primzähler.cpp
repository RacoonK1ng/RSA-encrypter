#include <iostream>
#include <fstream>
#include <vector>

int main() {
    int max = 1;
    std::cout << "Limit: ";
    std::cin >> max;

    std::vector<bool> ist_prim(max, true);
    ist_prim[0] = ist_prim[1] = false; // 0,1 sind keine Primzahlen

    for (int p = 2; p * p < max; ++p) {
        if (ist_prim[p]) {
            for (int viel = p * p; viel < max; viel += p) {
                if (ist_prim[viel]) {
                    std::cout << "Eliminiert " << viel << " (vielfaches von " << p << ")\n";
                    ist_prim[viel] = false;
                }
            }
        }
    }

    std::ofstream file("primzahlen.txt");
    for (int i = 2; i < max; ++i) {
        if (ist_prim[i]) {
            file << i << "\n";
        }
    }


    file.close();
    return 0;
}