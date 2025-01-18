<template>
  <div class="main_page">
    <div class="main_page__title">
      Заполнить заявку на строительство
    </div>
    <div class="main_page__subtitle">
      Давайте создадим бриф вашего будущего дома!
    </div>
    <div class="main_page__form">
      <div class="main_page__input_container ic-1">
        <input id="first_name" type="text" class="ic__input">
        <div class="cut"></div>
        <label class="main_page__placeholder" for="first_name">Имя</label>
      </div>
      <div class="main_page__input_container ic-2">
        <input id="surname" type="text" class="ic__input">
        <div class="cut"></div>
        <label class="main_page__placeholder" for="surname">Фамилия</label>
      </div>
      <div class="main_page__input_container ic-2">
        <input id="email" type="email" class="ic__input">
        <div class="cut"></div>
        <label class="main_page__placeholder" for="email">Email</label>
      </div>
      <div class="main_page__input_container ic-2">
        <input id="phone_number" type="text" class="ic__input">
        <div class="cut"></div>
        <label class="main_page__placeholder" for="phone_number">Номер телефона</label>
      </div>
      <div class="main_page__input_container ic-2">
        <textarea id="description" type="text" class="ic__input"></textarea>
        <div class="cut"></div>
        <label class="main_page__placeholder" for="description">Ваши пожелания</label>
      </div>
      <button class="main_page__submit">отправить</button>
    </div>
  </div>
</template>
