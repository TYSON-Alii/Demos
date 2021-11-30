#include <iostream>
class any {
private:
    void* _data = nullptr;
public:
    void* data() const { return _data; };
    void clear() { _data = nullptr; };
    template <typename T> operator T() const { return *static_cast<T*>(_data); };

    template <typename T> void operator=(const T& v) { _data = new T(v); };
    template <typename T> void operator=(T* v) { _data = new T*(v); };
};

using namespace std;

int main() {
    any v;
    v = "sdadasd";
    cout << (const char*)v;
    v = 45.f;
    cout << (float)v;

    return 0;
};
