#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;
class Bank{
	private:
	    int total;
	    string id;
	    struct persoana{
	    	string nume,ID,adresa;
	    	int contact,bani;
		}persoana[100];
	public:
		Bank(){
			total=0;
		}
		void optiune();
		void perData();
		void afiseaza();
		void update();
		void cautare();
		void tranzacti();
		void del();
};
int main(){
	Bank b;
	b.optiune();

	return 0;
}
void Bank::optiune(){

	char ch;
	while(1){
	cout<<"\n\nApasa..!!"<<endl;
	cout<<"1. Creaza un cont nou"<<endl;
	cout<<"2. Vizualizeaza lista clientilor"<<endl;
	cout<<"3. Updateaza continutul contului existent"<<endl;
	cout<<"4. Verifica detaliile contului existent"<<endl;
	cout<<"5. Pentru tranzactii"<<endl;
	cout<<"6. Sterge contul existent"<<endl;
	cout<<"7. Exit"<<endl;
	ch=getch();
	system("CLS");
	switch(ch){
		case '1':
			Bank::perData();
			break;
		case '2':
			if(total==0){
				cout<<"Nu este introdusa nici o data"<<endl;
			}else{
			Bank::afiseaza();
		   }
			break;
		case '3':
			if(total==0)
			cout<<"Nu este introdusa nici o data"<<endl;
			else
			Bank::update();

			break;
		case '4':
			if(total==0)
			cout<<"Nu este introdusa nici o data"<<endl;
			else
			Bank::cautare();
			break;
		case '5':
			if(total==0)
			cout<<"Nu este introdusa nici o data"<<endl;
			else
			Bank::tranzacti();
			break;
		case '6':
			if(total==0)
			cout<<"Nu este introdusa nici o data"<<endl;
			else
			Bank::del();
			break;
		case '7':
			exit(0);
			break;
		default:
			cout<<"Optiune invalida"<<endl;
			break;
	}
    }
}
void Bank::perData(){
	cout<<"Introdu informatii despre persoana "<<total+1<<endl;
	cout<<"Introdu numele: ";
	cin>>persoana[total].nume;
	cout<<"ID: ";
	cin>>persoana[total].ID;
	cout<<"Address: ";
	cin>>persoana[total].adresa;
	cout<<"Contact: ";
	cin>>persoana[total].contact;
	cout<<"Total Cash: ";
	cin>>persoana[total].bani;
	total++;
}
void Bank::afiseaza(){
	for(int i=0;i<total;i++){
		cout<<"Date despre persoana "<<i+1<<endl;
		cout<<"Nume: "<<persoana[i].nume<<endl;
		cout<<"ID: "<<persoana[i].ID<<endl;
		cout<<"Addresa "<<persoana[i].adresa<<endl;
		cout<<"Contact: "<<persoana[i].contact<<endl;
		cout<<"Bani: "<<persoana[i].bani<<endl;
	}
}
void Bank::update(){
	cout<<"Indroduceti Id-ul persoanei pe care doriti sa o updatati"<<endl;
	cin>>id;
	for(int i=0;i<total;i++){
		if(id==persoana[i].ID){
		cout<<"Informatii vechi"<<endl;
		cout<<"Informatii persoana "<<i+1<<endl;
		cout<<"Nume: "<<persoana[i].nume<<endl;
		cout<<"ID: "<<persoana[i].ID<<endl;
		cout<<"Adresa "<<persoana[i].adresa<<endl;
		cout<<"Contact: "<<persoana[i].contact<<endl;
		cout<<"Bani: "<<persoana[i].bani<<endl;
		cout<<"\nIntroduceti date noi"<<endl;
		cout<<"Introduceti numele: ";
	cin>>persoana[i].nume;
	cout<<"ID: ";
	cin>>persoana[i].ID;
	cout<<"Adresa: ";
	cin>>persoana[i].adresa;
	cout<<"Contact: ";
	cin>>persoana[i].contact;
	cout<<"Suma bani: ";
	cin>>persoana[i].bani;
	break;
		}
		if(i==total-1){
			cout<<"Nu exista astfel de informatii"<<endl;
		}
	}
}
void Bank::cautare(){
cout<<"Indroduceti Id-ul persoanei pe care doriti sa o cautati"<<endl;
cin>>id;
for(int i=0;i<total;i++){
	if(id==persoana[i].ID){
		cout<<"Nume: "<<persoana[i].nume<<endl;
		cout<<"ID: "<<persoana[i].ID<<endl;
		cout<<"Adresa: "<<persoana[i].adresa<<endl;
		cout<<"Contact: "<<persoana[i].contact<<endl;
		cout<<"Bani: "<<persoana[i].bani<<endl;
		break;
	}
	if(i==total-1){
		cout<<"Nu exista astfel de informatii"<<endl;
	}
}
}
void Bank::tranzacti(){
	int bani;
	char ch;
	cout<<"Indroduceti Id-ul persoanei pe care doriti a caror informatii doresti sa le tranzactionezi"<<endl;
     cin>>id;
     for(int i=0;i<total;i++){
     	if(id==persoana[i].ID){
     		cout<<"Nume: "<<persoana[i].nume<<endl;
     	     cout<<"Adresa: "<<persoana[i].adresa<<endl;
		     cout<<"Contact: "<<persoana[i].contact<<endl;
		     cout<<"\nBani existenti "<<persoana[i].bani<<endl;
		     cout<<"Press 1 pentu depozitare"<<endl;
		     cout<<"Press 2 pentru retragere"<<endl;
		     ch=getch();
		     switch(ch){
		     	case '1':
		     		cout<<"Cati de multi bani doriti sa depozitati??"<<endl;
		     		cin>>bani;
		     		persoana[i].bani+=bani;
		     		cout<<"Introduceti noua suma de bai "<<persoana[i].bani<<endl;
		     		break;
		     	case '2':
		     		back:
		     		cout<<"Cati de multi bani doriti sa retrageti??"<<endl;
		     		cin>>bani;
		     		if(bani>persoana[i].bani)
                        {
		     			cout<<"Suma de bani actuala este "<<persoana[i].bani<<endl;
		     			Sleep(3000);
		     			goto back;
					 }
					 persoana[i].bani-=bani;
					 cout<<"Suma de bani noua este "<<persoana[i].bani<<endl;
					 break;
				default:
					cout<<"Date invalide"<<endl;
					break;
			 }
			 break;
		 }
		 if(i==total-1){
		 	cout<<"Nu exista astfel de informatii"<<endl;
		 }
	 }
}
void Bank::del(){
	char ch;
	cout<<"Press 1 sa stergi o informatie"<<endl;
	cout<<"Press 2 sa stergi toate informatiile"<<endl;
	ch=getch();
	switch(ch){
		case '1':
	cout<<"Indroduceti Id-ul persoanei pe care doriti sa o stergeti"<<endl;
     cin>>id;
     for(int i=0;i<total;i++){
     	if(id==persoana[i].ID){
     		for(int j=i;j<total;j++){
     		persoana[j].nume=persoana[j+1].nume;
     		persoana[j].ID=persoana[j+1].ID;
     		persoana[j].adresa=persoana[j+1].adresa;
     		persoana[j].contact=persoana[j+1].contact;
     		persoana[j].bani=persoana[j+1].bani;
     		total--;
     		cout<<"Informatia dorita a fost stearsa"<<endl;
     		break;

			 }
		 }
		 if(i=total-1){
		cout<<"Nu exista astfel de informatii"<<endl;
		 }
	 }
	 break;
	 case '2':
	 	total=0;
	 	cout<<"Toate conturile sunt goale"<<endl;
	 	break;
	default:
		cout<<"Date invalide"<<endl;
		break;
	}

}
