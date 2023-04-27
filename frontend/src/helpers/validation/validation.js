function requiredField() {
  return "v !== !!v || Поле обязательное";
}

function minChar() {
  return "v.length > 4 || Минимальная длина 5 символов";
}

export { requiredField, minChar };
