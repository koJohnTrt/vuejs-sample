import { createApp, h } from 'vue';
import axios from 'axios';

import './dist/css/bootstrap.css';

import App from './App.vue';
import router from './router';

axios.defaults.baseURL = 'http://localhost:5000/'; // the FastAPI backend

const app = createApp({
    router,
    render: () => h(App),
}).use(router);
app.mount('#app');
