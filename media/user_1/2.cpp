#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

int gradestring(string grad);

int main()
{
  map<string,string> stud;
  map<string,pair<string,int>> semester[9];
  map<string,vector<pair<string,string>>> grades;

  fstream fin,fout;
  fin.open("students.csv",ios::in);
  string w1,w2,line;
	while(!fin.eof())
  {
    getline(fin,line);
	  stringstream s(line);
    if(line.size()==0)
    {
      break;
    }
  	getline(s,w2,',');
  	getline(s,w1,',');
    stud[w1]=w2;
   }
   fin.close();

    fin.open("courses.csv",ios::in);
    string w[7];

    while(!fin.eof())
    {
      getline(fin,line);
    	stringstream s(line);
    	if(line.size()==0)
      {
        break;
      }
    	for(int i=0;i<7;i++)
      {
        getline(s,w[i],',');
    	}
      semester[stoi(w[0])][w[1]]=mp(w[2],stoi(w[6]));
    }
  fin.close();

  fin.open("grades.csv",ios::in);
  string w3;
  while(!fin.eof())
  {
  	getline(fin,line);

  	stringstream s(line);
  	if(line.size()==0)
    {
      break;
    }
  	getline(s,w1,',');
  	getline(s,w2,',');
    w2 = w2.substr(0,w2.size()-1);
  	getline(s,w3,',');
  	grades[w1].pb(mp(w2,w3));
  }
  fin.close();

  for(auto t:grades)
  {
  	string str=t.first;
  	str=str+".txt";
  	fout.open(str,ios::out);
    fout << "Name : " << stud[t.first] << endl;
	  fout << "Roll Number : " << t.first <<endl;

    int tot_cred=0;
    int totcredachieved=0;

  	for(int i=1;i<9;i++)
    {
  		fout<<"Semester "<<i<<endl;
      fout<<"Course Number"<<"\t|\t"<<"C"<<"\t | \t"<<"Grade" << endl;
  		int sem_cred=0;
  		int achieved_cred_sem=0;
    	for(auto c:t.second)
      {
    		if(semester[i].find(c.first)!=semester[i].end())
        {
    			fout << c.first << "\t\t\t" << semester[i][c.first].second << "\t\t" << c.second << endl;
    			sem_cred = sem_cred + semester[i][c.first].second;
    			achieved_cred_sem = achieved_cred_sem + semester[i][c.first].second*gradestring(c.second);
    		}
    	}
      // SPI calculation
      float spi = (float)achieved_cred_sem/(float)sem_cred;
    	fout << "SPI: " << spi << endl;


      // CPI calculation

    	tot_cred = tot_cred + sem_cred;
    	totcredachieved = totcredachieved + achieved_cred_sem;
      float cpi=(float)totcredachieved/(float)tot_cred;
    	fout<<"CPI: "<<cpi<<endl;
    }
        fout.close();
      }
        return 0;
  }


int gradestring(string grad)
{
  if(grad=="AS")
		return 10;
  else if(grad=="AA")
    return 10 ;
	else if(grad=="AB")
    return 9;
	else if(grad=="BB")
    return 8;
	else if(grad=="BC")
    return 7;
	else if(grad=="CC")
    return 6;
	else if(grad=="CD")
    return 5;
	else if(grad=="DD")
    return 4;
  else
    return 0;
}
