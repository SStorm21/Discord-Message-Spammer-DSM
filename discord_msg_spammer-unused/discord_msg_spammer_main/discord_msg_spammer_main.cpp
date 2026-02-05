#include <iostream>
#include <string>
using namespace std;

int main()
{

    int x = 0;
    while (1 == 1){

        cout << " " << string(48, '-') << endl;
        cout<< "        DISCORD MESSAGE SPAMMER [v0.5-min]    " << endl;

        cout << " " << string(48, '-') << endl;

        cout<< "\n   CHANNELS & CONFIGURATION" << endl;
        cout<< "   " << string(24, '-') << endl;
        cout<< "   ( 1 )  Import Tokens List" << endl;
        cout<< "   ( 2 )  Set Channel IDs" << endl;
        cout<< "   ( 3 )  Start Spammer" << endl;

        cin>>x;

        switch(x) 
        {
        case 1:
            cout<< "this is option num 1 ill run python script number 1";
            break;
        case 2:
            break;

        }
    }

    return  0;
}


