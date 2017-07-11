---
layout: page
permalink: /members/
title: BioFoundry Members
description: Current members and alumni
---

<!-- <link rel="stylesheet" href="{{ '/assets/css/members.css' | prepend: site.baseurl | prepend: site.url }}"> -->

<br>
<div class="container">
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'Current' %}
	    <a href="{{ member.url | prepend: site.baseurl | prepend: site.url }}"> 
	        <figure>
	            <img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}">
	            <figcaption>    
	            <b> {{ member.title }} </b>
	            <p><small>{{ member.program }} | since {{ member.year_start }} </small></p>
	            </figcaption>
	        </figure>
	    </a>
	{% endif %}
	{% endfor %}
	</div>
</div>
<br>