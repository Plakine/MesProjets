/*  Projet: Site Web
    Auteur: J.Antognelli
    Type:Scolaire
    Description : 
        Fichier javascript contenant les fonctions 
        pour le site de conversion de nombre
        * Traduction de Fonctions.py
*/ 

//Changes color scheme (Fait main)
function change_theme(){
    let root = document.documentElement;
    let night_button = document.getElementsByClassName("Night_Day")
    console.log(night_button)
    //To Night
    if (root.style.getPropertyValue("--current-theme") == "day"){
    root.style.setProperty("--main-theme","rgba(0, 0, 0, 0.84)");
    root.style.setProperty("--secondary-theme",'rgba(0,0,0,0.95)');
    root.style.setProperty("--current-theme",'night');
    root.style.setProperty("--font-color",'rgb(255,255,255)')
    night_button[0].src="resources/Light_mode_v3.png"
    }

    //To day
    else{
        root.style.setProperty("--main-theme","rgb(180, 177, 177)"); //Un peu moins gris
        root.style.setProperty("--secondary-theme",'rgb(138, 137, 137)'); //Gris
        root.style.setProperty("--current-theme",'day'); 
        root.style.setProperty("--font-color",'rgb(0,0,0)') //Noir
        night_button[0].src = "resources/Night_mode_v3.png";}}

function BeAnnoying(){
    var annoyingList = ["-50% sur les autocorrections de contrôles!","je lache NSI", "Comment se passe le divorce","l'abus d'alcool est dangereux pour le marriage", "Arthur, ou Perceval c'est mieux que Merlin",    "je suis à court d'idées", "Le saviez-vous : le logo est en Comic Sans MS","C'est pas très clair \"Quelques autres pages\" non?","Derrière vous","Je vous interdit de bloquer les alertes","C'est pas si mal le comic sans MS"]
    if( Math.random() > 0.75){
        change_theme()
    }
    alert(annoyingList[Math.floor(Math.random()*(annoyingList.length-1))])
    setTimeout(BeAnnoying,90_000)
}


{//TODO Integrer les trucs la
function dectobin(num1){
    res = '';
    n = num1;
    while (n!=0) {
        res = (n%2).toString()+res
        n = Math.floor(n/2)
    }
    return res
}
function bintodec(bin1){
    res = 0 ;
    v = 0;
    for  (let i = bin1.length-1; i >=0; i--){
        res = res + parseInt(bin1[i])*(2**v);
        v++;
    }
    return (res)
}
function hexaversdeci(hex1){
    hexa = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,"6":6, "7":7,"8":8,"9":9,"A":10, "B":11,"C":12,"D":13,"E":14,"F":15}
    res = 0;
    hex1 = hex1.toUpperCase();
    v = 0;
    for (let i = hex1.length-1; i >= 0;i--){
        res = res + ((hexa[hex1[i]])*(16**v));
        v ++;
    }
    return res;
}
function decivershexa(dec1){
    hexa = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8",9:"9",10:"A", 11:"B",12:"C",13:"D",14:"E",15:"F"}
    res = "";
    while (dec1!=0){
        res = (hexa[dec1%16]).toString() + res;
        dec1 = Math.floor(dec1/16);
    }
    return res;
}
function hextobin(hexa1){
    dictbin = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",
    }  
    res = "";
    hexa1 = hexa1.toUpperCase();
    for (let i = 0;i<hexa1.length;i++){
        res = res + dictbin[hexa1[i]] ;
    }
    return res;
}
function bintohex(n){
    while ((n).length%4 != 0){
        n = "0" +n;
    }
    dictbin = {
        "0000":"0",
        "0001":"1",
        "0010":"2",
        "0011":"3",
        "0100":"4",
        "0101":"5",
        "0110":"6",
        "0111":"7",
        "1000":"8",
        "1001":"9",
        "1010":"A",
        "1011":"B",
        "1100":"C",
        "1101":"D",
        "1110":"E",
        "1111":"F",
    } 
    res = "";
    for (let i=0;i <Math.floor(n.length/4);i++){
        res += dictbin[n.slice(i*4,(i+1)*4)];
    }
    return res;
}

function B1B2(num1,b1,b2){
    dicto={
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":18,
        "J":19,
        "K":20,
        "L":21,
        "M":22,
        "N":23,
        "O":24,
        "P":25,
        "Q":26,
        "R":27,
        "S":28,
        "T":29,
        "U":30,
        "V":31,
    }
    n = 0;
    v = 0;
    num1 = num1.toString().toUpperCase()
    for (let i = num1.length-1; i >= 0;i--){
        n+= dicto[num1[i]]*b1**v;
        v++;
    }
    res = "";
    while (n!=0){
        res = Object.keys(dicto).find(key => dicto[key] == (n%b2).toString())+res;
        n = Math.floor(n/b2);
    }
    return res;
}

function addany(num1,num2){
    if ((num1).length > (num2).length){
        while ((num2).length != (num1).length){
            num2 = "0" + num2;
        }
    }
    else if ((num2).length > (num1).length){
        while ((num1).length != (num2).length){
            num1 = "0" + num1
        }
    }
    else if ((num1).length == (num2).length){
        //pass
    }
    retenue = 0;
    res = "";
    for (let i = num1.length-1; i >=0;i--){
        Value = parseInt(num1[i])+parseInt(num2[i])+retenue 
        if (Value == 1 || Value == 3){
            res = '1' + res;
        }
        else{
            res = "0"+res;
        }
        if ((Value) > 1){
            retenue = 1;
        }
        else{
            retenue = 0;
        }
    }
    if (retenue == 1){
        res = "1"+res;
    }
    return res;
}

function addfix(num1, num2, lenmax){
    while (num1.length < lenmax){
        num1 = "0"+num1
    }
    while (num2.length < lenmax){
        num2 = "0" + num2
    }
    retenue = 0;
    res = "";
    for (let i = lenmax-1; i >=0;i--){
        Value = parseInt(num1[i])+parseInt(num2[i])+retenue 
        if (Value == 1 || Value == 3){
            res = '1' + res;
        }
        else{
            res = "0"+res;
        }
        if ((Value) > 1){
            retenue = 1;
        }
        else{
            retenue = 0;
        }
    }
    return res;

}

function subany(num1,num2){
    while ((num1).length != (num2).length){
        if ((num1).length > (num2).length){
            num2 = "0" + num2;
        }
        else{
            num1 = "0" + num1;
        }
    }
    res = ""; 
    retenue = 0; 
    for (let i = num1.length-1; i >= 0;i--){
        if (parseInt(num1[i])-(parseInt(num2[i]+retenue)) in [1,-1,-3]){
            res = "1" + res;
        }
        else if (parseInt(num1[i])-(parseInt(num2[i])+retenue) in [0,-2]){
            res = "0" +res;
        }
        if (parseInt(num1[i])-(parseInt(num2[i])+retenue) < 0){
            retenue = 1 ; 
        }
        else{
            retenue = 0;
        }
    }
return res;
}

function multipleany(num1,num2){
    presumlist = [];
    resact = "";
    for (let i = 0; i<num1.length;i++){
        for (let j = num2.length-1; j >= 0; j--){
            if (parseInt(num1[i])-(parseInt(num2[j])) < 0){
                resact = "1"+resact;
            }
            else{
                resact="0"+resact;
            }
        }
        presumlist.push(resact)
        resact = "0"*(i+1);
    }
    while ((presumlist.length) != 1 ){
        presumlist.push(addany(presumlist[0],presumlist[1]));
        presumlist.shift();
        presumlist.shift();
    }
    res = presumlist[0];
    return res; 
}

function deccomp2(num1){
    if (num1 > 0){
        return "0"+dectobin(Math.abs(num1))
    }
    num1 = Math.abs(num1)
    n = dectobin(num1)

    res = ''
    for (i in n){
        if (n[i] == "0"){
            res += "1"
        }
        else{
            res += "0"
        }
    }
    console.log(res)
    while (1){
        if(addfix(n,res,n.length).indexOf("1") != -1){
            res = addfix(res,"1",res.length)
            console.log(n,res)
        }else{
        console.log(res)
        return "1" + res;}
}}

}