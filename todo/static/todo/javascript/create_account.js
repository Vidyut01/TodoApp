function validateInputs() {
    var name = document.getElementById("username").value
    
    var username_err = document.getElementById("username-err")
    if (name.length < 3) {
        username_err.innerHTML = "Username must be atleast 3 characters long"
        username_err.style.display = "block"
        return false
    }
    else {
        username_err.style.display = "none"
    }

    var password = document.getElementById("password").value
    var password_re = document.getElementById("password_re").value

    var password_re_err = document.getElementById("password_re-err")
    if (password !== password_re) {
        password_re_err.innerHTML = "Passwords do not match"
        password_re_err.style.display = "block"
        return false
    }
    else {
        password_re_err.style.display = "none"
    }

    var upper = false
    var num = false
    for (var i in password) {        
        if (!isNaN(password[i])) {
            num = true

        }
        else if (password[i] === password[i].toUpperCase()) {
            upper = true

        }

    }

    var password_err = document.getElementById("password-err")
    if (!(upper && num) || password.length < 8) {
        password_err.style.color = "red"
        return false

    }
    else {
        password_err.style.color = "black"
    }


    return true
}
