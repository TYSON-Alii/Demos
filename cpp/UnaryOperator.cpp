#include <iostream>
using namespace std;

template <typename T>
struct sqr_op {
	T a;
	sqr_op(const T& v) : a(v) {
		a = v;
	}
	operator T() {
		return a * a;
	}
};
template <typename T>
struct sqrtf_op {
	T a;
	sqrtf_op(const T& v) : a(v) {
		a = v;
	}
	operator T() {
		return std::sqrtf(a);
	}
};
#define sqr (float)(sqr_op<float>)
// #define sqrtf (float)(sqrtf_op<float>)

struct del_op {
	del_op(auto v) {
		cout << "i'm gonna delete this shit\n";
	}
};
#define del (del_op)

struct print_op {
	print_op(auto v) {
		cout << v << '\n';
	}
};
#define print (print_op)


auto main() -> int {
	print "merhaba";
	print sqr sqr 3.14;

	return 0;
}
