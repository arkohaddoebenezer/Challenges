#include <iostream>
#include <cmath>

using namespace std;

class Main {
public:
    int getCentury(int year) {
        return int (ceil(double(year) / 100.0));
    }
};

int main() {
    Main myObject;
    int year = 2024;
    int century = myObject.getCentury(year);

    std::cout << "Year: " << year << " is in the " << century << "th century." << std::endl;

    return 0;
}
