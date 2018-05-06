---
layout: simple
permalink: /publications/
title: Publications
description: Innovation does not believe in academic borders. Neither do we! We use insights and methodologies from a variety of scientific and technological domains to meet our objectives.
---

<div class="col-lg-8 col-md-12 text-left">
	<h3 class="publication-anchors" id="articles">Journal Articles</h3><hr><br>
	<ol reversed>
	{% for article in site.data.articles %}
	  <li><p>{{ article.title }}</p></li>
	{% endfor %}
	</ol>
	<br>

	<h3 class="publication-anchors" id="books">Books</h3><hr><br>
	<ol reversed>
	{% for book in site.data.books %}
	  <li><p>{{ book.title }}</p></li>
	{% endfor %}
	</ol>
	<br>

	<h3 class="publication-anchors" id="chapters">Book Chapters</h3><hr><br>
	<ol reversed>
	{% for chapter in site.data.chapters %}
	  <li><p>{{ chapter.title }}</p></li>
	{% endfor %}
	</ol>
	<br>

	<h3 class="publication-anchors" id="invited">Invited Talks and Public Lectures</h3><hr><br>
	<ol reversed>
	{% for invite in site.data.invited %}
	  <li><p>{{ invite.title }}</p></li>
	{% endfor %}
	</ol>
	<br>

	<h3 class="publication-anchors" id="presentations">Oral Presentations</h3><hr><br>
	<ol reversed>
	{% for presentation in site.data.presentations %}
	  <li><p>{{ presentation.title }}</p></li>
	{% endfor %}
	</ol>	
	<br>

	<h3 class="publication-anchors" id="posters">Poster Presentations</h3><hr><br>
	<ol reversed>
	{% for poster in site.data.posters %}
	  <li><p>{{ poster.title }}</p></li>
	{% endfor %}
	</ol>	
	<br>

</div>

<div class="col-lg-4 col-md-12">
	<a href="#articles" type="button" class="list-group-item">
		Articles
	</a>
	<a href="#books" type="button" class="list-group-item">
		Books
	</a>	
	<a href="#chapters" type="button" class="list-group-item">
		Book Chapters
	</a>
	<a href="#invited" type="button" class="list-group-item">
		Invited Talks
	</a>		
	<a href="#presentations" type="button" class="list-group-item">
		Oral Presentations
	</a>
	<a href="#posters" type="button" class="list-group-item">
		Poster Presentations
	</a>			
</div>