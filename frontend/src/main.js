import './assets/style.css'

import {createApp} from 'vue'
import App from './App.vue'

export default {
    data() {
        return {
            forms: []
        }
    },
    methods:
        {
            getForms() {
                return fetch('http://localhost:8000/forms')
                    .then(response => response.json())
                    .then(data => {
                        this.forms = data
                    })
            }
        },

}
const methods = {
    getForms() {
        return fetch('http://localhost:8000/forms')
            .then(response => response.json())
            .then(data => {
                this.forms
            })
    }
}

createApp(App).mount('#app')
