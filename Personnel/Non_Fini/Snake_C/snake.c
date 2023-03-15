#define SDL_MAIN_HANDLED
#include <SDL2/sdl.h>

int isbig(int given){
    char res;
    if (given >=10){
        return 1;
    }else if (given <10){
        return 0;
}
}

int main(int argv, char** args[]){
    SDL_Init(SDL_INIT_VIDEO);
    return 0;
}

