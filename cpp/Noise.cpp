#include <iostream>
#include <Windows.h>
using namespace std;

auto main() -> int {
    cout.sync_with_stdio(false);
    static const auto& hand = GetStdHandle(STD_OUTPUT_HANDLE);
    for (unsigned short i = 0; i < 64*64; i++) {
            SetConsoleTextAttribute(hand, rand() % 256);
            cout << 'A';
    };
};
