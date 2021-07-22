function checkaccess(){
    var code = document.getElementById("accesscode").value
    if (code === "code")
        return true;
    else{
        alert("Invalid Access Code")
        return false;
    }
}