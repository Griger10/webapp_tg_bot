<template>
  <div class="main_page">
    <form action="#" method="post" class="main_page__form">
      <h1 class="main_page__title">Заполнить заявку</h1>
      <div class="main_page__input_container ic">
        <input required id="first_name" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="first_name">Имя</label>
      </div>
      <div class="main_page__input_container ic">
        <input required id="surname" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="surname">Фамилия</label>
      </div>
      <div class="main_page__input_container ic">
        <input required id="email" type="email" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="email">Email</label>
      </div>
      <div class="main_page__input_container ic">
        <input required id="phone_number" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="phone_number">Номер телефона</label>
      </div>
      <button class="main_page__submit" @click="sendForm()">Отправить</button>
    </form>
  </div>
</template>
<script setup>
function sendForm() {
  let name = document.getElementById('first_name').value;
  let surname = document.getElementById('surname').value;
  let email = document.getElementById('email').value;
  let phone_number = document.getElementById('phone_number').value;
  if (name === '' || surname === '' || email === '' || phone_number === '') {
    alert('Заполните все поля!');
  }
  let data = {'first_name': name, 'last_name': surname, 'email': email, 'phone_number': phone_number};

  fetch('http://127.0.0.1:8000/v1/forms/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.log(error));

  name.textContent = '';
  surname.textContent = '';
  email.textContent = '';
  phone_number.textContent = '';
}
</script>