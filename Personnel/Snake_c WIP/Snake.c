#include <SDL2/SDL.h>
#include <stdio.h>

//? Build command
//? gcc snake.c -ISDL2\include -LSDL2\lib -Wall -lmingw32 -lSDL2main -lSDL2 -o main

void insertdecal(int* arr, int ele, int size){
    for (int i = ele; i <= size-1; i++){
        arr[i] = arr[i+1];
    }
}

int update(int* snake, int* snakelen, int dirx, int diry){
    SDL_Event event;
    while(SDL_PollEvent(&event) != 0){
        if (event.type == SDL_QUIT){
            return -1;
        }
        if (event.type == SDL_KEYDOWN){
            switch (event.key.keysym.sym)
            {
            case SDLK_z:
                insertdecal(snake, 0, 2);
                break;
            case SDLK_ESCAPE:
                return -1;
            default:
                return 0;
            }
        }
    }
    return 0;
}

int main(int argc, char* argv[]){

    SDL_Init(SDL_INIT_EVERYTHING);
    SDL_Window *window =  SDL_CreateWindow("Snake", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 800, SDL_WINDOW_SHOWN);
    int snakelen, dirx, diry;
    dirx = 0;
    diry = 0;
    snakelen = 2;
    int snake[1024];
    snake[0] = 1;
    snake[1] = 2;
    while (1 == 1){
        if (update(snake, &snakelen, dirx, diry) == -1){
            SDL_DestroyWindow(window);
            SDL_Quit();
            return 1;
        }
    }
}
