---
layout: page
permalink: /members/
title: BioFoundry Members
description: Current members and alumni
---

<!-- <link rel="stylesheet" href="{{ '/assets/css/members.css' | prepend: site.baseurl | prepend: site.url }}"> -->

<br>
<div class="container">
	<!-- <div class="row"> -->
	{% for member in site.members %}
	{% if member.status == 'Current' %}
	<div class="col-md-3 col-sm-6">
	    <!-- <a href="{{ member.url | prepend: site.baseurl | prepend: site.url }}">  -->
	            <center><img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}"></center>
	            <br>
	            <b> {{ member.title }} </b>
	            <small>{{ member.program }} | since {{ member.year_start }} </small>
	</div>
	    <!-- </a> -->
	{% endif %}
	{% endfor %}
	<!-- </div> -->
</div>
<br>