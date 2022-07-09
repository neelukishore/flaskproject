function validateUserName(){
    var name = document.forms['registrationform']['username'].value;

    if(name=='' || name.length5 || name.length>20){
        document.getElementById("username").style.border = "2px solid red";
        document.getElementById("errorname").style.color = "red";
        document.getElementById("errorname").innerHTML = "UserName must contain 5 to 20 characters";
        return false;
    }
    else{
        document.getElementById("username").style.border = "2px solid green";
        document.getElementById("errorname").style.color = "green";
        document.getElementById("errorname").innerHTML = "UserName satisfied";
        return true;
    }

}
function validatePassword(){
    var password1 = document.forms['registrationform']['password'].value;
    var patt = new RegExp("[0-9]");
    var result = patt.test(password1);
    if(result=="false" || password1.length<5 || password1.length>20){
        document.getElementById("password").style.border = "2px solid red";
        var errorpassword = "Password must contain 1 digit with 5 to 20 characters";
        document.getElementById("password").value = "";
        document.getElementById("password").placeholder = errorpassword;
        return false;
    }
    else{
        document.getElementById("password").style.border = "2px solid green";
        return true;
    }
}
function validateLoginEmail(){
    var loginemail = document.forms["loginform"]["email1"].value;
    var atposition = loginemail.indexOf("@");
    var dotposition = loginemail.lastIndexOf(".");
    
    if(atposition<1 || dotposition<atposition+2 || dotposition+2>=loginemail.length){
        document.getElementById("email1").style.border = "2px solid red";
        return false;
    }
    else{
        document.getElementById("email1").style.border ="2px solid green";
        return true;
    }
}
function validateloginPassword(){
    var password1 = document.forms['loginform']['password1'].value;
    var patt = new RegExp("[0-9]");
    var result = patt.test(password1);
    if(result=="false" || password1.length<5 || password1.length>20){
        document.getElementById("password1").style.border = "2px solid red";
        
        return false;
    }
    else{
        document.getElementById("password1").style.border = "2px solid green";
        return true;
    }
}

function validateall(){
    if(validateUserName() & validatePassword() ){
        return true;
    }
    else{
        return false;
    }
}

function validatelogin(){
    if(validateLoginEmail() & validateloginPassword()){
        return true;
    }
    else{
        return false;
    }
}