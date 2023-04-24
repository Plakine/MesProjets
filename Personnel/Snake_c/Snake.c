#include <SDL2/SDL.h>
#include <stdio.h>
// Build command : gcc snake.c -ISDL2\include -LSDL2\lib -Wall -lmingw32 -lSDL2main -lSDL2 -o main
int main(int argc, char* argv[]){
    /*Initial i zes the timen, audio, video, joystick,
    haptic, gamecontrollen and events sutsystems  */
    SDL_Init(SDL_INIT_EVERYTHING);
    printf("d");
    SDL_Quit();
    return 0;
    
}