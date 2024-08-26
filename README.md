Aplikacija je namijenjena za poslodavce koji pomoću aplikacije raspisuju natječaje za posao.

Funkcionalnosti su: Dodaj posao, uredi posao te izbriši posao.

Za pokretanje aplikacije je potreban Docker. Nakon što se preuzmu datoteke s github-a,

otvara se projekt u VS Code-u(ili nekom drugom programu, npr. PyCharm). Potrebno je

instalirati flask i pony, u terminalu, pomoću komandi 'pip install flask' i 'pip install pony'.

Nakon toga, u terminalu se upiše "docker build --tag posao:3.1 ." za stvaranje image-a u Dockeru.

Nakon toga "docker run -p 5001:8000 posao:3.1" za pokretanje preko Dockera.

U web pregledniku upisujemo localhost:5001 i možemo koristiti aplikaciju.
