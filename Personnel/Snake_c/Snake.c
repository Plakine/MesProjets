#include <SDL2/SDL.h>
#include <stdio.h>

// Build command : gcc snake.c -ISDL2\include -LSDL2\lib -Wall -lmingw32 -lSDL2main -lSDL2 -o main

int update(){
    SDL_Event event;
    while(SDL_PollEvent(&event) != 0){
        if (event.type == SDL_QUIT){
            return -1;
        }
        if (event.type == SDL_KEYDOWN){
            switch (event.key.keysym.sym)
            {
            case SDLK_z:
                return 1;
            default:
                return 0;
            }
        }
    }
    return 0;
}



int main(int argc, char* argv[]){
    /*Initial i zes the timen, audio, video, joystick,
    haptic, gamecontrollen and events sutsystems  */
    SDL_Init(SDL_INIT_EVERYTHING);
    SDL_Window *window =  SDL_CreateWindow("Snake", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 800, SDL_WINDOW_SHOWN);
    // TODO : Create window
    while (1 == 1){
        if (update() == -1){
            break;
        }
    }
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 1;
}
