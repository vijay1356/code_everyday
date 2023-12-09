#include <stdio.h>
#include <math.h>

#define pi 3.14159265358979323846
#define screen_width 80 // Define your screen width and height
#define screen_height 24

const float theta_spacing = 0.07;
const float phi_spacing = 0.02;

const float R1 = 1;
const float R2 = 2;
const float K2 = 5;

float K1; // Define K1 here

void initializeConstants() {
    K1 = screen_width * K2 * 3 / (8 * (R1 + R2));
}

void render_frame(float A, float B) {
    // Rest of the code remains unchanged...
}

int main() {
    initializeConstants();

    float A = 0, B = 0;

    while (1) {
        render_frame(A, B);
        A += 0.04;
        B += 0.02;
    }

    return 0;
}
