import { render } from "../node_modules/lit-html/lit-html.js";
import page from "../node_modules/page/page.mjs";

import { logout as apiLogout } from "./api/data.js";
import { homePage } from "../src/views/home.js";
import { loginPage } from "../src/views/login.js";
import { registerPage } from "./views/register.js";
import { catalogPage } from "./views/catalog.js";
import { createPage } from "./views/create.js";
import { detailsPage } from "./views/details.js";
import { editPage } from "./views/edit.js";

const main = document.getElementById('main-content')
document.getElementById('logoutBtn').addEventListener('click', logout);
setUserNav();

page('/', decorateContext, guestUsersOnly, homePage);
page('/login', decorateContext, loginPage);
page('/register', decorateContext, registerPage);
page('/catalog', decorateContext, catalogPage);
page('/create', decorateContext, createPage);
page('/details/:id',decorateContext, detailsPage);
page('/edit/:id',decorateContext, editPage);



page.start();



function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, main);
    ctx.setUserNav = setUserNav;

    next();
}


function setUserNav() {
    const token = sessionStorage.getItem('authToken');
    if (token != null) {
        document.getElementById('user').style.display = '';
        document.getElementById('guest').style.display = 'none';
    } else {
        document.getElementById('guest').style.display = '';
        document.getElementById('user').style.display = 'none';
    }
}

function guestUsersOnly(ctx, next) {
    const token = sessionStorage.getItem('authToken');
    if (token != null) {
        return ctx.page.redirect('/catalog');
    }
    next();
}


async function logout() {
    await apiLogout();
    setUserNav();
    page.redirect('/');
}