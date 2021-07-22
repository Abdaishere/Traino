function check(){
    let alertstring = []
    var letters = /^[A-Za-z]+$/;
    
    let Username = document.getElementsByName('first_name')[0].value;
    if(Username == ''){
        alertstring.push("• First Name field must be filled out")
    }
    Username = document.getElementsByName('last_name')[0].value;
    if(Username == ''){
        alertstring.push("• Last Name field must be filled out")
    }
    

    Username = document.getElementsByName('username')[0].value;
    if(Username == ''){
        alertstring.push("• Username field must be filled out")
    }
    if (!Username[0].match(letters)){
        alertstring.push("• Username field must start with a letter")
    }
    
    let email = document.getElementsByName('email')[0].value
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email == ''){
        alertstring.push("• email address must be filled out")
    }
    else if (!email.match(mailformat)){
        alertstring.push("• invalid email address")
    }
    
    let password = document.getElementsByName('password1')[0].value
    if (password == ''){
        alertstring.push("• Password must be filled out")
    }
    else if (password.length <= 7){
        alertstring.push("• Password too short (must be 8 letters or more)")
    }
    let passwordagain = document.getElementsByName('password2')[0].value
    if (passwordagain == '' && password != ''){
        alertstring.push("• Password not confirmed")
    }
    else if (passwordagain !== password){
        alertstring.push("• Password not identical")
    }


    if (alertstring.length != 0 ){
        alert(alertstring.join('\n'));
        return false;
    }
    return true;
}

