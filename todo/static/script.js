function clearText() {
    if (document.querySelector('input[name="todo"]').value.length < 2) {
        document.getElementById("error").innerHTML = "Please add task..."
    } else {
        document.getElementById("error").innerHTML = ""
    }
}

document.querySelector("#sub-btn").addEventListener("click", (e) => {
    e.preventDefault();
    console.log(document.querySelector('input[name="todo"]').value.length)
    if (document.querySelector('input[name="todo"]').value.length < 2) {
        document.getElementById("error").innerHTML = "Please add task..."
    } else {
        document.getElementById("error").innerHTML = ""
        document.querySelector('#todo-form').submit()
    }
})