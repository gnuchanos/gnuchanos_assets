#include <stdio.h>

// python.h
// pointer önemli
// data typecast
// switch case
// statick and dynamic


int main(){

    int number1 = 10; //%d
    float number2 = 20.0f; //%f
    char* name = "Kubilay"; //s pointer*

    char* games[] = {"half life3", "left 4 dead 3", "portal 3"};


    printf("number1:%d | number2:%f \n", number1, number2);
    printf("Name:%s \n", name);
    printf("%s %s %s", games[0], games[1], games[2]); 











    return 0;
}