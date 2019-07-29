// problem 3

#include<iostream>
#include <stdio.h> 
#include <math.h>

#define PI 3.14159265

using namespace std;

int main(){
	float param, cosine, sine;
	int a[1][2],r1,c1,r2,c2, i, j, k;
	r1=1;c1=2;r2=2;c2=2;
	
	param = 30.0;
	cosine = cos ( param * PI / 180.0 );
	sine = sin ( param * PI / 180.0 );

	float rotm[2][2] = {{cosine, -sine}, {sine, cosine}};
	float mult[2][2] = {{0,0},{0,0}};
	
	a[0][0] = 2;
    a[0][1] = 3;
    
    for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
            for(k = 0; k < c1; ++k)
            {
                mult[i][j] += a[i][k] * rotm[k][j];
            } 

    // Displaying the multiplication of two matrix.
    cout << endl << "multiplication: " << endl;
    for(i = 0; i < r1; ++i)
    for(j = 0; j < c2; ++j)
    {
        cout << " " << mult[i][j];
        if(j == c2-1)
            cout << endl;
    }
    return 0;            
}

// /////////////////////////////////////////////
////////////////////////////////////////////////

// problem 4

#include<iostream>
#include<cmath>
#include <bits/stdc++.h> 

using namespace std;

int main(){
	int r1,c1,r2,c2, i, j, k;
	r1=3;c1=3;r2=3;c2=3;
	
	float m[3][3] = {{1.760,8.040, -1.510}, {8.040, -1.820, 0.475}, {-1.510, 0.475, 0.058}};
	float mult[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
	
	for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
            for(k = 0; k < c1; ++k)
            {
                mult[i][j] += m[i][k] * m[k][j];
            } 

    float sum = 0;
    for (i = 0; i<r1; i++)
    	for(j=0; j<c2; j++)
    		sum += mult[i][j];

    float s = sqrt(sum);
    float M0 = (1/sqrt(2))*(s);

    float Mw = (2.0/3.0)*(log10(M0)- 16.1);

    cout<<"M0: "<<M0<<endl;
    cout<<"Mw: "<<Mw<<endl;

    return 0;            
}

















