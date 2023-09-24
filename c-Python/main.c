#include <stdio.h>







int main() {
    char* name = "kubilay"; // pointer
    int age = 28; float health = 100.0f;

    printf("My Name:%s Age:%d, HealthBar:%f\n", name, age, health);

    int age = 28; float health = 60.0f;
    printf("My Name:%s Age:%d, HealthBar:%f\n", name, age, health);

    return 0;
}
