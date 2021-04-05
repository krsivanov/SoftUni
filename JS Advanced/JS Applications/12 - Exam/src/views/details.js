import { html } from "../../node_modules/lit-html/lit-html.js";

import { deleteArticle, getArticleById } from "../api/data.js";


const detailsTemplate = (article, isOwner, onDelete) => html`
<section id="details-page" class="content details">
    <h1>Arrays</h1>

    <div class="details-content">
        <strong>Published in category ${article.category}</strong>
        <p>${article.content}</p>

        <div class="buttons">
            ${isOwner ? html`  <a href="/edit/${article._id}" class="btn edit">Edit</a>
            <a @click=${onDelete} href="#" class="btn delete">Delete</a>` : ''}
            <a href="/catalog" class="btn edit">Back</a>
        </div>
    </div>
</section>`;


export async function detailsPage(ctx) {
    const userId = sessionStorage.getItem('userId');
    const articleId = ctx.params.id;
    const article = await getArticleById(articleId);
    const isOwner = userId === article._ownerId;
    ctx.render(detailsTemplate(article, isOwner, onDelete));

    async function onDelete() {
        const confirmed = confirm('Are you sure?');
        if (confirmed) {
            await deleteArticle(articleId);
            ctx.page.redirect('/catalog')
        }
    }
}