const inputs = document.querySelectorAll("input");

inputs.forEach((input, index) => {

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            if (index + 1 < inputs.length) {
                inputs[index + 1].focus();
            }

        }

    });

});


function addStudent() {

    let roll = document.getElementById("roll").value;

    let name = document.getElementById("name").value;

    let marks = document.getElementById("marks").value;


    // Validation

    if (roll === "" || name === "" || marks === "") {

        alert("All fields are required!");

        return;
    }


    if (isNaN(roll)) {

        alert("Roll Number must contain only numbers!");

        return;
    }


    if (!isNaN(name)) {

        alert("Name should contain only letters!");

        return;
    }


    if (isNaN(marks)) {

        alert("Marks must contain only numbers!");

        return;
    }


    let student = {
        roll: roll,
        name: name,
        marks: marks
    };


    let students = JSON.parse(localStorage.getItem("students")) || [];

    students.push(student);

    localStorage.setItem("students", JSON.stringify(students));


    addRow(roll, name, marks);


    document.getElementById("roll").value = "";
    document.getElementById("name").value = "";
    document.getElementById("marks").value = "";

    document.getElementById("roll").focus();
}
