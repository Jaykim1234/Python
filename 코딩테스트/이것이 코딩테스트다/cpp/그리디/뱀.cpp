#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#define APPLE 1
#define SNAKE 2
using namespace std;

int dy[] = {0, 1, 0 , -1};
int dx[] = {1, 0, -1, 0};

vector<vector<int>> map;

queue<pair<int, char>> snakeDir;

int n;

int getDir(int dir, char roDir) {
    if (roDir == 'L') dir = (dir -1 < 0 ? 3: dir -1);
    else dir = (dir +1>3 ? 0: dir +1);
    return dir;
}

int move() {
    deque<pair<int, int>> snake;
    snake.push_back(make_pair(1, 1));

    int y, x;
    int time = 0 ;
    int dir = 0 ;
    int roCnt = snakeDir.front().first;
    char roDir = snakeDir.front().second;
    snakeDir.pop();
    y = x =1;
    map[y][x] = SNAKE;

    while (1) {
        y = y + dy[dir];
        x = x + dy[dir];
        time += 1;

        if (y==0 || y == (n+1) || x==0 || x==(n+1)) return time;

        if (map[y][x] == SNAKE) return time;

        if (map[y][x] == APPLE) {
            map[y][x] = SNAKE;
            snake.push_front(make_pair(y, x));

        }

        else{
            map[y][x] = SNAKE;
            snake.push_front(make_pair(y,x));
            map[snake.back().first][snake.back().second] = 0;
            snake.pop_back();
        }
        if (time==roCnt){
            dir = getDir(dir, roDir);
            if(!snakeDir.empty()){
                roCnt = snakeDir.front().first;
                roDir = snakeDir.front().second;
                snakeDir.pop();

            }
        }

    }
}
#https://smartshk.tistory.com/30