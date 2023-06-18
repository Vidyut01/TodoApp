function validateInputs() {
    let valid = true
    
    let name = document.getElementById("username").value
    
    let username_err = document.getElementById("username-err")
    if (name.length < 3) {
        username_err.innerHTML = "Username must be atleast 3 characters long"
        username_err.style.display = "block"
        valid = false
    }
    else if (name.includes(" ")){
        username_err.innerHTML = "Username can't contain spaces"
        username_err.style.display = "block"
        valid = false
    }
    else {
        username_err.style.display = "none"
    }

    let password = document.getElementById("password").value
    let password_re = document.getElementById("password_re").value

    let password_re_err = document.getElementById("password_re-err")
    if (password !== password_re) {
        password_re_err.innerHTML = "Passwords do not match"
        password_re_err.style.display = "block"
        valid = false
    }
    else {
        password_re_err.style.display = "none"
    }

    let upper = false
    let num = false
    for (let i in password) {        
        if (!isNaN(password[i])) {
            num = true

        }
        else if (password[i] === password[i].toUpperCase()) {
            upper = true

        }

    }

    let password_err = document.getElementById("password-err")
    if (!(upper && num) || password.length < 8) {
        password_err.style.color = "red"
        valid = false

    }
    else {
        password_err.style.color = "#000000"
    }


    return valid
}
