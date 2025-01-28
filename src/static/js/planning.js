document.getElementById("form").addEventListener("submit", function (e) {
    console.log("submit");
    e.preventDefault();
    const nom = document.getElementById("nom").value;
    const debut = document.getElementById("debut").value;
    const fin = document.getElementById("fin").value;

    fetch("/api/planning/new", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nom,
            debut,
            fin
        })
    }).then(() => { // à revoir
        window.location.reload();
    });
});


document.querySelectorAll('[name="btn_modif"]').forEach((btn) => {
    btn.addEventListener("click", function (e) {
            e.preventDefault();
            const id = this.parentElement.getAttribute("data-id");
            console.log(id);
    });
});


document.querySelectorAll('[name="btn_suprim"]').forEach((btn) => {
    btn.addEventListener("click", function (e) {
            e.preventDefault();
            const id = this.parentElement.getAttribute("data-id");
            console.log(id);
            fetch("/api/planning/delete", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    id
                })
            }).then((data) => {
                window.location.reload();
                // console.log(data);
            })
    });
});