function setBody() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("bg").style.backgroundColor = "#282c34"
    }
    else {
        document.getElementById("bg").style.backgroundColor = "#ffffff"
    }

}

function setHeading() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("heading").style.color = "#ffffff"
    }
    else {
        document.getElementById("heading").style.color = "#000000"
    }

}

function setTaskBody() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("task-body").style.color = "#ffffff"
    }
    else {
        document.getElementById("task-body").style.color = "#000000"
    }
}

function setForm() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("form-bg").style.backgroundColor = "#5f5e5e"
        document.getElementById("form-bg").style.color = "#ffffff"
    }
    else {
        document.getElementById("form-bg").style.backgroundColor = "rgb(216, 226, 226)"
        document.getElementById("form-bg").style.color = "#000000"
    }
}

function setIcon() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("theme-icon").src = "/static/todo/icons/moon-fill.svg"
    }
    else {
        document.getElementById("theme-icon").src = "/static/todo/icons/sun-fill.svg"
    }
}

function setNoTask() {
    if (localStorage.getItem('theme') === 'dark') {
        document.getElementById("notask").style.color = "#ffffff"
    }
    else {
        document.getElementById("notask").style.color = "#000000"
    }
}

function toggleTheme(page="") {
    if (localStorage.getItem('theme') === 'dark') {
        localStorage.setItem('theme', 'light')
    }
    else {
        localStorage.setItem('theme', 'dark')
    }

    document.getElementById("bg").style.transition = "all 0.5s"
    
    setBody()
    setIcon()

    if (page === "index") {
        document.getElementById("heading").style.transition = "all 0.5s"
        setHeading()
    }
    else if (page === "task") {
        document.getElementById("task-body").style.transition = "all 0.5s"
        document.getElementById("form-bg").style.transition = "all 0.5s"
        setTaskBody()
        setForm()
    }
    else if (page === "form") {
        document.getElementById("form-bg").style.transition = "all 0.5s"
        setForm()
    }
    
    try {
        document.getElementById("notask").style.transition = "all 0.5s"
        setNoTask()
    }
    catch (e) {}
    
    
    

}
