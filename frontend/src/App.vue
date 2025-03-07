<template>
  <div class="main_page">
    <form @submit.prevent="sendForm()" class="main_page__form">
      <h1 class="main_page__title">Заполнить заявку</h1>
      <div class="main_page__input_container ic">
        <input v-model="first_name" required id="first_name" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="first_name">Имя</label>
      </div>
      <div class="main_page__input_container ic">
        <input v-model="last_name" required id="last_name" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="last_name">Фамилия</label>
      </div>
      <div class="main_page__input_container ic">
        <input v-model="email" required id="email" type="email" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="email">Email</label>
      </div>
      <div class="main_page__input_container ic">
        <input v-model="phone_number" required id="phone_number" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="phone_number">Номер телефона</label>
      </div>
      <button class="main_page__submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Отправка...' : 'Отправить' }}
      </button>
    </form>
  </div>
</template>
<script setup>
import {ref} from 'vue'

const first_name = ref('');
const last_name = ref('');
const email = ref('');
const phone_number = ref('');
const isSubmitting = ref(false);

async function sendForm() {
  try {
    if (
        !first_name.value ||
        !last_name.value ||
        !email.value ||
        !phone_number.value
    ) {
      alert('Заполните все поля!');
      return;
    }

    isSubmitting.value = true;

    const data = {
      first_name: first_name.value,
      last_name: last_name.value,
      email: email.value,
      phone_number: phone_number.value
    };

    // Отправка запроса
    await fetch('http://127.0.0.1/api/forms/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data),
    });

    first_name.value = '';
    last_name.value = '';
    email.value = '';
    phone_number.value = '';

    window.location.replace("http://127.0.0.1/");

  } catch (error) {
    console.error('Ошибка отправки:', error);
    alert('Произошла ошибка при отправке формы!');
  } finally {
    isSubmitting.value = false;
  }
}
</script>