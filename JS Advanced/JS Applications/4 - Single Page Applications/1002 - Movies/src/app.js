import { setupHome } from "./home.js";
import { setupDetails } from "./details.js";
import { setupLogin } from "./login.js";
import { setupRegister } from "./register.js";
import { setupCreate } from "./create.js";
import { setupEdit } from "./edit.js";

const main = document.querySelector('main');

setupSection('home-page',setupHome);

function setupSection(sectionId, setup){
    const section = document.getElementById(section);
    setup(main, section)
}