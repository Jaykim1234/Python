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
    snake.push_back(make_pair())
}