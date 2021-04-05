import { html } from "../../node_modules/lit-html/lit-html.js";

import { getArticles } from "../api/data.js";

const homeTemplate = (articles) => html`
<section id="home-page" class="content">
    <h1>Recent Articles</h1>
    <section class="recent js">
        <h2>JavaScript</h2>

        ${getElement(articles, 'JavaScript') === undefined ? html`<h3 class="no-articles">No articles yet</h3>` 
        : articleTemplate(getElement(articles, 'JavaScript'))}

    </section>
    <section class="recent csharp">
        <h2>C#</h2>

        ${getElement(articles, 'C#') === undefined ? html`<h3 class="no-articles">No articles yet</h3>` 
        : articleTemplate(getElement(articles, 'C#'))}

    </section>
    <section class="recent java">
        <h2>Java</h2>

        ${getElement(articles, 'Java') === undefined ? html`<h3 class="no-articles">No articles yet</h3>` 
        : articleTemplate(getElement(articles, 'Java'))}        

    </section>
    <section class="recent python">
        <h2>Python</h2>

        ${getElement(articles, 'Python') === undefined ? html`<h3 class="no-articles">No articles yet</h3>` 
        : articleTemplate(getElement(articles, 'Python'))}

    </section>
</section>`;


const articleTemplate = (article) => html`
<article>
    <h3>${article.title}</h3>
    <p>${article.content}</p>
    <a href="/details/${article._id}" class="btn details-btn">Details</a>
</article>`;

export async function homePage(ctx) {
    const articles = await getArticles();
    ctx.render(homeTemplate(articles));
}

function getElement(articles, categorySearch) {
    return articles.find( ({category }) => category === `${categorySearch}`);
}