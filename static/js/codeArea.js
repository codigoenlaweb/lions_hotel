const phoneNumberPerson = document.querySelector("#id_phone_number_person");
const codeArea = document.querySelector("#codearea");
const phone = document.querySelector("#phone");

phoneNumberPerson.value = codeArea.value + phone.value;

phone.addEventListener("keydown", () => {
  setTimeout(() => {
    phoneNumberPerson.value = codeArea.value + phone.value;
  }, 0);
});

codeArea.addEventListener("keydown", () => {
  setTimeout(() => {
    phoneNumberPerson.value = codeArea.value + phone.value;
  }, 0);
});
