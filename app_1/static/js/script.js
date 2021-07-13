const form_eliminar = document.getElementById("form_eliminar");
const inputs = document.querySelectorAll("#form input");
const select = document.getElementById("id_provincia");
const regex = {
  letras: /^[a-zA-Z]+$/,
};

function error(id) {
  const div = document.getElementById("id_" + id);

  if (div.classList.contains("is-valid")) {
    div.classList.replace("is-valid", "is-invalid");
  } else {
    div.classList.add("is-invalid");
  }
}
function success(id) {
  const div = document.getElementById("id_" + id);

  if (div.classList.contains("is-invalid")) {
    div.classList.replace("is-invalid", "is-valid");
  } else {
    div.classList.add("is-valid");
  }
}

// validacion del form //
const validarForm = (e) => {
  switch (e.target.name) {
    case "nombre":
      const name = inputs[1];
      if (!regex.letras.test(name.value)) {
        error("nombre");
      } else {
        success("nombre");
      }
      break;

    case "apellido":
      const apellido = inputs[2];
      if (!regex.letras.test(apellido.value)) {
        error("apellido");
      } else {
        success("apellido");
      }
      break;

    case "edad":
      const input = inputs[3];
      const edad = Number(input.value);
      if (edad < 0 || edad > 100 || edad === 0) {
        error("edad");
      } else {
        success("edad");
      }
      break;

    case "dni":
      const dni = inputs[4];
      if (dni.value.length !== 8) {
        error("dni");
      } else {
        success("dni");
      }
      break;
  }

  if (select !== null) {
    select.addEventListener("change", () => {
      select.classList.add("is-valid");
    });
  }
};

// eventListener
inputs.forEach((input) => {
  input.addEventListener("keyup", validarForm);
  input.addEventListener("blur", validarForm);
});

if (form_eliminar !== null) {
  form_eliminar.addEventListener("submit", (e) => {
    e.preventDefault();
    Swal.fire({
      title: "Esta seguro?",
      text: "Este cambio no podra revertirse",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, eliminar",
      cancelButtonText: "No eliminar",
    }).then((result) => {
      if (result.isConfirmed) {
        form_eliminar.submit();
      }
    });
  });
}
