#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

unsigned int q2(int R, vector< vector<int> > coords)
{
    // your code is here
    // ----------------------------------------------
    // ----------------------------------------------
}

void compare_output(string, string);

int main()
{
    // DO NOT EDIT main() function

    int R, N, x, y;
    vector< vector<int> > coords;
    clock_t start_time, end_time;

    ifstream input;
    ofstream output;

    input.open("input.txt");          // input data
    output.open("output.txt");        // your answer

    start_time = clock();
    input >> R;
    input >> N;
    for(int i=0; i<N; i++) {
        input >> x;
        input >> y;
        vector<int> coord;
        coord.push_back(x);
        coord.push_back(y);
        coords.push_back(coord);
    }
    int result = q2(R, coords);
    cout << result << endl;
    output << result << endl;
    end_time = clock();

    // Checking answers
    input.close();
    output.close();
    compare_output("output.txt", "expected.txt");
    cout << "Elapsed time: " << (double) (end_time - start_time) / CLOCKS_PER_SEC << " seconds. ";
}

const std::string WHITESPACE = " \n\r\t\f\v";
 
std::string ltrim(const std::string &s)
{
    size_t start = s.find_first_not_of(WHITESPACE);
    return (start == std::string::npos) ? "" : s.substr(start);
}
 
std::string rtrim(const std::string &s)
{
    size_t end = s.find_last_not_of(WHITESPACE);
    return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}
 
std::string trim(const std::string &s) {
    return rtrim(ltrim(s));
}

void compare_output(string file1, string file2)
{
    ifstream f1(file1.c_str());
    ifstream f2(file2.c_str());
    string line1, line2;
    string s1, s2;
    int i = 1;
    int success = 1;

    while(!f1.eof() && !f2.eof()) {
        getline(f1, line1);
        getline(f2, line2);
        s1 = trim(line1);
        s2 = trim(line2);
        if (s1 != s2) {
            cout << "[" << i << "] Wrong answer: Yours=\'" << s1 << "\', Expected=\'" << s2 << "\n" << endl;
            success = 0;
            break;
        }
        i++;
    }
    if (f2.eof() && success) cout << "Success!\n" << endl;
    f1.close();
    f2.close();
}
