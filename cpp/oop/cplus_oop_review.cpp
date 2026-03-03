#include <iostream>
#include <string>
#include <utility>

using namespace std;

class House 
{
private:
    string name;
    string color;
    int rooms;
    pair<int, int> size;   // (width, length)
    bool door_open;
    bool lights_on;

public:
    // Constructor
    House(string name, string color, int rooms, pair<int, int> size) 
    {
        this->name = name;
        this->color = color;
        this->rooms = rooms;
        this->size = size;
        this->door_open = false;
        this->lights_on = false;
    }

    void open_door() 
    {
        door_open = true;
        cout << name << ": The door is now open." << endl;
    }

    void close_door() 
    {
        door_open = false;
        cout << name << ": The door is now closed." << endl;
    }

    void turn_on_lights() 
    {
        lights_on = true;
        cout << name << ": The lights are now on." << endl;
    }

    void turn_off_lights() {
        lights_on = false;
        cout << name << ": The lights are now off." << endl;
    }

    void show_info() {
        cout << "House Name : " << name << endl;
        cout << "Color      : " << color << endl;
        cout << "Rooms      : " << rooms << endl;
        cout << "Size       : (" << size.first << ", " << size.second << ") m^2" << endl;
        cout << "Door Open  : " << (door_open ? "true" : "false") << endl;
        cout << "Lights On  : " << (lights_on ? "true" : "false") << endl;
    }
};

int main() {
    // Create objects (instances)
    House house1("House1", "Blue", 4, {30, 40});

    House house2("House2", "Red", 5, {20, 30});
    
    House house3("House3", "White", 3, {50, 60});

    // Use methods
    house1.show_info();
    cout << endl;

    house1.open_door();
    house1.turn_on_lights();
    cout << endl;

    house1.show_info();
    cout << endl;

    house2.show_info();

    return 0;
}



// g++ cplus_oop_review.cpp -o cplus_oop_review