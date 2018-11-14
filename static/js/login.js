function $1(ID) {
    return document.getElementById(ID)
}

function checkInfo() {
    if ($1("name").value == "" || $1("pwd").value == "") {
        $1("bg").style.display = "block";
        $1("show").style.display = "block";
        return false;
    } else {
        return true;
    }
}

function hideDiv() {
    $1("bg").style.display = "none";
    $1("show").style.display = "none";
}