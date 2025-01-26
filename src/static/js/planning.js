document.getElementById("form").addEventListener("submit", function (e) {
    console.log("submit");
    e.preventDefault();
    const nom = document.getElementById("nom").value;
    const duree = document.getElementById("duree").value;
    fetch("/api/planning", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nom,
            duree
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
    });
});