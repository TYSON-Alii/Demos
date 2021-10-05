#include <iostream>
#include <Windows.h>

enum Key {
	KEY_A = 65,
	KEY_B = 66,
	KEY_C = 67,
	KEY_D = 68,
	KEY_E = 69,
	KEY_F = 70,
	KEY_G = 71,
	KEY_H = 72,
	KEY_I = 73,
	KEY_J = 74,
	KEY_K = 75,
	KEY_L = 76,
	KEY_M = 77,
	KEY_N = 78,
	KEY_O = 79,
	KEY_P = 80,
	KEY_Q = 81,
	KEY_R = 82,
	KEY_S = 83,
	KEY_T = 84,
	KEY_U = 85,
	KEY_V = 86,
	KEY_W = 87,
	KEY_X = 88,
	KEY_Y = 89,
	KEY_Z = 90,
	KEY_0 = 48,
	KEY_1 = 49,
	KEY_2 = 50,
	KEY_3 = 51,
	KEY_4 = 52,
	KEY_5 = 53,
	KEY_6 = 54,
	KEY_7 = 55,
	KEY_8 = 56,
	KEY_9 = 57,
	KEY_SPACE = 32,
	KEY_ESC = 27,
	KEY_DELETE = 8,
	KEY_TAB = 9,
	KEY_UP = 38,
	KEY_DOWN = 40,
	KEY_RIGHT = 39,
	KEY_LEFT = 37,
	KEY_SHIFT = 16,
	KEY_ENTER = 13,
	MOUSE_LEFT = 1,
	MOUSE_RIGHT = 2,
	MOUSE_MIDDLE = 16
};

bool KeyPressed(Key key_code) {
	return (GetKeyState(key_code) & 0x800);
};

int main() {
	while (true) {
		if (KeyPressed(KEY_ESC))
			break;
		std::cout << "please STOP. (press escape button)\n";
		Sleep(50);
	};
	return 0;
};
